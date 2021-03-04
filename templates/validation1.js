function validate(){
	var n=document.myform.nme.value;
	var bt=document.myform.btp.value;
	var num=document.myform.pno.value;
	var adr=document.myform.addr.value;


	if(n==""){
		document.getElementById('ne').innerHTML="*Name Required";
		return false;
	}
	else{
		document.getElementById('ne').innerHTML="";
	}

	if(bt==""){
		document.getElementById('bp').innerHTML="*Blood_Type Required";
		return false;

	}
	else{
		document.getElementById('bp').innerHTML="";
	}

	if(num==""){
		document.getElementById('pn').innerHTML="*Phone Number Required";
		return false;
	}
	else{
		document.getElementById('pn').innerHTML="";

	}

	if(adr==""){
		document.getElementById('ad').innerHTML="*Address Required";
		return false;

	}
	else{
		document.getElementById('ad').innerHTML="";
		
	}