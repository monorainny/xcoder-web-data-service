# -*- coding: utf-8 -*-
from django.template.loader import get_template
from django.template.context import Context, RequestContext
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.utils import simplejson
from LogService.models import TbCmQueryLog, TbCmUserAuth
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.contrib.auth import authenticate
from django.contrib.auth.views import login, logout
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

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
def jqgrid_main(request):
    return render_to_response('jqgrid/test.php', RequestContext(request, {'user': request.user}));

def data_load(request):
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
    
    try:
        if search != 'false':
            query_log = TbCmQueryLog.objects.order_by(sidx).filter(query_id__icontains=search)[page * rows:page * rows + rows]
        else:
            query_log = TbCmQueryLog.objects.order_by(sidx).all()[page * rows:page * rows + rows]
    except:
        return HttpResponse('검색 결과가 없습니다.')
    
    data = []
    
    for entry in query_log:
        cell = []
        
        cell.append(int(entry.id))
        cell.append(entry.user)
        cell.append(entry.query_id)
        cell.append(entry.getQueryStarDtm())
        cell.append(entry.getQueryEndDtm())
        
        row_data = {}
        
        row_data['id'] = int(entry.id)
        row_data['cell'] = cell
        
        data.append(row_data)
    
    resultData = {}
    
    resultData['page'] = page + 1
    resultData['records'] = query_log.count()
    resultData['rows'] = data
    resultData['total'] = TbCmQueryLog.objects.all().count() / rows + 1
    
    return HttpResponse(simplejson.dumps(resultData), mimetype='application/json')

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

