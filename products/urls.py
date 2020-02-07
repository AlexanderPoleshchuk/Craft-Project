from django.conf.urls import url, include
from django.contrib import admin
from products import views
from django.urls import path

urlpatterns = [
    path('panel', views.panel_view),
    url(r'^product/(?P<product_id>\w+)/$', views.product, name='product')
]