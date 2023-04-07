from django.urls import path
from . import views
from lms.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('courses/', CourseList.as_view(), name='courses'),
    path('courses/create', CourseCreate.as_view(), name='create-course'),
    path('courses/<int:id>/', CourseRetrieveUpdateDelete.as_view(), name='delete_course'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)