from django.urls import path
from . import views

urlpatterns = [
    path('api/student', views.GetData),
    path('api/skills', views.GetSkills),
    path('api/experience', views.Experiences),
    path('api/project', views.Projects),
]
