from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# Create your views here.
def home(request):
    context = {}
    templates = 'home.html'
    return render(request, templates, context)

def about(request):
    context = {}
    templates = 'about.html'
    return render(request, templates, context)

@login_required
def userProfile(request):
    user = request.user
    context = {'user':user}
    templates = 'profile.html'
    return render(request, templates, context)
