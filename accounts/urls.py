from django.urls import path
from . import views
# create urls
urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('customer/', views.customer),
]