from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#import models and serializers
from .models import Student,Skills,Experience
from .serializers import StudentSerializer,SkillsSerializer,ExperienceSerializer

@api_view(['GET'])
def GetData(request):
    # Query all Student objects
    studentsData = Student.objects.all()
    
    # Serialize the data
    serialized_data = StudentSerializer(studentsData, many=True)
    
    # Return JSON response
    return Response(serialized_data.data)

@api_view(['GET'])
def GetSkills(request):
    # Query all Student objects
    studentsSkills = Skills.objects.all()

    # Check if the queryset is empty
    if not studentsSkills.exists():
        return Response({"message": "No skills data found"}, status=status.HTTP_404_NOT_FOUND)
    
    # Serialize the data if data exists
    serialized_data = SkillsSerializer(studentsSkills, many=True)
    
    # Return JSON response
    return Response(serialized_data.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def Experiences(request):
    # Query all Student objects
    studentExperience = Experience.objects.all()

    # Check if the queryset is empty
    if not studentExperience.exists():
        return Response({"message": "No skills data found"}, status=status.HTTP_404_NOT_FOUND)
    
    # Serialize the data if data exists
    serialized_data = ExperienceSerializer(studentExperience, many=True)
    
    # Return JSON response
    return Response(serialized_data.data, status=status.HTTP_200_OK)