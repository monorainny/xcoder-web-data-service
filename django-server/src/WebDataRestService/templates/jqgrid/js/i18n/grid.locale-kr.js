;(function($){
/**
 * jqGrid English Translation
 * Tony Tomov tony@trirand.com
 * http://trirand.com/blog/ 
 * Dual licensed under the MIT and GPL licenses:
 * http://www.opensource.org/licenses/mit-license.php
 * http://www.gnu.org/licenses/gpl.html
**/
$.jgrid = {
	defaults : {
		recordtext: "���� {0} - {1} / {2}",
		emptyrecords: "���ڵ尡 �����ϴ�.",
		loadtext: "�ҷ����� ��...",
		pgtext : "������ {0} / {1}"
	},
	search : {
		caption: "�˻�...",
		Find: "ã��",
		Reset: "�ʱ�ȭ",
		odata : ['����', '���� �ʴ�', '����', '���ų� ����','ũ��','���ų� ũ��', '�ܾ�� ����','�ܾ�� ���� �� ��','����ִ� �ܾ�','������� ���� �ܾ�','�ܾ�� ����','�ش� �ܾ�� ������ ����','���Ե�','���Ե��� ����'],
		groupOps: [	{ op: "AND", text: "���" },	{ op: "OR",  text: "�Ǵ�" }	],
		matchText: " ã��",
		rulesText: " ��Ģ"
	},
	edit : {
		addCaption: "�� ���ڵ�",
		editCaption: "���ڵ� ����",
		bSubmit: "����",
		bCancel: "���",
		bClose: "�ݱ�",
		saveData: "�����Ͱ� �ٲ�����ϴ�! �����Ͻðڽ��ϱ�??",
		bYes : "��",
		bNo : "�ƴϿ�",
		bExit : "���",
		msg: {
			required:"�ش� ��Ұ� �ʿ��մϴ�.",
			number:"���ڸ� �־� �ֽʽÿ�.",
			minValue:"���� ���ڴ� �ش� ���ں��� Ŀ�� �մϴ� - ",
			maxValue:"���� ���ڴ� �ش� ���ں��� �۾ƾ� �մϴ� - ",
			email: "�ùٸ� �̸��� �ּҰ� �ƴմϴ�.",
			integer: "�ùٸ� �������� �־� �ֽʽÿ�.",
			date: "�ùٸ� ��¥ �������� �־� �ֽʽÿ�.",
			url: "URL�� ('http://' �Ǵ� 'https://') �������� �����ؾ� �մϴ�."
		}
	},
	view : {
		caption: "���ڵ� ����",
		bClose: "�ݱ�"
	},
	del : {
		caption: "����",
		msg: "���� ���ڵ带 �����Ͻðڽ��ϱ�??",
		bSubmit: "����",
		bCancel: "���"
	},
	nav : {
		edittext: "",
		edittitle: "��å�� �� ����",
		addtext:"",
		addtitle: "�� �߰�",
		deltext: "",
		deltitle: "�� ����",
		searchtext: "",
		searchtitle: "�� ã��",
		refreshtext: "",
		refreshtitle: "�׸��� ���ΰ�ħ",
		alertcap: "���",
		alerttext: "���� �����Ͻʽÿ�.",
		viewtext: "",
		viewtitle: "���� ���ϴ�."
	},
	col : {
		caption: "Į�� ����/���߱�",
		bSubmit: "����",
		bCancel: "���"
	},
	errors : {
		errcap : "����",
		nourl : "URL�� �������� �ʾҽ��ϴ�.",
		norecords: "���ڵ尡 ���� ó������ ���߽��ϴ�.",
		model : "colNames �� colModel ���̰� �޶�� �մϴ�!"
	},
	formatter : {
		integer : {thousandsSeparator: " ", defaultValue: '0'},
		number : {decimalSeparator:".", thousandsSeparator: " ", decimalPlaces: 2, defaultValue: '0.00'},
		currency : {decimalSeparator:".", thousandsSeparator: " ", decimalPlaces: 2, prefix: "", suffix:"", defaultValue: '0.00'},
		date : {
			dayNames:   [
				"��", "��", "ȭ", "��", "��", "��", "��",
				"�Ͽ���", "������", "ȭ����", "������", "�����", "�ݿ���", "�����"
			],
			monthNames: [
				"01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12",
				"1��", "2��", "3��", "4��", "5��", "6��", "7��", "8��", "9��", "10��", "11��", "12��"
			],
			AmPm : ["����","����","����","����"],
			S: '',//function (j) {return j < 11 || j > 13 ? ['st', 'nd', 'rd', 'th'][Math.min((j - 1) % 10, 3)] : 'th'},
			srcformat: 'Y-m-d',
			newformat: 'Y/m/d',
			masks : {
				ISO8601Long:"Y-m-d H:i:s",
				ISO8601Short:"Y-m-d",
				ShortDate: "Y/j/n",
				LongDate: "Y�� F�� d�� l",
				FullDateTime: "Y�� F�� d�� l A g:i:s",
				MonthDay: "F�� d��",
				ShortTime: "A g:i",
				LongTime: "A g:i:s",
				SortableDateTime: "Y-m-d\\TH:i:s",
				UniversalSortableDateTime: "Y-m-d H:i:sO",
				YearMonth: "Y�� F��"
			},
			reformatAfterEdit : false
		},
		baseLinkUrl: '',
		showAction: '',
		target: '',
		checkbox : {disabled:true},
		idName : 'id'
	}
};
})(jQuery);
