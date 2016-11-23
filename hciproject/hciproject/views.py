from django.shortcuts import render
from django.http import HttpResponse
from models import UserProfile, Question
from forms import UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime
from django.shortcuts import redirect
from django.contrib.auth.models import User
import random
import json
from django.core.serializers.json import DjangoJSONEncoder

class MyEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__

def index(request):
    context = {"string": "hello world"}
    response = render(request,'index.html', context)
    return response

def quiz(request):
    context = {}
    num_ques = len(Question.objects.all())
    question_list = []
    while len(question_list) < 3:
        question = random.randint(0, num_ques-1)
        if question not in question_list:
            question_list.append(question)
    questions = []
    for id in question_list:
        question = Question.objects.get(id=id)
        questions.append(question)
    print questions
    context["questions"] = json.dumps(questions, cls=MyEncoder)
    response = render(request, 'quiz.html', context)
    return response


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def register_profile(request):
    context = {}
    if not request.method == 'POST':
		context['profile_form'] = UserProfileForm(request.GET)
		return render(request, 'registration/profile_registration.html', context)
    else:
    	profile_form = UserProfileForm(request.POST)
    	user = User.objects.get(id=request.user.id)
    	if profile_form.is_valid():
    		try: # Does a profile exist?
    			profile = UserProfile.objects.get(user=user)
    		except: # No?
    			profile = profile_form.save(commit=False)
    			profile.user = user
    		if 'picture' in request.FILES and request.FILES.get('picture'):
    			profile.picture = request.FILES.get('picture')
    		profile.save()
    	return render(request, 'index.html', context)

@login_required
def profile(request):
    context = {}
    user = User.objects.get(id=request.user.id)
    print user.username
    try:
        profile = UserProfile.objects.get(user=user)
    except:
        profile = None
        print "NO PROFILE"

    context['userprofile'] = profile

    return render(request, 'profile.html', context)
