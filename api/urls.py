from django.urls import path
from .views import MyInfoView, MyInfoView_func


appname = 'api'
urlpatterns = [
    path('', MyInfoView_func, name='myinfoview'),
]
