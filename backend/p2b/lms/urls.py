from django.urls import path
from lms.views import *
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('courses/', CourseList.as_view(), name='courses'),
    path('courses/create', CourseCreate.as_view(), name='create-course'),
    path('courses/<str:pk>/update', views.updateCourse, name='update-course'),
    path('courses/<str:pk>/delete', views.deleteCourse, name='delete-course'),
    path('courses/<str:pk>/', views.getCourse, name='course'),
]