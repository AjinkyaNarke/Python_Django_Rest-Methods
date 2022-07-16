from asyncio import streams
import json
from django.shortcuts import render
import io
from rest.models import Student
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse



def Studet_api(request):
    if request.method == 'GET':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pydata=JSONParser().parse(stream)
        id=pydata.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            ser=StudentSerializer(stu)
            json_data=JSONRenderer().render(ser.data)
            return HttpResponse(json_data,content_type='application/json')

    stu=Student.objects.all()
    serializer=StudentSerializer(stu,many=True)
    json_data=JSONRenderer().render(ser.data)
    return HttpResponse(json_data,content_type='application/json')
