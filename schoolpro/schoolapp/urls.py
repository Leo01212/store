
from django.urls import path
from . import views
urlpatterns = [

    path('',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('forms/',views.student_form,name='student_form'),
    path('logout/', views.logout, name='logout'),
    path('success/', views.success, name='success')
]