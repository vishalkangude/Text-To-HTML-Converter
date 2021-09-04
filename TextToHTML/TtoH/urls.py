from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Home),
    path('Convert',views.Convert),
    path('Download', views.download_file),
    path('Copy', views.Copy)
]
