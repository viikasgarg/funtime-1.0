var calcDrawn = 0 ;
var firstNum=0;
var op="";
var deci=0;


function hideShowCalc(calc)
{
var hideCalc = 1 ;
var showCalc = 2 ;

operation = document.getElementById('combo1').value;

if(operation == hideCalc)
	{			
       		if(window.confirm("Do u really want to hide calculator"))
		{
			calc.style.visibility="hidden";
		}
	}	
		
if(operation == showCalc)
	{
       		if(window.confirm("Do u really want to Show calculator"))
		{
			if(!calcDrawn)
			{			
				drawCalc(calc);
				calc.style.visibility="visible";
				calcDrawn = 1;
			}
			else
			{
			calc.style.visibility="visible";
			}
		}
	}
			

	
}

function drawCalc(calc)
{	
	var buttons = new Array("1","2","3","+","4","5","6","-","7","8","9","*","0",".","/","=");	
	var textRow=document.createElement("p"); 
	textRow.className = "calc-display"; 
	textRow.innerHTML='<input type="text" Id=screen class="calc-display-input" value=0 onfocus="this.blur()">';
	calc.appendChild(textRow);
	
	var clearRow=document.createElement("p"); 
	clearRow.className = "calc-row"; 
	clearRow.innerHTML='<input class="calc-button calc-button-yellow calc-button-big" type="button" size=20 value="CLR" onclick=DoCalc(value);>';
	calc.appendChild(clearRow);
	
	for (var rows = 0; rows < 4;rows++)
	{
		//var row=calc.insertRow(-1);
		var row=document.createElement("p"); //calc.insertRow(-1);
		row.className = "calc-row"; 
		for (var cols=0;cols<4;cols++)
		{	
			//var cell=row.insertCell(-1);
			var val = buttons[rows*4+cols];
			var class_name = ''
			if (val in {1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1,0:1})
				class_name =  '"calc-button"';
			if(val in {"+":1,"-":1,"*":1,"/":1,".":1})
				class_name =  '"calc-button calc-button-red calc-button-big"';
			if (val=="=")
				class_name =  '"calc-button calc-button-yellow calc-button-big"';
			row.innerHTML+='<input class='+class_name + ' type="button" size=10 value='+ val + ' onclick=DoCalc(value);>';
		}
		calc.appendChild(row);
	}	

}

function DoCalc(val)
{
	if(val == "CLR") {
		firstNum=0;
		op="";
		deci=0;
		document.getElementById('screen').value = 0;
		return; 
	}
	if(val.indexOf(".") > -1 && document.getElementById('screen').value.indexOf(".") < 0)
	{ 	
		if(!deci) 
		{	
			document.getElementById('screen').value+=val;
			deci=1;
		}
	}

	if (val in {1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1,0:1})
		if(document.getElementById('screen').value!=0 ||
           document.getElementById('screen').value.indexOf(".") > -1)
			document.getElementById('screen').value+=val;
		else
			document.getElementById('screen').value=val;
	
	if(val in {"+":1,"-":1,"*":1,"/":1})
	{
		firstNum=document.getElementById('screen').value;
		document.getElementById('screen').value="0";	
		oper=val;
		deci=0;

	}

	if (val=="=")
	{
		try	
		{
			document.getElementById('screen').value=eval(firstNum+oper+document.getElementById('screen').value).toPrecision(12).replace(/\.?0+$/,"");
			firstNum=document.getElementById('screen').value;
			deci=0;
		}
		catch(e)
		{
			window.alert("wrong format \n"+e.message);
		}
	}
}