from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    technology = models.CharField(max_length=200)
    project_description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    def __str__(self):
        return self.title()
    
class Certification(models.Model):
    title = models.CharField(max_length=100)
    issuing_organization = models.CharField(max_length=100)
    date_issued = models.DateField()
    certificate_link = models.URLField(blank=True, null=True)
    certification_image = models.ImageField(upload_to='certifications/', blank=True, null=True)
    
    def __str__(self):
        return self.title
    


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='services/', blank=True, null=True)

    def __str__(self):
        return self.title
    
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()


    def __str__(self):
        return f"Message from {self.name}"
    
