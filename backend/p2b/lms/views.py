from re import search
from urllib import request
from xml.dom import ValidationErr
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from lms.models import Course
from lms.serializers import CourseSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.

#get all courses
class CourseList(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields = ['title', 'description']

#create a course
class CourseCreate(CreateAPIView):
    serializer_class = CourseSerializer

    def create(self, request, *args, **kwargs):
        try:
            cost = request.data.get('cost')
            if cost is not None and float(cost) <= 0.00:
                raise ValidationErr({'cost': "Must be above KES0.00"})
        except ValueError:
            raise ValidationErr({'cost': 'A valid number is required'})
        return super().create(request, *args, **kwargs)

class CourseRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    lookup_field = 'id'
    serializer_class = CourseSerializer
    #delete and clearing the cache
    def delete(self, request, *args, **kwargs):
        course_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('course_data_{}'.format(course_id))
        return response
    #update note
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            course = response.data
            #stores data in the cache
            cache.set('course_data_{}'.format(course['id']),
            {
                'title' :course['title'],
                'description' : course['description'],
                'cost' : course['cost'],
                'photo' : course['photo'],
                'video' : course['video']
            })
        return response


