from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import MyInfoSerializer
from .models import MyInfo

# Create your views here.


class MyInfoView(ListAPIView):
    queryset = MyInfo.objects.all()
    serializer_class = MyInfoSerializer
