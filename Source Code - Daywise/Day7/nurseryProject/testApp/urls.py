from django.urls import path
from testApp import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('date/', views.dateinfo),
]

