# -*- coding: utf-8 -*-
import sqlalchemy.pool as pool
from sqlalchemy import *
from QueryManager import *
from sqlalchemy.engine.result import ResultProxy

engine = None

class QueryService(object):
    manager = None
    
    def __init__(self):
        globals()[self.__class__.__name__] = self
        self.manager=QueryManager()
        
        global engine
        
        if engine is None:
            engine = create_engine("mysql://root:xcoder@14.63.199.221/WebDataRestService?charset=utf8&use_unicode=0", pool_recycle=3600)
            print("Create Engine")
    
    def __call__(self):
        return self
    
    def executeQuery(self, queryId, dict, resultFlag):
        resultData = {}
        resultData['query_id'] = ''
        resultData['query_text'] = ''
        
        conn = engine.connect()
        queryInfo = self.manager.getQueryInfo(queryId)
        
        queryResult = {}
        
        try:
            try:
                executeQuery = queryInfo["query"]
                resultData['query_id'] = queryId
                resultData['query_text'] = executeQuery
            except:
                executeQuery = queryId
                resultData['query_id'] = 'User Define Query'
                resultData['query_text'] = executeQuery
            
            if not dict:
                queryResult = conn.execute(executeQuery)
            else:
                paramInfo = self.manager.getParam(queryInfo, dict);
                queryResult = conn.execute(executeQuery, paramInfo)
            resultData['status'] = 'success'
        except:
            resultData['status'] = 'fail'
            raise
        finally:
            conn.close()
        
        print("query exeute success : " + queryId)
        
        resultData['result'] = []
        
        result = []
        
        if type(queryResult) == ResultProxy:
            result = [r for r in queryResult]
        else:
            result = queryResult
        
        if resultFlag and result is not null and len(result) > 0:   
            resultList = []
            
            for raw in result:
                data = {}
                
                for column, value in raw.items():
                    data[column] = value
                
                resultList.append(data)
            
            resultData['result'] = resultList
            return resultData
        
        return resultData