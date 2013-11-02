# -*- coding: utf-8 -*-
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import Context, RequestContext
from django.template.loader import get_template
from django.template.response import TemplateResponse
from django.utils import simplejson

from LogService.models import TbCmQueryLog, TbCmUserAuth
from DbService.QueryService import *
from django.db.models.aggregates import Count, Avg

def index(request):
    template = get_template('default.html')
    variables = Context({
        'head_title' : '기본검색',
        'page_title' : '사용자 관심자 정보를 설정합니다.',
        'page_body' : '어떤 관심사',
    })
    
    output = template.render(variables)
    return HttpResponse(output)

def top(request):
    return render_to_response('top.html', RequestContext(request, {'user': request.user}));

def left(request):
    return render_to_response('left.html', RequestContext(request, {'user': request.user}));

def main(request):
    return render_to_response('main.html', RequestContext(request, {'user': request.user}));

@login_required(login_url='/accounts/login/')
def jqgrid_main(request, data_type):
    template = get_template('jqgrid/test.php')
    variables = RequestContext(request, {
        'user': request.user,
        'data_type' : data_type,
    })
    
    output = template.render(variables)
    return HttpResponse(output)

def data_load(request, data_type):
    if request.method == 'GET':
        search=request.GET['_search']
        nd=request.GET['nd']
        rows=int(request.GET['rows'])
        page=int(request.GET['page']) - 1
        sidx=request.GET['sidx']
        sord=request.GET['sord']
    elif request.method == 'POST':
        search=request.POST['_search']
        nd=request.POST['nd']
        rows=int(request.POST['rows'])
        page=int(request.POST['page']) - 1
        sidx=request.POST['sidx']
        sord=request.POST['sord']
    
    if sord != 'asc':
        sidx = '-' + sidx
    
    query_log = getDataToDataType(data_type, search, rows, page, sidx, sord)
    
    data = getResultData(data_type, query_log)
    
    resultData = {}
    
    resultData['page'] = page + 1
    resultData['records'] = len(query_log)
    resultData['rows'] = data
    resultData['total'] = TbCmQueryLog.objects.all().count() / rows + 1
    
    return HttpResponse(simplejson.dumps(resultData), mimetype='application/json')

def getDataToDataType(data_type, search, rows, page, sidx, sord):
    try:
        if data_type == 'schema' or data_type == 'account' or data_type == 'usage':
            queryResult = dbQueryExecute(data_type)
            query_log = queryResult['data']
        elif data_type == 'history':
            if search != 'false':
                query_log = TbCmQueryLog.objects.order_by(sidx).filter(query_id__icontains=search)[page * rows:page * rows + rows]
            else:
                query_log = TbCmQueryLog.objects.order_by(sidx).all()[page * rows:page * rows + rows]
        elif data_type == 'statistic':
            query_log = TbCmQueryLog.objects.values('query_id').annotate(execute_count=Count('query_id'),execute_time=Avg('execute_time')).order_by('-execute_count')[0:10]
        elif data_type == 'connect':
            query_log = TbCmUserAuth.objects.all()
        elif data_type == 'admin':
            query_log = TbCmUserAuth.objects.all()
    except Exception, e:
        return HttpResponse('검색 결과가 없습니다.')
    
    return query_log

