# -*- coding: utf-8 -*-

from lxml import etree
from lxml import objectify
from django.core.files import File
import os

init_status = False

class QueryManager(object):
    queryMap = {}
    def __init__(self):
        globals()[self.__class__.__name__] = self
        
        global init_status
        
        if init_status == False:
            self.queryLoad()
            init_status = True
    
    def __call__(self):
        return self
    
    def getQueryInfo(self, queryId):
        queryInfo = self.queryMap.get(queryId)
        
        return queryInfo
    
    def getParam(self, queryInfo, data):
        param = []
        
        try:
            param = queryInfo["parameter"]
        except:
            pass
        
        return self.getQueryParam(param, data)
    
    def getQueryParam(self, param, data):
        paramList = []
        
        if param:
            for p in param:
                paramData = data[p]
                paramList.append(paramData)
        
        return paramList
    
    def queryLoad(self):
        path= os.path.dirname(os.path.abspath(__file__))  
        myfiles = os.path.join(path, 'query-map')  
        os.chdir(myfiles)
        for files in os.listdir("."):
            self.queryLoadXml(files)
    
    def queryLoadXml(self, files):
        tree = objectify.parse(files)
        root = tree.getroot()
        
        for child in root.query:
            queryId = child.get("id")
            
            queryInfo = {}
            
            query = child.sql.text
            query = query.strip()
            query = query.replace("\n", " ")
            query = query.replace("\t", " ")
            
            while query.count("  ") > 0:
                query = query.replace("  ", " ")
            
            queryInfo["query"] = query
            
            paramlist = list()
            
            try:
                for param in child.parameter.param:
                    paramlist.append(param.get("id"));
                
                queryInfo["parameter"] = paramlist
            except:
                pass
            
            self.queryMap[queryId] = queryInfo
            
        print ("Query Map Loader Success!!")

if __name__ == '__main__':
    manager=QueryManager()
    
    queryInfo = manager.getQueryInfo("updateMember")
    
    if not queryInfo:
        print ("Not Query Info")
    else:
        print (queryInfo)

