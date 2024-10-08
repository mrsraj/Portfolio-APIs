from rest_framework import serializers
from .models import Student, StudentDetails,Skills,SkillsDetails,Experience

class StudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = ['id', 'universityname', 'collegename', 'branch', 'degree', 'passion'] 

class StudentSerializer(serializers.ModelSerializer):
    details = StudentDetailsSerializer(many=True, read_only=True)  

    class Meta:
        model = Student
        fields = ['id', 'name', 'details'] 
        
class SkillsDetailsSerializer(serializers.ModelSerializer):  # Inheriting from serializers.ModelSerializer
    class Meta:
        model = SkillsDetails
        fields = ['relatedskills']

class SkillsSerializer(serializers.ModelSerializer):
    topic = SkillsDetailsSerializer(many=True, read_only=True, source='skills_details')  # Matching related_name

    class Meta:
        model = Skills
        fields = ['skills', 'topic']  # Include SkillsDeta in the fields
        
class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'


    
# from rest_framework import serializers
# from .models import Student, StudentDetails

# class StudentDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StudentDetails
#         fields = ['id', 'universityname', 'collegename', 'branch', 'degree', 'passion']

# class StudentSerializer(serializers.ModelSerializer):
#     details = serializers.SerializerMethodField()  # Use SerializerMethodField to customize the output

#     class Meta:
#         model = Student
#         fields = ['id', 'name', 'details']

#     def get_details(self, obj):
#         # Get the first related StudentDetails instance, if it exists
#         details = obj.details.first()
#         return StudentDetailsSerializer(details).data if details else None