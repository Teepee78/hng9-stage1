from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.generics import ListAPIView
from .serializers import MyInfoSerializer
from .models import MyInfo

# Create your views here.
def MyInfoView_func(request):
    info = MyInfo.objects.all()
    serializer = MyInfoSerializer(info, many=True)
    return JsonResponse(serializer.data, safe=False)

class MyInfoView(ListAPIView):
    queryset = MyInfo.objects.all()
    serializer_class = MyInfoSerializer
