from rest_framework import serializers
from lms.models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','title', 'description', 'cost', 'photo','video']