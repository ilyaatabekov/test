from django.urls import path
from .import views

urlpatterns = [
    path('',views.index, name='home'),
    path('weak', views.weak, name='weak'),
    path('weak_1', views.weak_1, name='weak_1'),
    path('day_1', views.day1, name='day_1'),
    path('day_2', views.day2, name='day_2'),
    path('day_3', views.day3, name='day_3'),
    path('day_4', views.day4, name='day_4'),
    path('day_5', views.day5, name='day_5'),
    path('day_6', views.day6, name='day_6'),
    path('day_7', views.day7, name='day_7'),
    path('weak_2', views.weak_2, name='weak_2'),
    path('day_1_2', views.day1_2, name='day_1_2'),
    path('day_2_2', views.day2_2, name='day_2_2'),
    path('day_3_2', views.day3_2, name='day_3_2'),
    path('day_4_2', views.day4_2, name='day_4_2'),
    path('day_5_2', views.day5_2, name='day_5_2'),
    path('day_6_2', views.day6_2, name='day_6_2'),
    path('day_7_2', views.day7_2, name='day_7_2')
]