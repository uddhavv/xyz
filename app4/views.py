import json
from django.http import HttpResponse,request
from django.shortcuts import render
from rest_framework.views import *
from django.views.decorators.csrf import csrf_exempt
from . import models
from .models import *
import mysql.connector

class SecondLearningRestAPI(APIView):# insert data in table
    def post(self,request):
        print("++++++++++++++++++",request.data)
        dname = str(request.data['dname'])
        dadd = str(request.data["dadd"])
        # testapp_emp
        print(dname, "************************")
        print(dadd, "************************")
        data=Uvg(dname=dname,dadd=dadd) # Django Database API(insert data) #sql insert query
        data.save()
        return HttpResponse(({"status": 'Scusses'}), status=status.HTTP_201_CREATED)

class getAPI(APIView):
    def get(self,request):
        data=Uvg.objects.values()
        print("Database data",data)
        return HttpResponse(({"status": "Scusses"},{"Uvg":list(data)}), status=status.HTTP_201_CREATED)