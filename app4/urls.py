from . import views
from django.urls import path
from.views import *


urlpatterns=[
    path('dog/',views.SecondLearningRestAPI.as_view(),name='dog'),
    path('',views.getAPI.as_view(),name='getAPI'),

]