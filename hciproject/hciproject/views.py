from django.shortcuts import render
from django.http import HttpResponse
from models import UserProfile
from forms import UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime
from django.shortcuts import redirect
from django.contrib.auth.models import User



def index(request):
    context_dict = {"string": "hello world"}
    response = render(request,'index.html', context_dict)
    return response

def quiz(request):
    response = render(request, 'quiz.html')
    return response



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def register_profile(request):
    	context_dict = {}

	if not request.method == 'POST':
		context_dict['profile_form'] = UserProfileForm(request.GET)
		return render(request, 'registration/profile_registration.html', context_dict)

	profile_form = UserProfileForm(request.POST)
	user = User.objects.get(id=request.user.id)

	if profile_form.is_valid():
		try: # Does a profile exist?
			profile = UserProfile.objects.get(user=user)
		except: # No?
			profile = profile_form.save(commit=False)
			profile.user = user
		if 'website' in request.POST and request.POST['website']:
			profile.website = request.POST['website']
		if 'picture' in request.FILES and request.FILES.get('picture'):
			profile.picture = request.FILES.get('picture')
		profile.save()

	return render(request, 'index.html', context_dict)

@login_required
def profile(request):
    context_dict = {}
    user = User.objects.get(id=request.user.id)
    print user.username
    try:
        profile = UserProfile.objects.get(user=user)
    except:
        profile = None
        print "NO PROFILE"

    context_dict['userprofile'] = profile

    return render(request, 'profile.html', context_dict)
