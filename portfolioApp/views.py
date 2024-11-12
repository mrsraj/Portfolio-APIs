from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Import models and serializers
from .models import Student, Skills, Experience, Project
from .serializers import StudentSerializer, SkillsSerializer, ExperienceSerializer, ProjectSerializer

@api_view(['GET'])
def GetData(request):
    try:
        # Query all Student objects
        studentsData = Student.objects.all()
        
        # Serialize the data
        serialized_data = StudentSerializer(studentsData, many=True)
        
        # Return JSON response
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def GetSkills(request):
    try:
        # Query all Skills objects
        studentsSkills = Skills.objects.all()

        # Check if the queryset is empty
        if not studentsSkills.exists():
            return Response({"message": "No skills data found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Serialize the data if data exists
        serialized_data = SkillsSerializer(studentsSkills, many=True)
        
        # Return JSON response
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def Experiences(request):
    try:
        # Query all Experience objects
        studentExperience = Experience.objects.all()

        # Check if the queryset is empty
        if not studentExperience.exists():
            return Response({"message": "No experience data found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Serialize the data if data exists
        serialized_data = ExperienceSerializer(studentExperience, many=True)
        
        # Return JSON response
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def Projects(request):
    try:
        # Query all Project objects
        project = Project.objects.all()

        # Check if the queryset is empty
        if not project.exists():
            return Response({"message": "No project data found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Serialize the data if data exists
        serialized_data = ProjectSerializer(project, many=True)
        
        # Return JSON response
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)