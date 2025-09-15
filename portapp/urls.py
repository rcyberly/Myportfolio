# portapp/urls.py

from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
# Make sure all viewsets are imported
from django.conf import settings
from django.conf.urls.static import static
from .views import ProjectViewSet, CertificationViewSet, ServiceViewSet , ContactViewSet

router = DefaultRouter()
router.register('projects', ProjectViewSet, basename='project')
router.register('certifications', CertificationViewSet, basename='certifications')
router.register('services', ServiceViewSet, basename='service')
router.register('contactus', ContactViewSet, basename='contactus')

urlpatterns = [
# Manually defined paths for your pages and forms
    path('', views.index, name='index'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('projects/', views.projects, name='projects'),
    path('certifications/', views.certifications, name='certifications'),
    path('services/', views.services, name='services'),
    path('contactus/', views.contactus, name='contactus'),
    path('contacts/', views.view_contacts_secret, name='contacts'),
    # path('add-project/', views.add_project, name='add_project'),
    path('add-certification/', views.add_certification, name='add_certification'),
    # path('add-service/', views.add_service, name='add_service'),
    

    
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)