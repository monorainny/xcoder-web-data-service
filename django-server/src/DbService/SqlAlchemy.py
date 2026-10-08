# -*- coding: utf-8 -*-

from QueryService import *

if __name__ == '__main__':
    queryService = QueryService()
    
    queryService.executeUpdate("CreateTable", {})
    
    queryService = QueryService()
    
    dict = {"username":"foo", "password":"bar"}
    queryService.executeUpdate("InsertUser", dict)
    
    queryService = QueryService()
    result = queryService.executeQuery("SelectUser", {})
