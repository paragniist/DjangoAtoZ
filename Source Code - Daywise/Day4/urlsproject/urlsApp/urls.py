from django.urls import path
from urlsApp import views


urlpatterns=[
    path('HydJobs/', views.hydjobs),
    path('PuneJobs/', views.punejobs),
    path('BangloreJobs/', views.banglorejobs),
    path('ChennaiJobs/', views.chennaijobs),
] 