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
    try:
        query_log = TbCmQueryLog.objects.all()
    except:
        return HttpResponse('검색 결과가 없습니다.')
    
    data = list()
    
    for entry in query_log:
        user = {
            'user': entry.user,
            'query_id': entry.query_id,
            'query_text': entry.query_text,
            'getQueryStarDtm': entry.getQueryStarDtm(),
            'getQueryEndDtm': entry.getQueryEndDtm(),    
        }
        
        data.append(user)
    
    return HttpResponse(simplejson.dumps(data), mimetype='application/json')
