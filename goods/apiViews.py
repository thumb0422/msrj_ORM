# -*- coding: utf-8 -*-
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def api_GetList(request):
    data = request.data
    data['status'] = 20000
    print(data)
    return JsonResponse(data=data,status=201)

