from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden, HttpResponse
from django.views.decorators.http import require_POST
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Project, Certification, Service, Contact
from .serializers import ProjectSerializer, CertificationSerializer, ServiceSerializer, ContactSerializer
from .forms import ServiceForm, ProjectForm, ContactForm

# ViewSets for the API endpoints
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'start_date']

class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fileds = ['name','email','subject','message']

# Regular Django views for the front-end pages
def index(request):
    return render(request, 'portapp/index.html')

def aboutus(request):
    return render(request, 'portapp/aboutus.html')

def projects(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
        else:
            # Re-render the page with the form and its errors if invalid
            projects_list = Project.objects.all()
            return render(request, 'portapp/projects.html', {'projects': projects_list, 'form': form})
    else:
        # For a GET request, create an empty form instance
        form = ProjectForm()

    projects_list = Project.objects.all()
    
    # Pass both the projects list and the form to the template
    context = {
        'projects': projects_list,
        'form': form,
    }
    
    return render(request, 'portapp/projects.html', context)
# def projects(request):
#     projects_list = Project.objects.all().order_by('-start_date') # Optional: order by date
#     return render(request, 'projects.html', {'projects': projects_list})

# def add_project(request):
#     if request.method == 'POST':
#         form = ProjectForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('projects')
#     else:
#         form = ProjectForm()
    
#     return render(request, 'add_project.html', {'form': form})




def certifications(request):
    certs = Certification.objects.all()
    return render(request, 'portapp/certifications.html', {'certifications': certs})

@require_POST
def add_certification(request):
    title = request.POST.get('title')
    issuing_organization = request.POST.get('issuing_organization')
    date_issued = request.POST.get('date_issued')
    certificate_link = request.POST.get('certificate_link')
    certification_image = request.FILES.get('certification_image')
    
    if title and issuing_organization and date_issued:
        Certification.objects.create(
            title=title,
            issuing_organization=issuing_organization,
            date_issued=date_issued,
            certificate_link=certificate_link,
            certification_image=certification_image
        )
        return redirect('certifications')
    return HttpResponse("Invalid form submission.", status=400)


def services(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('services')
    else:
        form = ServiceForm()

    services_list = Service.objects.all()
    return render(request, 'portapp/services.html', {'services': services_list, 'form': form})



# def services(request):
#     services_list = Service.objects.all()
#     return render(request, 'portapp/services.html', {'services': services_list})

# @require_POST
# def add_service(request):
#     title = request.POST.get('title')
#     description = request.POST.get('description') # This is the change
#     image = request.FILES.get('image')
    
#     if title and description: # Image is optional now, so checking for it is unnecessary
#         Service.objects.create(
#             title=title,
#             description=description,
#             image=image
#         )
#         return redirect('services')
#     return HttpResponse("Invalid form submission.", status=400)

def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts')
    else:
        form = ContactForm()
    return render(request, 'portapp/contactus.html', {'form': form})


# Define a secret key to access the messages page
# This should be a strong, random string in a real application,
# ideally stored in environment variables.
SECRET_KEY = "my-super-secret-key-12345"

def contactus(request):
    """
    Handles the contact form submission.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the secure messages page with the secret key
            # Changed the redirect to a hardcoded URL to avoid the 404 error
            return redirect(f'/contacts/?key={SECRET_KEY}')
    else:
        form = ContactForm()
    return render(request, 'portapp/contactus.html', {'form': form})

def view_contacts_secret(request):
    """
    Displays all submitted contact messages.
    This page is protected by a secret key.
    """
    # Check if the provided key matches the secret key
    if request.GET.get('key') == SECRET_KEY:
        # Removed .order_by('-created_at') to fix the FieldError
        contacts_list = Contact.objects.all()
        return render(request, 'portapp/contacts.html', {'contacts': contacts_list})
    else:
        # Return a 403 Forbidden error if the key is incorrect or missing
        return HttpResponseForbidden("Access Denied.")

# You will need to add the URL pattern for view_contacts_secret in your urls.py
# For example: path('contacts/', views.view_contacts_secret, name='contacts'),
