
from django.contrib import admin
from django.urls import path
from sim3_api.views import sim3_list

urlpatterns = [
    path('list/', sim3_list)
]
