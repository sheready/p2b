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
from rest_framework.generics import ListAPIView, CreateAPIView

# Create your views here.

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/courses/',
            'method': 'GET',
            'title': None,
            'description': None,
            'cost': None,
            'details': 'Returns an array of courses'
        },
        {
            'Endpoint': '/courses/id',
            'method': 'GET',
            'title': None,
            'description': None,
            'cost': None,
            'details': 'Returns a course instance'
        },
        {
            'Endpoint': '/courses/create/',
            'method': 'POST',
            'title': {'title': ""},
            'description':{'description': ""},
            'cost': {'cost': ""},
            'details': 'Creates new course with data sent in post request'
        },
        {
            'Endpoint': '/courses/id/update/',
            'method': 'PUT',
            'title': {'title': ""},
            'description':{'description': ""},
            'cost': {'cost': ""},
            'details': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/courses/id/delete/',
            'method': 'DELETE',
            'title': {'title': ""},
            'description':{'description': ""},
            'cost': {'cost': ""},
            'details': 'Deletes and exiting note'
        },
    ]

    return Response(routes)

#get all courses
class CourseList(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields = ['title', 'description']


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
