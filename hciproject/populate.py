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
            "incorrect": ["Partick", "Gorbals", "Easterhouse"],
        },
        "question": "In which part of Glasgow is the Scottish comedy 'Still Game' predominantly filmed?",
        "image": "question_images/005.jpg",
        "category": "T",
        "learn_text": "The fictional area of Craiglang was complied of many areas of Glasgow, though most filming of exteriors took place in Maryhill."
    },
    {
        "answers": {
            "correct": "Gallery of Modern Art",
            "incorrect": ["Kelvingrove Art Gallery", "Transport Museum", "Glasgow City Chambers"],
        },
        "question": "Identify the building pictured.",
        "image": "question_images/007.jpg",
        "category": "L",
        "learn_text": "The GoMA is Scotland's most visited modern art gallery."
    },
    {
        "answers": {
            "correct": "1471",
            "incorrect": ["1371", "1671", "1571"],
        },
        "question": "When was Provand's Lordship (Glasgow's oldest house) built?",
        "image": "question_images/008.jpeg",
        "category": "H",
        "learn_text": "Provand's Lordship was built in 1471 as part of St. Nicholas's Hospital and is one of 4 medieval buildings to survive in Glasgow."
    },
    {
        "answers": {
            "correct": "5",
            "incorrect": ["3", "9", "14"],
        },
        "question": "How many Clyde built sailing ships are left afloat in the world?",
        "image": "question_images/009.jpg",
        "category": "T",
        "learn_text": "The SV Glenlee is one of them and can be seen at the Clyde Maritime Centre."
    },
    {
        "answers": {
            "correct": "Huntarian Art Gallery and Museum",
            "incorrect": ["Kelvingrove Art Gallery", "Scotland Street School Museum", "People's Palace"],
        },
        "question": "Which Glasgow museum became Scotland's first public museum in 1807",
        "image": "question_images/010.jpg",
        "category": "H",
        "learn_text": "The Huntarian is Scotland's oldest public museum and one of the leading university museums in the world."
    },
    {
        "answers": {
            "correct": "Donald Dewar",
            "incorrect": ["George Galloway", "Menzies Campbell", "Tommy Sheridan"],
        },
        "question": "Identify this Glaswegian Politician.",
        "image": "question_images/011.jpeg",
        "category": "P",
        "learn_text": "Donald Dewar was leader of the Scottish Labour Party in 1999 and was elected First Minister of Scotland in 2000. He died while in office."
    },
    {
        "answers": {
            "correct": "Joseph Black",
            "incorrect": ["Lord Kelvin", "Robert Napier", "James Watt"],
        },
        "question": "Identify this Glasgow University alumnus.",
        "image": "question_images/012.jpg",
        "category": "P",
        "learn_text": "Joseph Black attended the University of Glasgow for 4 years in 1746 and in 1757 was appointed Regius Professor of the Practice of Medicine at the university."
    },
    {
        "answers": {
            "correct": "176km",
            "incorrect": ["153km", "197km", "214km"],
        },
        "question": "How long is the River Clyde?",
        "image": "question_images/013.jpg",
        "category": "T",
        "learn_text": "The River Clyde is the 8th longest river in the United Kingdom and the 2nd longest in Scotland."
    },
    {
        "answers": {
            "correct": "1990",
            "incorrect": ["1988", "1992", "1994"],
        },
        "question": "In which year was Glasgow named European City of Culture?",
        "image": "question_images/014.jpg",
        "category": "H",
        "learn_text": "Glasgow is home to over 100 cultural and artistic organisations. The Scottish Ballet, Opera and Symphony Orchestra are all based here."
    },
    {
        "answers": {
            "correct": "Glasgow Science Centre",
            "incorrect": ["Riverside Museum", "Clyde Auditorium", "Tron Theatre"],
        },
        "question": "Identify this building.",
        "image": "question_images/015.jpg",
        "category": "L",
        "learn_text": "The Science Centre opened in 2001 and is a popular visitor attraction."
    },
    {
        "answers": {
            "correct": "Glasgow City Chambers",
            "incorrect": ["Glasgow Cathedrel", "Royal Infirmary", "Mitchell Library"],
        },
        "question": "Identify this building.",
        "image": "question_images/016.jpg",
        "category": "L",
        "learn_text": "The City Chambers has functioned as the headquarters of Glasgow City Council since 1996."
    },
     {
        "answers": {
            "correct": "Kelvingrove Park",
            "incorrect": ["Glasgow Botanic Gardens", "Glasgow Green", "Queen's Park"],
        },
        "question": "Which park does Glasgow University overlook?",
        "image": "question_images/017.jpeg",
        "category": "T",
        "learn_text": "Glasgow University is situated in the city's West End and is the 4th oldest university in the English speaking world."
    },
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
