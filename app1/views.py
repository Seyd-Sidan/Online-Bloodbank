from django.db import models
from django.shortcuts import render
from .models import doner
from .models import reciever

# Create your views here.
def home(request):
	return render(request,"home.html")


def donerpg(request):
	return render(request,"donerpg.html")


def recieverpg(request):
	return render(request,"recieverreg.html")

def recieverlog(request):
	return render(request,"recieverlog.html")


def doneradd(request):
	response={}
	flag=0
	try:
		n=request.POST["nme"]
		b_t=request.POST["btp"]
		no=request.POST["pno"]
		adr=request.POST["addr"]
		dnr=doner.objects.all()
		for i in dnr:
			if(no==i.phone_no):
				flag=1
		if(flag==1):
			response["msg2"]="Already Registered Under this Number!!!!"
			return render(request,'donerpg.html',response)
		else:
			donerlst=doner(name=n,blood_type=b_t,phone_no=no,address=adr)
			donerlst.save()
			response["msg1"]="Blood Doner Registration Succesfull!!!!"
			return render(request,'donerpg.html',response)
	except Exception as e:
		print(e)
		response["msg3"]="doner cannot be Added!!!!"
		return render(request,'donerpg.html',response)

def recieveradd(request):
	response={}
	flag=0
	try:
		n=request.POST["name"]
		b_t=request.POST["bltp"]
		no=request.POST["phno"]
		adr=request.POST["addrs"]
		rcr=reciever.objects.all()
		for i in rcr:
			if(no==i.phone_no):
				flag=1
		if(flag==1):
			response["msg0"]="Already Registered Under this Number!!!!"
			return render(request,'donerpg.html',response)
		else:
			recieverlst=reciever(name=n,blood_type=b_t,phone_no=no,address=adr)
			recieverlst.save()
			response["msg1"]="Blood Reciever Registration Succesfull!!!!"
			return render(request,'recieverreg.html',response)
	except Exception as e:
		response["msg2"]="Blood Reciever cannot be Added!!!!"
		return render(request,'recieverreg.html',response)


def log(request):
	response={}
	flag=0
	global x
	x=0
	try:
		n=request.POST["name"]
		phone=request.POST["pno"]
		lst1=reciever.objects.all()
		for i in lst1:
			if(n==i.name and phone==i.phone_no):
				flag=1
				x=i.phone_no
				print(x)
		if(flag==1):
			return render(request,'result.html')
		else:
			response["msg1"]="User Not Found!!!"
			return render(request,'recieverlog.html',response)
	except Exception as e:
		response["msg2"]="Login Failed!!"
		return render(request,'recieverlog.html',response)

def display(request):
	global x
	lst=reciever.objects.all()
	for i in lst:
		if(x==i.phone_no):
			a=i.blood_type
	lst2=doner.objects.filter(blood_type=a)
	return render(request,"result.html",{'res':lst2})

def remdnr(request):
	return render(request,"remdoner.html")


def remdoner(request):
	response={}
	try:
		n=request.POST["num"]
		lst3=doner.objects.get(phone_no=n)
		lst3.delete()
		response["msg1"]="Account Deleted Succesfully!!"
		return render(request,'remdoner.html',response)
	except Exception as e:
		print(e)
		response["msg2"]="Account Not Found!!!"
		return render(request,'remdoner.html',response)




