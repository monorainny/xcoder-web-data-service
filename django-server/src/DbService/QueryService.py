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
    
    def executeQuery(self, queryId, dict, resultFlag):
        resultData = {}
        resultData['query_id'] = ''
        resultData['query_text'] = ''
        
        conn = engine.connect()
        queryInfo = self.manager.getQueryInfo(queryId)
        
        result = {}
        
        try:
            try:
                executeQuery = queryInfo["query"]
                resultData['query_id'] = executeQuery
            except:
                executeQuery = queryId
                resultData['query_text'] = executeQuery
            
            if not dict:
                result = conn.execute(executeQuery)
            else:
                paramInfo = self.manager.getParam(queryInfo, dict);
                result = conn.execute(executeQuery, paramInfo)
            resultData['status'] = 'success'
        except:
            resultData['status'] = 'fail'
            raise
        finally:
            conn.close()
        
        print("query exeute success : " + queryId)
        
        if resultFlag and result is not null:   
            resultList = []
            
            for raw in result:
                data = {}
                
                for column, value in raw.items():
                    data[column] = value
                
                resultList.append(data)
            
            resultData['result'] = resultList
            return resultData
        
        return resultData