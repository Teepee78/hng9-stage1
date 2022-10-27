from django.urls import path
from .views import MyInfoView


appname = 'api'
urlpatterns = [
    path('', MyInfoView.as_view(), name='myinfoview'),
]
