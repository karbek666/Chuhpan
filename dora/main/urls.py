from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index,name="boot"),
    path('reg/', views.register, name='reg'),
    path('qwerty/', views.create, name="create_form"),
    path('logout1/', views.logout, name='logout1'),
    path('login/', views.user_login, name='login')

    ]