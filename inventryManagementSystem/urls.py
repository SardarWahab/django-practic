
from django.contrib import admin
from django.urls import path
from IMS.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
]
