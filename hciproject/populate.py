import os
from django.core.wsgi import get_wsgi_application


""" Question template

{
    "answers": {
        "correct": "",
        "incorrect": ["", "", ""],
    },
    "question": "",
    "image": "question_images/",
    "category": "",
    "learn_text": ""
}

"""
profiles = [
    {
        "picture": "profile_images/capture.jpg",
        "score": {
            "L": 200,
            "T": 120,
            "H": 40,
            "P": 90,
            "B":430
        },
        "location" : "W"
    }
]

questions = [
    {
        "answers": {
            "correct": "University of Glasgow",
            "incorrect": ["Kelvingrove Art Gallery", "Oran Mor", "People's Palace"],
        },
        "question": "Identify the building pictured.",
        "image": "question_images/002.jpg",
        "category": "L",
        "learn_text": "The University of Glasgow Main Building was completed in 1887."
    },
    {
        "answers": {
            "correct": "Peter Capaldi",
            "incorrect": ["Richard E. Grant", "James Nesbitt", "John Hannah"],
        },
        "question": "Identify this Glaswegian actor",
        "image": "question_images/001.jpg",
        "category": "P",
        "learn_text": "Peter Capaldi was born in Glasgow in 1958, and attended the Glasgow School of Art"
    },
    {
        "answers": {
            "correct": "James McAvoy",
            "incorrect": ["James D'Arcy", "Luke Evans", "Ewan McGregor"],
        },
        "question": "Identify this Glaswegian actor",
        "image": "question_images/004.jpg",
        "category": "P",
        "learn_text": "James McAvoy was born in Glasgow in 1979, and has gone on to acheive Hollywood fame."
    },
    {
        "answers": {
            "correct": "Charles Rennie Mackintosh",
            "incorrect": ["John James Burnet", "James Ross Gillespie", "John Kinross"],
        },
        "question": "Who designed the Glasgow School of Art, built between 1898 and 1906?",
        "image": "question_images/006.jpg",
        "category": "H",
        "learn_text": "Mackintosh also completed the Queen's Cross Church Project in Maryhill, which is now the Charles Rennie Mackintosh Society Headquarters"
    },
    {
        "answers": {
            "correct": "Maryhill",
            "incorrect": ["Partick", "Gorbels", "Easterhouse"],
        },
        "question": "In which part of Glasgow is the Scottish comedy 'Still Game' predominantly filmed?",
        "image": "question_images/005.jpg",
        "category": "T",
        "learn_text": "The fictional area of Craiglang was complied of many areas of Glasgow, though most filming fo exteriors was done in Maryhill."
    }
]

def add_question(answers, question, image, category, learn_text, id):
    q = Question.objects.get_or_create(
        id=id,
        answers=answers,
        question=question,
        image=image,
        category=category,
        learn_text=learn_text
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
    for profile in profiles:
        add_profile(
            admin,
            profile["picture"],
            profile["score"],
            profile["location"]
        )
    print "Questions: ", len(questions)
    i = 0
    for question in questions:
        add_question(
            question["answers"],
            question["question"],
            question["image"],
            question["category"],
            question["learn_text"],
            i
        )
        i += 1



if __name__ == '__main__':
    print "Starting population script..."
    os.environ['DJANGO_SETTINGS_MODULE'] = 'hciproject.settings'
    application = get_wsgi_application()
    from django.contrib.auth.models import User
    from hciproject.models import Question, UserProfile
    populate()
    print "Done"
