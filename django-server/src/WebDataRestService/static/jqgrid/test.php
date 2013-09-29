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
					url:'/data_load',
					datatype: "json",
					colNames:['Inv No','Date', 'Client', 'Amount','Tax','Total','Notes'],
					colModel:[
						{name:'id',index:'id', width:55},
						{name:'invdate',index:'invdate', width:90},
						{name:'name',index:'name asc, invdate', width:100},
						{name:'amount',index:'amount', width:80, align:"right"},
						{name:'tax',index:'tax', width:80, align:"right"},		
						{name:'total',index:'total', width:80,align:"right"},		
						{name:'note',index:'note', width:150, sortable:false}		
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
