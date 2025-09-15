from django import forms

from .models import Project, Service, Contact

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        # You've corrected this line to match your model
        fields = ['title', 'start_date', 'end_date', 'technology', 'project_description', 'video_file']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        # Change 'service_description' to 'description'
        fields = ['title', 'description', 'image']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email','phone', 'subject', 'message',]