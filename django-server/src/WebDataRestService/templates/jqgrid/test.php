<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>

<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>Insert title here</title>

	<link href="http://jkdrama.cafe24.com/jqgrid/css/jquery-ui-1.8.21.custom.css" rel="stylesheet" type="text/css" />
	<link href="http://jkdrama.cafe24.com/jqgrid/css/ui.jqgrid.css" rel="stylesheet" type="text/css" />

	<script src="http://jkdrama.cafe24.com/jqgrid/js/jquery-1.7.2.min.js" type="text/javascript"></script>
	<script src="http://jkdrama.cafe24.com/jqgrid/js/i18n/grid.locale-kr_utf-8.js" type="text/javascript"></script>
	<script src="http://jkdrama.cafe24.com/jqgrid/js/jquery.jqGrid.min.js" type="text/javascript"></script>

	<script type="text/javascript">
		jQuery(document).ready(function(){
				if ('{{ data_type }}' == 'schema')
				{
					jQuery("#list2").jqGrid({
						url:'/data_load/{{ data_type }}',
						datatype: "json",
						colNames:['TABLE_SCHEMA', 'TABLE_NAME', 'TABLE_ROWS', 'DATA_LENGTH', 'INDEX_LENGTH', 'CREATE_TIME'],
						colModel:[
							{name:'테이블스키마',index:'TABLE_SCHEMA', width:140, align:"left"},
							{name:'테이블명',index:'TABLE_NAME', width:140, align:"left"},
							{name:'테이블행수',index:'TABLE_ROWS', width:80, align:"right"},
							{name:'데이타길이',index:'DATA_LENGTH', width:80, align:"right"},
							{name:'인덱스길이',index:'INDEX_LENGTH', width:80, align:"right"},
							{name:'생성일',index:'CREATE_TIME', width:150, align:"center"}
						],
						rowNum:10,
						rowList:[10,20,30],
						pager: '#pager2',
						sortname: 'TABLE_SCHEMA',
						viewrecords: true,
						sortorder: "desc",
						caption:"테이블 목록"
					});
					jQuery("#list2").jqGrid('navGrid','#pager2',{edit:false,add:false,del:false});
				}
				else if ('{{ data_type }}' == 'account')
				{
					jQuery("#list2").jqGrid({
						url:'/data_load/{{ data_type }}',
						datatype: "json",
						colNames:['Host', 'User'],
						colModel:[
							{name:'접속구분',index:'Host', width:240, align:"center"},
							{name:'사용자',index:'User', width:150, align:"center"}
						],
						rowNum:10,
						rowList:[10,20,30],
						pager: '#pager2',
						sortname: 'User',
						viewrecords: true,
						sortorder: "desc",
						caption:"DB 사용자 목록"
					});
					jQuery("#list2").jqGrid('navGrid','#pager2',{edit:false,add:false,del:false});
				}
				else if ('{{ data_type }}' == 'usage')
				{
					jQuery("#list2").jqGrid({
						url:'/data_load/{{ data_type }}',
						datatype: "json",
						colNames:['database_name', 'size(MB)'],
						colModel:[
							{name:'데이타베이스명',index:'database_name', width:240, align:"center"},
							{name:'크기(MB)',index:'size', width:150, align:"right"}
						],
						rowNum:10,
						rowList:[10,20,30],
						pager: '#pager2',
						sortname: 'size',
						viewrecords: true,
						sortorder: "desc",
						caption:"사용공간 목록"
					});
					jQuery("#list2").jqGrid('navGrid','#pager2',{edit:false,add:false,del:false});
				}
				else if ('{{ data_type }}' == 'history')
				{
					jQuery("#list2").jqGrid({
						url:'/data_load/{{ data_type }}',
						datatype: "json",
						colNames:['id', 'User', 'Query', 'Start Date', 'End Date'],
						colModel:[
							{name:'id',index:'id', width:40, align:"right"},
							{name:'사용자',index:'user', width:80, align:"center"},
							{name:'쿼리',index:'query_id', width:200},
							{name:'쿼리실행시작시각',index:'query_start_dtm', width:150, align:"center"},
							{name:'쿼리실행종료시각',index:'query_end_dtm', width:150, align:"center"}
						],
						rowNum:10,
						rowList:[10,20,30],
						pager: '#pager2',
						sortname: 'id',
						viewrecords: true,
						sortorder: "desc",
						caption:"쿼리 실행 목록"
					});
					jQuery("#list2").jqGrid('navGrid','#pager2',{edit:false,add:false,del:false});
				}
				else if ('{{ data_type }}' == 'statistic')
				{
					jQuery("#list2").jqGrid({
						url:'/data_load/{{ data_type }}',
						datatype: "json",
						colNames:['query id', 'count'],
						colModel:[
							{name:'쿼리내용',index:'query_id', width:240, align:"left"},
							{name:'횟수',index:'count', width:150, align:"right"}
						],
						rowNum:10,
						rowList:[10,20,30],
						pager: '#pager2',
						sortname: 'query_id',
						viewrecords: true,
						sortorder: "desc",
						caption:"쿼리 실행 빈도 목록"
					});
					jQuery("#list2").jqGrid('navGrid','#pager2',{edit:false,add:false,del:false});
				}
				else if ('{{ data_type }}' == 'connect')
				{
					jQuery("#list2").jqGrid({
						url:'/data_load/{{ data_type }}',
						datatype: "json",
						colNames:['id', 'user_id', 'user_name', 'last login date'],
						colModel:[
							{name:'id',index:'id', width:40, align:"center"},
							{name:'사용자',index:'user_id', width:240, align:"center"},
							{name:'사용자명',index:'user_name', width:240, align:"left"},
							{name:'최종접속일',index:'last_login', width:150,align:"center"}
						],
						rowNum:10,
						rowList:[10,20,30],
						pager: '#pager2',
						sortname: 'query_id',
						viewrecords: true,
						sortorder: "desc",
						caption:"접속정보 목록"
					});
					jQuery("#list2").jqGrid('navGrid','#pager2',{edit:false,add:false,del:false});
				}
				else if ('{{ data_type }}' == 'admin')
				{
					jQuery("#list2").jqGrid({
						url:'/data_load/{{ data_type }}',
						datatype: "json",
						colNames:['id', 'user_id', 'user_name', 'regist date'],
						colModel:[
							{name:'id',index:'id', width:40, align:"center"},
							{name:'사용자',index:'user_id', width:240, align:"left"},
							{name:'사용자명',index:'user_name', width:240, align:"left"},
							{name:'등록일',index:'regist_date', width:150, align:"center"}
						],
						rowNum:10,
						rowList:[10,20,30],
						pager: '#pager2',
						sortname: 'query_id',
						viewrecords: true,
						sortorder: "desc",
						caption:"USER정보 목록"
					});
					jQuery("#list2").jqGrid('navGrid','#pager2',{edit:false,add:false,del:false});
				}
		});

</script>

</head>
<body>
	<table id="list2"></table>
	<div id="pager2"></div>
</body>
</html>
