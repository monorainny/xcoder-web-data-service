# -*- coding: utf-8 -*-
from django.template.loader import get_template
from django.template.context import Context, RequestContext
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson
from LogService.models import TbCmQueryLog

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
    return render_to_response('top.html', RequestContext(request));

def left(request):
    return render_to_response('left.html', RequestContext(request));

def main(request):
    return render_to_response('main.html', RequestContext(request));

def jqgrid_main(request):
    return render_to_response('jqgrid/test.php', RequestContext(request));

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
    except Exception, e:
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
