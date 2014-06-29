# -*- coding: utf-8 -*-

from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from django.utils import simplejson, timezone
from django.utils.timezone import utc
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

from datetime import datetime

from LogService.models import TbCmQueryLog
from QueryService import *
from django.template.context import RequestContext
import time

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
    
    data['queryId'] = queryId
    
    startTime = get_current_time()
    
    resultData = {}
    
    try:
        queryService = QueryService()
        resultData = queryService.executeQuery(queryId, dataSet, True)
        result = resultData['result']
        
        data["result"] = "true"
        data["data"] = result
    except Exception, e:
        resultData['query_id']=queryId
        resultData['query_text']=queryId
        data["data"] = ''
        data["result"] = "false"
        print e
    
    finishTime = get_current_time()
    
    insertQueryLog('admin', resultData['query_id'], resultData['query_text'], startTime, finishTime)
    
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
    
    data['queryId'] = queryId
    
    startTime = get_current_time()
    
    resultData = {}
    
    try:
        queryService = QueryService()
        resultData = queryService.executeQuery(queryId, dataSet, False)
        
        data["result"] = "true"
    except:
        data["result"] = "false"
    
    finishTime = get_current_time()
    
    insertQueryLog('admin', resultData['query_id'], resultData['query_text'], startTime, finishTime)
    
    return HttpResponse(simplejson.dumps(data), mimetype='application/json')

def createData(queryData):
    dataSet = {}
    dataList = []
    
    try:
        dataList = queryData.split('|')
    except:
        dataList.append(queryData)
    
    for dataObject in dataList:
        data = dataObject.split('=')
        dataSet[data[0]] = data[1]
    
    return dataSet

def insertQueryLog(user_id, query_id, query_text, startTime, finishTime):
    cmQueryLog = TbCmQueryLog()
    
    cmQueryLog.user = user_id
    cmQueryLog.query_id = query_id
    cmQueryLog.query_text = query_text
    cmQueryLog.execute_time = datetime_to_milliseconds(finishTime) - datetime_to_milliseconds(startTime);
    cmQueryLog.query_start_dtm = startTime
    cmQueryLog.query_end_dtm = finishTime
    
    cmQueryLog.save()
    
def get_current_time():
    if USE_TZ:
        return timezone.make_aware(datetime.now(),timezone.get_default_timezone())
    else:
        return timezone.now()

def datetime_to_milliseconds(some_datetime_object):
    '''
    timetuple = some_datetime_object.timetuple()
    timestamp = time.mktime(timetuple)
    return timestamp * 1000.0
    '''
    ms = time.mktime(some_datetime_object.utctimetuple()) * 1000
    ms += getattr(some_datetime_object, 'microseconds', 0) / 1000
    
    return int(ms)
    
