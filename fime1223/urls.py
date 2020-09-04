from django.urls import path
from .import views

from django.conf.urls import url
from . import views
from django.urls import include, path
urlpatterns = [
    path('', views.home, name='home'),
    path('registerpage/', views.registerpage, name='resisterpage'),
    path('addyourschool/', views.addyourschool, name='addyourschool'),
     # path('reg_sign/', views.reg_sign, name='reg_sign'),
    path('login/', views.login,name='login'),
    path('Basic_information', views.Basic_information, name='Basic_information'),

    path('admission_informationvarn', views.admission_informationvarn, name='admission_informationvarn'),
    path('Facility', views.Facility, name='Facility'),
    # path('infrastructure_and_campus', views.infrastructure_and_campus, name='infrastructure_and_campus'),
    path('Sports_curricular', views.Sports_curricular, name='Sports_curricular'),
    path('Awards_Recognition', views.Awards_Recognition, name='Awards_Recognition'),
    path('fee_Scructure', views.fee_Scructure, name='fee_Scructure'),
    path('Hostel_Accomodation', views.Hostel_Accomodation, name='Hostel_Accomodation'),
    path('create_myClass', views.create_myClass, name='create_myClass'),
    # path('sports_and_curr', views.sports_and_curr, name='sports_and_curr'),

    path('Admission_document_eligibility', views.Admission_document_eligibility, name='Admission_document_eligibility'),
    path('logout/', views.logout,name='logout'),
    path('dashboard/', views.dashboard,name='dashboard'),
    path('collages/', views.collages,name='collages'),
    path(r'^register/$', views.register,name='register'),

    # path(r'^register/$', views.user_register, name='user_register')
    url(r'^register/$', views.user_register, name='user_register'),
]



