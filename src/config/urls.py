from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from app.builder.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    url('',index,name='index'),
]
