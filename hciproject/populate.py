import os
from django.core.wsgi import get_wsgi_application


questions = [
    {
        "answers": {
            "correct": "University of Glasgow",
            "incorrect": ["Kelvingrove Art Gallery", "Oran Mor", "People's Palace"],
        },
        "question": "Identify the building pictured.",
        "image": "pop_img/glasgow.jpg",
        "category": "L",
    }
]

def add_question(answers, question, image, category):
    q = Question.objects.get_or_create(
        answers=answers,
        question=question,
        image=image,
        category=category
    )[0]
    return q

def add_profile(user, picture, score, location):
    p = UserProfile.objects.get_or_create(
        user=user,
        picture=picture,
        score=score,
        location=location
    )[0]
    return p

def populate():
    Question.objects.all().delete()
    UserProfile.objects.all().delete()
    admin = User.objects.get(username="admin")
    #add_profile(admin, "profile_images/glasgow.jpg",

    for question in questions:
        add_question(
            question["answers"],
            question["question"],
            question["image"],
            question["category"]
        )



if __name__ == '__main__':
    print "Starting population script..."
    os.environ['DJANGO_SETTINGS_MODULE'] = 'hciproject.settings'
    application = get_wsgi_application()
    from django.contrib.auth.models import User
    from hciproject.models import Question, UserProfile
    populate()
    print "Done"
