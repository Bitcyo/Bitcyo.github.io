from django.shortcuts import render
from django.http import JsonResponse
from portafolio import models
from pathlib import Path
from django.conf import settings

# Create your views here.

def index(request):
    archivo = models.FilePDF.objects.first()
    file_name = archivo.file.name if archivo else ''
    skills = models.Skill.objects.all()
    interests = models.Interest.objects.all()
    
    
    presentations_sections = models.Presentation.objects.all()
    index_path = Path(settings.BASE_DIR) / 'index.html'

    return render(request, str(index_path), {'file_name': file_name, 'presentations_sections': presentations_sections, 'skills': skills, 'interests': interests})


