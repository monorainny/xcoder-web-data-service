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
							{name:'TABLE_SCHEMA',index:'TABLE_SCHEMA', width:140, align:"right"},
							{name:'TABLE_NAME',index:'TABLE_NAME', width:140, align:"right"},
							{name:'TABLE_ROWS',index:'TABLE_ROWS', width:80},
							{name:'DATA_LENGTH',index:'DATA_LENGTH', width:80},
							{name:'INDEX_LENGTH',index:'INDEX_LENGTH', width:80},
							{name:'CREATE_TIME',index:'CREATE_TIME', width:150}
						],
						rowNum:10,
						rowList:[10,20,30],
						pager: '#pager2',
						sortname: 'TABLE_SCHEMA',
						viewrecords: true,
						sortorder: "desc",
						caption:"JSON Example"
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
							{name:'Host',index:'Host', width:240, align:"right"},
							{name:'User',index:'User', width:150}
						],
						rowNum:10,
						rowList:[10,20,30],
						pager: '#pager2',
						sortname: 'User',
						viewrecords: true,
						sortorder: "desc",
						caption:"JSON Example"
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
							{name:'database_name',index:'database_name', width:240, align:"right"},
							{name:'size',index:'size', width:150}
						],
						rowNum:10,
						rowList:[10,20,30],
						pager: '#pager2',
						sortname: 'size',
						viewrecords: true,
						sortorder: "desc",
						caption:"JSON Example"
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
							{name:'user',index:'user', width:80, align:"right"},
							{name:'query_id',index:'query_id', width:200},
							{name:'query_start_dtm',index:'query_start_dtm', width:150},
							{name:'query_end_dtm',index:'query_end_dtm', width:150}
						],
						rowNum:10,
						rowList:[10,20,30],
						pager: '#pager2',
						sortname: 'id',
						viewrecords: true,
						sortorder: "desc",
						caption:"JSON Example"
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
							{name:'query_id',index:'query_id', width:240, align:"right"},
							{name:'count',index:'count', width:150}
						],
						rowNum:10,
						rowList:[10,20,30],
						pager: '#pager2',
						sortname: 'query_id',
						viewrecords: true,
						sortorder: "desc",
						caption:"JSON Example"
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
							{name:'id',index:'id', width:40, align:"right"},
							{name:'user_id',index:'user_id', width:240, align:"right"},
							{name:'user_name',index:'user_name', width:240, align:"right"},
							{name:'last_login',index:'last_login', width:150}
						],
						rowNum:10,
						rowList:[10,20,30],
						pager: '#pager2',
						sortname: 'query_id',
						viewrecords: true,
						sortorder: "desc",
						caption:"JSON Example"
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
							{name:'id',index:'id', width:40, align:"right"},
							{name:'user_id',index:'user_id', width:240, align:"right"},
							{name:'user_name',index:'user_name', width:240, align:"right"},
							{name:'regist_date',index:'regist_date', width:150}
						],
						rowNum:10,
						rowList:[10,20,30],
						pager: '#pager2',
						sortname: 'query_id',
						viewrecords: true,
						sortorder: "desc",
						caption:"JSON Example"
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
