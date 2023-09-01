from django.urls import path,include 
from rest_framework import routers


from apps.todo.api.viewsets import TaskViewSet
"""O router criara o endpoint"""
routers = routers.DefaultRouter()

routers.register("", TaskViewSet, basename="task")

urlpatterns =[
    path('', include(routers.urls))

    
]