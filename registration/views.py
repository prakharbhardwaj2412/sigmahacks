from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import user ,shopkeeper

# Create your views here.
def signup(request):
	if request.method =="POST":
		print(request.body)
		data= json.loads(request.body)
		username=data['email']

		mobile_nom=data['mobile_no']
		unique_email=user.objects.filter(email=username , mobile_no= mobile_nom).exists()
		if(unique_email):
			message ="This user is already registered"
		else:
			user.objects.create(**data)
			message="Registered Sucessfully"
	return JsonResponse(message,safe=False)  


def shop_signup(request):
	if request.method =="POST":
		print(request.body)
		data= json.loads(request.body)
		username=data['email']
		mobile_nom=data['mobile_no']
		unique_email=shopkeeper.objects.filter(email=username , mobile_no= mobile_nom).exists()
		if(unique_email):
			message ="This user is already registered"
		else:
			shopkeeper.objects.create(**data)
			message="Registered Sucessfully"
	return JsonResponse(message,safe=False)  


def login(request):
	if request.method == "POST":
		print(request.body)
		data= json.loads(request.body)
		username=data['email']
		password=data['password']
		bool_filter=user.objects.filter(email=username,password=password).exists()  
		print(bool_filter)
		if (bool_filter):
			message=list(user.objects.filter(email=username).values('name','email','mobile_no','id','address'))
		else:
			message="invalid credentials"	
	return JsonResponse(message,safe=False)

def shop_login(request):
	if request.method == "POST":
		print(request.body)
		data= json.loads(request.body)
		username=data['email']
		password=data['password']
		bool_filter=shopkeeper.objects.filter(email=username,password=password).exists()  
		print(bool_filter)
		if (bool_filter):
			message=list(shopkeeper.objects.filter(email=username).values('name','email','mobile_no','id','address'))
		else:
			message="invalid credentials"	
	return JsonResponse(message,safe=False)

