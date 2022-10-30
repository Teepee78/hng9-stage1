from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.generics import ListAPIView
from .serializers import MyInfoSerializer
from .models import MyInfo
import json

# Create your views here.
def MyInfoView_func(request):
    # info = MyInfo.objects.all()
    # serializer = MyInfoSerializer(info, many=True)
    json_set = {"slackUsername": "Lase", "backend": True, "age": 23, "bio": "A Backend Engineer based in Lagos, Nigeria."}
    return JsonResponse(json_set, safe=False)

class MyInfoView(ListAPIView):
    queryset = MyInfo.objects.all()
    serializer_class = MyInfoSerializer
