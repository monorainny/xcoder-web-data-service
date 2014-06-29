# -*- coding: utf-8 -*-

from lxml import etree
from lxml import objectify
from django.core.files import File
import os
from LogService.models import TbCmQuery, TbCmQueryParam
from django.db.models.query_utils import Q

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
        try:
            tree = objectify.parse(files)
        except:
            return
        
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
            
            try:
                cmQuery = TbCmQuery.objects.filter(query_id=queryId)[0]
            except:
                cmQuery = TbCmQuery()
                cmQuery.query_id = queryId
                cmQuery.query_desc = child.get("description")
                cmQuery.query_text = query
                cmQuery.action_type = 'P'
                cmQuery.regist_user = 'admin'
                
                cmQuery.save()
            
            paramlist = list()
            
            try:
                index = 1
                
                for param in child.parameter.param:
                    paramId = param.get("id")
                    paramlist.append(paramId);
                    
                    try:
                        cmQueryParam = TbCmQueryParam.objects.filter(query_id=cmQuery.id, param_id=paramId)
                    except Exception, e:
                        cmQueryParam = TbCmQueryParam()
                        cmQueryParam.query_id = cmQuery.id
                        cmQueryParam.param_id = paramId
                        cmQueryParam.param_desc = param.get("description")
                        cmQueryParam.order_index = index
                        
                        try:                        
                            cmQueryParam.save()
                        except Exception, e:
                            pass
                        
                        index = index + 1
                
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

