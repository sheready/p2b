from re import search
from xml.dom import ValidationErr
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from lms.models import Course
from lms.serializers import CourseSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView

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

class CourseDelete(DestroyAPIView):
    queryset = Course.objects.all()
    lookup_field = 'id'
    #clearing the cache
    def delete(self, request, *args, **kwargs):
        course_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('course_data_{}'.format(course_id))
        return response

@api_view(['GET'])
def getCourse(request, pk):
    courses = Course.objects.get(id=pk)
    serializer = CourseSerializer(courses, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createCourse(request):
    data = request.data
    course = Course.objects.create(
        title = data['title'],
        description = data['description'],
        cost = data['cost']
    )
    serializer = CourseSerializer(course, many= False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateCourse(request, pk):
    data = request.data
    course = Course.objects.get(id=pk)
    serializer = CourseSerializer(instance=course, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteCourse(request, pk):
    course = Course.objects.get(id=pk)
    course.delete()
    return Response('Course has been deleted')
