# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

from django.utils import simplejson

from QueryService import *

# Create your views here.
def index(request):
    template = get_template('index.html')
    variables = Context({
        'head_title' : '기본검색',
        'page_title' : '사용자 관심자 정보를 설정합니다.',
        'page_body' : '어떤 관심사',
    })
    
    output = template.render(variables)
    return HttpResponse(output)

def executeQuery(request):
    if request.method == 'GET':
        queryId=request.GET['queryId']
        queryData=request.GET['queryData']
    elif request.method == 'POST':
        queryId=request.POST['queryId']
        queryData=request.POST['queryData']
    
    dataSet = {}
    
    if not queryData:
        dataSet = createData(queryData)
    
    data = {}
    
    try:
        queryService = QueryService()
        result = queryService.executeQuery(queryId, dataSet)
        
        data["result"] = "true"
        data["data"] = result
    except:
        data["result"] = "false"
    
    return HttpResponse(simplejson.dumps(data), mimetype='application/json')

def updateQuery(request):
    if request.method == 'GET':
        queryId=request.GET['queryId']
        queryData=request.GET['queryData']
    elif request.method == 'POST':
        queryId=request.POST['queryId']
        queryData=request.POST['queryData']
    
    dataSet = {}
    
    if not queryData:
        dataSet = createData(queryData)
    
    data = {}
    
    try:
        queryService = QueryService()
        queryService.executeQuery(queryId, dataSet)
        
        data["result"] = "true"
    except:
        data["result"] = "false"
    
    return HttpResponse(simplejson.dumps(data), mimetype='application/json')

def createData(queryData):
    dataSet = {}
    
    try:
        dataList = queryData.split["|"]
        
        for dataObject in dataList:
            data = dataObject.split["~"]
            dataSet[data[0]] = data[1]
    except:
        pass
    
    return dataSet
