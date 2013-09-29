# -*- coding: utf-8 -*-

import sqlalchemy.pool as pool
from sqlalchemy import *
from QueryManager import *

engine = None

class QueryService(object):
    manager = None
    
    def __init__(self):
        globals()[self.__class__.__name__] = self
        self.manager=QueryManager()
        
        global engine
        
        if engine is None:
            engine = create_engine("mysql://root:xcoder@14.63.199.221/WebDataRestService", pool_recycle=3600)
            print("Create Engine")
    
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
            executeQuery = queryInfo["query"]
            
            if not dict:
                result = conn.execute(executeQuery)
            else:
                paramInfo = self.manager.getParam(queryInfo, dict);
                result = conn.execute(executeQuery, paramInfo)
        except Exception, e:
            print e
        
        resultList = []
        
        for raw in result:
            data = {}
            
            for column, value in raw.items():
                data[column] = value
            
            resultList.append(data)
        
        print("query exeute success : " + queryId)
        print(resultList)
        
        conn.close()
        
        return resultList