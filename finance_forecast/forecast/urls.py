#manually created

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('program/list/', views.ProgramListView.as_view(), name= 'program_list'),
    path('program/detail/<int:pk>', views.ProgramDetailView.as_view(), name = 'program_detail'),
    path('program/forecast', views.CreateForecastView.as_view(), name = 'forecast_form'),
    path('program/forecast/<int:pk>/edit/', views.ForecastUpdateView.as_view(), name = 'forecast_edit'),
    path('forecast/list', views.ForecastListView.as_view(), name = 'forecast_list'),
    path('forecast/detail/<int:pk>',views.ForecastDetailView.as_view(), name = 'forecast_detail'),
    path('broken_page.html', views.broken_page, name = 'broken_page'),
    path('download', views.export_csv, name= 'export_csv')
]
