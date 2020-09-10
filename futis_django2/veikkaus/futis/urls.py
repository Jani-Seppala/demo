from django.urls import path

from . import views

app_name = 'futis'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('veikkaukset/', views.veikkaukset, name='veikkaus'),
    path('pistetilanne/', views.pistetilanne, name='pistetilanne'),
    path('veikkaus/<int:pk>/', views.veikkaukset, name='veikkaus'),
    path('luo_veikkaus/', views.luo_veikkaus, name='luo_veikkaus'),
    path('luo_veikkaus_beta/', views.luo_veikkaus_beta, name='luo_veikkaus_beta'),
]
