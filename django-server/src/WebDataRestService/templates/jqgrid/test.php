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
		});

</script>

</head>
<body>
	<table id="list2"></table>
	<div id="pager2"></div>
</body>
</html>
