# -*- coding: utf-8 -*-

from django.db import models

class TbCmUserAuth(models.Model):
    """
    사용자 정보 테이블 모델
    @param user_id : 사용자 아이디
    @param user_name : 사용자 이름
    @param user_passwd : 사용자 비밀번호
    @param user_status : 사용자 상태 정보 (R : 등록상태 / A : 사용허가 / D : 사용중지 / I : 유휴상태)
    @param last_login_dtm : 마지막 수행 시간
    @param regist_dtm : 사용자 등록 시간
    """
    user_id = models.CharField(max_length=40,null=True)
    user_name = models.CharField(max_length=40,null=False)
    user_passwd = models.CharField(max_length=80,null=False)
    user_status = models.CharField(max_length=1,null=False)
    last_login_dtm = models.DateTimeField(auto_now=True)
    regist_dtm = models.DateTimeField(auto_now_add=True)

class TbCmQuery(models.Model):
    """
    쿼리 테이블 모델
    @param query_id : 쿼리 아이디
    @param query_desc : 쿼리 설명
    @param query_text : 쿼리
    @param action_type : 쿼리 수행 구분 타입
    @param regist_user : 쿼리 등록자
    """
    query_id = models.CharField(max_length=20,null=True)
    query_desc = models.CharField(max_length=200,null=False)
    query_text = models.TextField()
    action_type = models.CharField(max_length=1,null=False)
    regist_user = models.ForeignKey(TbCmUserAuth)

class TbCmQueryParam(models.Model):
    """
    쿼리 파라미터 테이블 모델
    @param query : 쿼리 아이디 정보
    @param param_id : 파라미터 아이디
    @param param_desc : 파라미터 설명
    @param order_index : 파라미터 순서
    """
    query = models.ForeignKey(TbCmQuery)
    param_id = models.CharField(max_length=200,null=True)
    param_desc = models.CharField(max_length=200,null=False)
    order_index = models.IntegerField()

class TbCmQueryLog(models.Model):
    """
    쿼리 수행 로그 테이블 모델
    @param regist_dtm : 로그 등록 시간
    @param user : 쿼리 수행 아이디
    @param query_id : 쿼리 수행 아이디
    @param query_text : 쿼리 수행 내용
    @param query_start_dtm : 쿼리 수행 시작 시간
    @param query_end_dtm : 쿼리 수행 종료 시간
    """
    regist_dtm = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(TbCmUserAuth)
    query_id = models.CharField(max_length=20,null=True)
    query_text = models.TextField()
    query_start_dtm = models.DateTimeField()
    query_end_dtm = models.DateTimeField()
    
    def getQueryStarDtm(self):
        return self.QueryStartDtm.strftime("%Y-%m-%d %H:%M:%S")
    
    def getQueryEndDtm(self):
        return self.QueryEndDtm.strftime("%Y-%m-%d %H:%M:%S")

