# portfolio/views.py
from django.shortcuts import render
from .models import Profile, Education, Experience, Skill, Project, SocialLink


def home(request):
    try:
        profile = Profile.objects.first()
        social_links = SocialLink.objects.all()
        featured_projects = Project.objects.all().order_by('-date_created')[:3]
    except:
        # Handle case where models don't exist yet
        profile = None
        social_links = []
        featured_projects = []

    context = {
        'profile': profile,
        'social_links': social_links,
        'featured_projects': featured_projects,
        'active_tab': 'home'
    }
    return render(request, 'portfolio/home.html', context)


def resume(request):
    try:
        profile = Profile.objects.first()
        education = Education.objects.all().order_by('-year_start')
        experience = Experience.objects.all().order_by('-date_start')
        design_skills = Skill.objects.filter(skill_type='design')
        coding_skills = Skill.objects.filter(skill_type='coding')
        tool_skills = Skill.objects.filter(skill_type='tool')
    except:
        profile = None
        education = []
        experience = []
        design_skills = []
        coding_skills = []
        tool_skills = []

    context = {
        'profile': profile,
        'education': education,
        'experience': experience,
        'design_skills': design_skills,
        'coding_skills': coding_skills,
        'tool_skills': tool_skills,
        'active_tab': 'resume'
    }
    return render(request, 'portfolio/resume.html', context)  # Changed to resume.html


def portfolio(request):
    try:
        profile = Profile.objects.first()
        projects = Project.objects.all().order_by('-date_created')
        categories = Project.objects.values_list('category', flat=True).distinct()
    except:
        profile = None
        projects = []
        categories = []

    context = {
        'profile': profile,
        'projects': projects,
        'categories': categories,
        'active_tab': 'portfolio'
    }
    # Updated template name here
    return render(request, 'portfolio/portfolio_list.html', context)


from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile


def download_resume(request):
    # Get the same data as in your resume view
    profile = Profile.objects.first()
    education = Education.objects.all().order_by('-year_start')
    experience = Experience.objects.all().order_by('-date_start')
    design_skills = Skill.objects.filter(skill_type='design')
    coding_skills = Skill.objects.filter(skill_type='coding')
    tool_skills = Skill.objects.filter(skill_type='tool')

    # Render the template to string
    html_string = render_to_string('portfolio/resume_pdf.html', {
        'profile': profile,
        'education': education,
        'experience': experience,
        'design_skills': design_skills,
        'coding_skills': coding_skills,
        'tool_skills': tool_skills,
    })

    # Create PDF
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    result = html.write_pdf()

    # Generate response
    response = HttpResponse(result, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    return response