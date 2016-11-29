from django.shortcuts import render, render_to_response
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
from django.template import RequestContext

class MyEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__

def index(request):
    profiles = UserProfile.objects.all().order_by('-total_score')
    context = {"profiles": profiles}
    response = render(request,'index.html', context)
    return response


def quiz(request):
    context = {}
    num_ques = len(Question.objects.all())
    question_list = []
    while len(question_list) < 10:
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
    profile = UserProfile.objects.get(user=user)
    profiles = UserProfile.objects.all().order_by('-total_score')
    local_profiles = profiles.filter(location=profile.location)
    location = profile.get_location_display()
    total_questions = 0
    for category in profile.number_of_questions:
        total_questions += profile.number_of_questions[category]
    context['questions_answered'] = total_questions
    context['location'] = location
    context['all_profiles'] = profiles
    context['local_profiles'] = local_profiles
    context['userprofile'] = profile
    context["userprofile_json"] = json.dumps(profile, cls=MyEncoder)
    return render(request, 'profile.html', context)


def total_score(score):
    total = 0
    for header in score:
        total += score[header]
    return total


def send_score(request):
    user = User.objects.get(id=request.user.id)
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        print request.POST
        L_score = request.POST.get('score[L]')
        H_score = request.POST.get('score[H]')
        P_score = request.POST.get('score[P]')
        T_score = request.POST.get('score[T]')
        B_score = request.POST.get('score[B]')
        current_score = profile.score
        current_score['L'] += int(L_score)
        current_score['H'] += int(H_score)
        current_score['P'] += int(P_score)
        current_score['T'] += int(T_score)
        current_score['B'] += int(B_score)
        profile.score = current_score
        profile.total_score = total_score(current_score)

        L_questions = request.POST.get('questions[L]')
        H_questions = request.POST.get('questions[H]')
        P_questions = request.POST.get('questions[P]')
        T_questions = request.POST.get('questions[T]')
        current_questions = profile.number_of_questions
        current_questions['L'] += int(L_questions)
        current_questions['H'] += int(H_questions)
        current_questions['P'] += int(P_questions)
        current_questions['T'] += int(T_questions)
        profile.number_of_questions = current_questions

        profile.quizes_played += 1

        profile.save()
        print profile.score
        response_data = {"post": "success"}
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"error": "failed"}),
            content_type="application/json"
        )
