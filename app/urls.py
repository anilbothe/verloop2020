from django.contrib import admin
from django.urls import path
from app import views

app_name = 'main'

urlpatterns = [
    # path('', views.index, name="home"),    
    path('', views.GoodreadsAPIClient.as_view(), name="goods_reads"),
]
