from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'portfolio/home.html')
def projects_view(request):
    return render(request, 'portfolio/projects.html')
def skills_view(request):
    return render(request, 'portfolio/skills.html')