def getResultData(data_type, query_log):
    data = []
    
    for entry in query_log:
        cell = []
        row_data = {}
        
        if data_type == 'schema':
            cell.append(entry['TABLE_SCHEMA'])
            cell.append(entry['TABLE_NAME'])
            cell.append(entry['TABLE_ROWS'])
            cell.append(entry['DATA_LENGTH'])
            cell.append(entry['INDEX_LENGTH'])
            cell.append(entry['CREATE_TIME'].strftime("%Y-%m-%d %H:%M:%S"))
            
            row_data['id'] = entry['TABLE_SCHEMA']
        elif data_type == 'account':
            cell.append(entry['Host'])
            cell.append(entry['User'])
            
            row_data['id'] = entry['Host']
        elif data_type == 'usage':
            cell.append(entry['database_name'])
            cell.append(str(entry['size']))
            
            row_data['id'] = entry['database_name']
        elif data_type == 'history':
            query = entry.query_id
            
            if query == '':
                query = entry.query_text[:20]
            
            cell.append(int(entry.id))
            cell.append(entry.user)
            cell.append(query)
            cell.append(entry.getQueryStarDtm())
            cell.append(entry.getQueryEndDtm())
            
            row_data['id'] = int(entry.id)
        elif data_type == 'statistic':
            cell.append(entry['query_id'])
            cell.append(entry['execute_count'])
            cell.append(entry['execute_time'])
            
            row_data['id'] = entry['query_id']
        elif data_type == 'connect':
            cell.append(int(entry.id))
            cell.append(entry.user_id)
            cell.append(entry.user_name)
            cell.append(entry.last_login_dtm.strftime("%Y-%m-%d %H:%M:%S"))
            
            row_data['id'] = int(entry.id)
        elif data_type == 'admin':
            cell.append(int(entry.id))
            cell.append(entry.user_id)
            cell.append(entry.user_name)
            cell.append(entry.regist_dtm.strftime("%Y-%m-%d %H:%M:%S"))
            
            row_data['id'] = int(entry.id)
        
        row_data['cell'] = cell
        
        data.append(row_data)
    
    return data

def dbQueryExecute(data_type):
    query = ""
    dataSet = []
    
    if data_type == 'schema':
        query = "SELECT TABLE_SCHEMA, TABLE_NAME, TABLE_ROWS, DATA_LENGTH, INDEX_LENGTH, CREATE_TIME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = SCHEMA()"
    elif data_type == 'account':
        query = "select Host, User from mysql.user"
    elif data_type == 'usage':
        query = "SELECT table_schema 'database_name', SUM(data_length + index_length) / 1024 / 1024 'size' FROM information_schema.TABLES GROUP BY table_schema"
    
    result = {}
    
    try:
        queryService = QueryService()
        resultData = queryService.executeQuery(query, dataSet, True)
        executeResult = resultData['result']
        
        result["result"] = "true"
        result["data"] = executeResult
    except Exception, e:
        result["result"] = "false"
        print e
    
    return result

def main_refresh(request):
    return TemplateResponse(request, 'page_redirect.html', {'redirect_url':'/'})

def accounts_regist(request):
    return render_to_response('registration/regist_member.html', RequestContext(request, {'user': request.user}));

def accounts_regist_action(request):
    if request.method == 'GET':
        mail=request.GET['mail']
        password=request.GET['password']
        name=request.GET['name']
    elif request.method == 'POST':
        mail=request.POST['mail']
        password=request.POST['password']
        name=request.POST['name']
    
    message = "Already registed email address!!"
    
    try:
        current_entry = TbCmUserAuth.objects.get(user_id=mail)
    except:
        newMember = TbCmUserAuth()
        newMember.user_id = mail
        newMember.user_passwd = password
        newMember.user_name = name
        newMember.user_status = 'A'
        
        message = "success"
        
        try:
            newMember.save()
            
            User.objects.create_user(mail, mail, password)
        except:
            message = "Save Error"
    
    data = {'result_message' : message}
    
    return HttpResponse(simplejson.dumps(data), mimetype='application/json')

def accounts_info(request):
    login_user = TbCmUserAuth.objects.get(user_id=request.user.username)
    
    return render_to_response('registration/member.html', RequestContext(request, {'user': request.user, 'user_id':login_user.user_id, 'user_name':login_user.user_name}));

def accounts_info_modify(request):
    if request.method == 'GET':
        mail=request.GET['mail']
        password=request.GET['password']
        name=request.GET['name']
    elif request.method == 'POST':
        mail=request.POST['mail']
        password=request.POST['password']
        name=request.POST['name']
    
    member = TbCmUserAuth.objects.get(Email=mail)
    member.Email = mail
    member.Password = password
    member.Name = name
    message = "success"
    
    try:
        member.save()
        
        User.objects.create_user(mail, mail, password)
    except:
        message = "Save Error"
    
    data = {'result_message' : message}
    
    return HttpResponse(simplejson.dumps(data), mimetype='application/json')

def logout_page(request):
    logout(request)
    return TemplateResponse(request, 'page_redirect.html', {'redirect_url':'/'})

