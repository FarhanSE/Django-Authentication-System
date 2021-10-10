from django.urls import path
from . import views

urlpatterns = [
    path('', views.userLog, name='login'),
    path('register/', views.userReg, name='register'),
    path('welcome/', views.welcome, name='welcome'),
    path('logout', views.userOut, name='logout')
]