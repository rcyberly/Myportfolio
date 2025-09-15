# portapp/serializers.py

from rest_framework import serializers
from .models import Project, Certification, Service, Contact

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'start_date', 'end_date', 'technology', 'project_description', 'video_file']

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        # Corrected this line
        model = Certification 
        fields = ['id', 'title', 'issuing_organization', 'date_issued', 'certificate_link', 'certification_image']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title', 'service_description', 'service_image']
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email','phone','subject','message']