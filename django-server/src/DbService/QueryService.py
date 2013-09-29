# -*- coding: utf-8 -*-

import sqlalchemy.pool as pool
from sqlalchemy import *
from QueryManager import *

engine = create_engine("mysql://root:monorain@127.0.0.1/WebDataRestService", pool_recycle=3600)
print("Create Engine")

class QueryService(object):
    manager = None
    
    def __init__(self):
        globals()[self.__class__.__name__] = self
        self.manager=QueryManager()
    
    def __call__(self):
        return self
    
    def executeUpdate(self, queryId, dict):
        conn = engine.connect()
        queryInfo = self.manager.getQueryInfo(queryId)
        
        try:
            if not dict:
                executeQuery = queryInfo["query"];
                conn.execute(executeQuery)
            else:
                paramInfo = self.manager.getParam(queryInfo, dict);
                conn.execute(queryInfo["query"], paramInfo)
        except exc.DBAPIError, e:
            if e.connection_invalidated:
                print "Connection was invalidated!"
            else:
                raise exc.DisconnectionError()
        except Exception, e:
            print type(e)
            
        print("query update success : " + queryId)
        conn.close()
        
    def executeQuery(self, queryId, dict):
        conn = engine.connect()
        queryInfo = self.manager.getQueryInfo(queryId)
        
        result = {}
        
        try:
            if not dict:
                result = conn.execute(queryInfo["query"])
            else:
                paramInfo = self.manager.getParam(queryInfo, dict);
                result = conn.execute(queryInfo["query"], paramInfo)
        except:
            pass
        
        fieldList = result._metadata.keys
        
        resultList = []
        
        for raw in result:
            data = {}
            
            for field in fieldList:
                field = field.encode("utf-8")
                data[field] = raw[field].encode("utf-8")
            
            resultList.append(data)
        
        print("query exeute success : " + queryId)
        print(resultList)
        
        conn.close()
        
        return resultList