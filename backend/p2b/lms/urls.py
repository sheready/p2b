from django.urls import path
from . import views
from lms.views import *

urlpatterns = [
    path('courses/', CourseList.as_view(), name='courses'),
    path('courses/create', CourseCreate.as_view(), name='create-course'),
    path('courses/<int:id>/', CourseRetrieveUpdateDelete.as_view(), name='delete_course'),

]