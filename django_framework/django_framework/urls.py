"""django_framework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('add_shop', views.add_shop, name='add_shop'),
    path('clear_shops_table', views.clear_shops_table, name='clear_shops_table'),
    path('external_api_call', views.external_api_call, name='external_api_call'),
    path('serialize_json', views.serialize_json, name='serialize_json'),
    path('clear_students_table', views.clear_students_table, name='clear_students_table'),
]
