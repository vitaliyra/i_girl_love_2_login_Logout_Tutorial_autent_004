from django.contrib import admin
from django.urls import path
from i_girl_love_s import views
urlpatterns =[path('', views.index, name='home_sw'),
                        ]
