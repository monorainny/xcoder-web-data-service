# -*- coding: utf-8 -*-

from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from django.utils import simplejson
from django.utils.timezone import utc
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

from datetime import datetime

from LogService.models import TbCmQueryLog
from QueryService import *
from django.template.context import RequestContext

USE_TZ = getattr(settings, 'USE_TZ', False)

# Create your views here.
def index(request):
    template = get_template('index.html')
    variables = RequestContext(request, {
        'head_title' : '기본검색',
        'page_title' : '사용자 관심자 정보를 설정합니다.',
    })
    
    output = template.render(variables)
    return HttpResponse(output)

@csrf_exempt
@ensure_csrf_cookie
def executeQuery(request):
    if request.method == 'GET':
        queryId=request.GET['queryId']
        queryData=request.GET['queryData']
    elif request.method == 'POST':
        queryId=request.POST['queryId']
        queryData=request.POST['queryData']
    
    dataSet = {}
    
    if queryData is not None and queryData != '':
        dataSet = createData(queryData)
    
    data = {}
    
    startTime = get_current_time()
    
    try:
        queryService = QueryService()
        result = queryService.executeQuery(queryId, dataSet, True)
        
        data["result"] = "true"
        data["data"] = result
    except Exception, e:
        data["result"] = "false"
        print e
    
    finishTime = get_current_time()
    
    insertQueryLog('admin', queryId, startTime, finishTime)
    
    return HttpResponse(simplejson.dumps(data), mimetype='application/json')

@csrf_exempt
@ensure_csrf_cookie
def updateQuery(request):
    if request.method == 'GET':
        queryId=request.GET['queryId']
        queryData=request.GET['queryData']
    elif request.method == 'POST':
        queryId=request.POST['queryId']
        queryData=request.POST['queryData']
    
    dataSet = {}
    
    if queryData is not None and queryData != '':
        dataSet = createData(queryData)
    
    data = {}
    
    startTime = get_current_time()
    
    try:
        queryService = QueryService()
        queryService.executeQuery(queryId, dataSet, False)
        
        data["result"] = "true"
    except Exception, e:
        data["result"] = "false"
        print e
    
    finishTime = get_current_time()
    
    insertQueryLog('admin', queryId, startTime, finishTime)
    
    return HttpResponse(simplejson.dumps(data), mimetype='application/json')

def createData(queryData):
    dataSet = {}
    dataList = []
    
    try:
        dataList = queryData.split('|')
    except Exception, e:
        dataList.append(queryData)
        print type(e);
    
    for dataObject in dataList:
        data = dataObject.split('=')
        dataSet[data[0]] = data[1]
    
    return dataSet

def insertQueryLog(user_id, query_id, startTime, finishTime):
    cmQueryLog = TbCmQueryLog()
    
    cmQueryLog.user = user_id
    cmQueryLog.query_id = query_id
    cmQueryLog.query_text = ''
    cmQueryLog.query_start_dtm = startTime
    cmQueryLog.query_end_dtm = finishTime
    
    cmQueryLog.save()
    
def get_current_time():
    """
    Returns the current time setting the django timezone if the site is using
    timezones.
    """
    if USE_TZ:
        return datetime.utcnow().replace(tzinfo=utc)
    else:
        return datetime.now()
