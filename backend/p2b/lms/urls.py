from django.urls import path
from . import views
from lms.views import *

urlpatterns = [
    path('courses/', CourseList.as_view(), name='courses'),
    path('courses/create', CourseCreate.as_view(), name='create-course'),
    path('courses/<int:id>/delete', CourseDelete.as_view(), name='delete_course'),
    path('courses/<str:pk>/update', views.updateCourse, name='update-course'),
    path('courses/<str:pk>/delete', views.deleteCourse, name='delete-course'),
    path('courses/<str:pk>/', views.getCourse, name='course'),
]