import os
from django.core.wsgi import get_wsgi_application


def total_score(score):
    total = 0
    for header in score:
        total += score[header]
    return total

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

    User Profile template

{
    "username": "",
    "email": "@email.com",
    "password": "",
    "picture": "profile_images/",
    "score": {
        "L": , "T": , "H": , "P": , "B":
    },
    "location" : ""
}

"""

profiles = [
    {
        "username": "John",
        "email": "john@email.com",
        "password": "johnpassword",
        "picture": "profile_images/user.jpg",
        "score": {
            "L": 0, "T": 0, "H": 0, "P": 0, "B": 0
        },
        "location" : "W"
    },
    {
        "username": "Harry",
        "email": "harry@email.com",
        "password": "harrypassword",
        "picture": "profile_images/user.jpg",
        "score": {
            "L": 100, "T": 100, "H": 100, "P": 100, "B": 100
        },
        "location" : "W"
    },
    {
        "username": "George",
        "email": "george@email.com",
        "password": "georgepassword",
        "picture": "profile_images/user.jpg",
        "score": {
            "L": 200, "T": 200, "H": 200, "P": 200, "B": 200
        },
        "location" : "W"
    },
    {
        "username": "Judy",
        "email": "judy@email.com",
        "password": "judypassword",
        "picture": "profile_images/user.jpg",
        "score": {
            "L": 0, "T": 0, "H": 0, "P": 0, "B": 0
        },
        "location" : "W"
    },
    {
        "username": "Chris",
        "email": "chris@email.com",
        "password": "chrispassword",
        "picture": "profile_images/user.jpg",
        "score": {
            "L": 300, "T": 300, "H": 300, "P": 300, "B": 300
        },
        "location" : "W"
    },
    {
        "username": "Outsider",
        "email": "outsider@email.com",
        "password": "outsiderpassword",
        "picture": "profile_images/user.jpg",
        "score": {
            "L": 300, "T": 300, "H": 300, "P": 300, "B": 400
        },
        "location" : "N"
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
        "learn_text": "James McAvoy was born in Glasgow in 1979, and has gone on to achieve Hollywood fame."
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
    {
        "answers": {
            "correct": "George Square",
            "incorrect": ["Glasgow Green", "Cathedral Square", "Queen's Park"],
        },
        "question": "Which Glasgow location was used during filming of World War Z?",
        "image": "question_images/018.jpg",
        "category": "L",
        "learn_text": "The movie producers loved the look of George Square and filmed some scenes there in 2011."
    },
    {
        "answers": {
            "correct": "Kelvingrove Museum",
            "incorrect": ["Glasgow School of Art", "The Lighthouse", "Scotland Street School Museum"],
        },
        "question": "Which of these buildings was not designed by Charles Rennie Mackintosh?",
        "image": "question_images/019.jpg",
        "category": "P",
        "learn_text": "Kelvingrove was designed by Sir John W. Simpson and E.J. Milner Allen and opened in 1901."
    },
    {
        "answers": {
            "correct": "1957",
            "incorrect": ["1947", "1967", "1977"],
        },
        "question": "In which year did construction of the Clyde Tunnel begin?",
        "image": "question_images/020.jpg",
        "category": "H",
        "learn_text": "The Clyde Tunnel is a crossing underneath the River Clyde which connects Whiteinch and Govan."
    },
    {
        "answers": {
            "correct": "Clockwork orange",
            "incorrect": ["Orange circle", "Underground", "Metro"],
        },
        "question": "Which of these is a nickname for the Glasgow subway system?",
        "image": "question_images/021.jpg",
        "category": "T",
        "learn_text": "Clockwork Orange is the nickname due to vibrant orange livery and the trains run clockwise, or anti-clockwise in a circle."
    },
    {
        "answers": {
            "correct": "Jim Watt",
            "incorrect": ["Tancy Lee", "Walter McGowan", "Ken Buchanan"],
        },
        "question": "Name this Glasgow boxer",
        "image": "question_images/022.jpg",
        "category": "P",
        "learn_text": "Pictured is Jim Watt, the Glasweigan boxer who became world champion in the lightweight division in 1979."
    },
    {
        "answers": {
            "correct": "Singer",
            "incorrect": ["Brother", "Frister & Rossman", "Janome"],
        },
        "question": "Which of these is a famous sewing machine manufactured in Glasgow?",
        "image": "question_images/023.jpeg",
        "category": "T",
        "learn_text": "In 1867 the Singer Corporation decided that UK demand was high enough to justify a local factory. Glasgow was chosen as the factory location."
    },
    {
        "answers": {
            "correct": "Renfrew Street",
            "incorrect": ["Sauchiehall Street", "Bell Street", "Hope Street"],
        },
        "question": "On what Glasgow street would you find the Glasgow School of Art?",
        "image": "question_images/024.jpg",
        "category": "L",
        "learn_text": "The address of the Glasgow School of Art is 167 Renfrew Street."
    },
    {
        "answers": {
            "correct": "12th",
            "incorrect": ["11th", "13th", "14th"],
        },
        "question": "In which century was Glasgow Cathedral built?",
        "image": "question_images/025.jpeg",
        "category": "H",
        "learn_text": "The cathedral was built in the early 12th century and is a superb example of Scottish Gothic architecture."
    },
    {
        "answers": {
            "correct": "Glasgow Botanic Gardens",
            "incorrect": ["Kelvingrove Park", "Glasgow Green", "Queen's Park"],
        },
        "question": "Where would you find the Kibble Palace?",
        "image": "question_images/026.jpg",
        "category": "L",
        "learn_text": "The Kibble Palace is the most notable glasshouse in the botanic gardens. It is a 19th century wrought-iron framed structure."
    },
    {
        "answers": {
            "correct": "Forth & Clyde Canal",
            "incorrect": ["Forth & Kelvin Canal", "Clyde Canal", "Forth Canal"],
        },
        "question": "What is the name of the canal that links Glasgow and Grangemouth?",
        "image": "question_images/027.jpg",
        "category": "T",
        "learn_text": "The Forth & Clyde Canal opened in 1790 and runs from the River Carron at Grangemouth to the River Clyde at Bowling."
    },
    {
        "answers": {
            "correct": "A bomb went off",
            "incorrect": ["The monarch visited", "It was moved", "A new plant was discovered"],
        },
        "question": "What happened at the Kibble Palace in 1914?",
        "image": "question_images/026.jpg",
        "category": "H",
        "learn_text": "The bomb caused damage to 27 panes of glass and numerous plants."
    },
    {
        "answers": {
            "correct": "Robbie Coltrane",
            "incorrect": ["Stanley Baxter", "Dayton Callie", "Tommy Flanagan"],
        },
        "question": "Name this famous Glasweigan actor",
        "image": "question_images/028.jpg",
        "category": "P",
        "learn_text": "Robbie Coltrane is best known for his roles as Rubeus Hagrid in Harry Potter and Valentin Dmitrovich Zukovsky in GoldenEye."
    },
    {
        "answers": {
            "correct": "Saint Mungo",
            "incorrect": ["Saint Andrew", "Saint Blane", "Saint Regulus"],
        },
        "question": "Which saint is thought to be the founder of Glasgow?",
        "image": "question_images/010.jpg",
        "category": "H",
        "learn_text": "Glasgow was founded by the Christian missionary Saint Mungo in the 6th century. He established a church where the present Glasgow Cathedral stands."
    },
    {
        "answers": {
            "correct": "598,830",
            "incorrect": ["548,830", "648,830", "498,830"],
        },
        "question": "What is the current estimate of the population of Glasgow?",
        "image": "question_images/029.jpg",
        "category": "T",
        "learn_text": "The estimated population of Glasgow in 2011 was 598,830, making Glasgow the 3rd largest city in the UK after London and Birmingham."
    },
    {
        "answers": {
            "correct": "Scottish Football Museum",
            "incorrect": ["Kelvingrove Museum", "People's Palace", "Huntarian Museum"],
        },
        "question": "Which of these Glasgow museums has the oldest football in the world?",
        "image": "question_images/030.jpg",
        "category": "L",
        "learn_text": "The football was found in the Queen's Chamber at Stirling Castle during renovation work and is thought to be 1 of 4 ordered for King James IV in the 1490s."
    },
    {
        "answers": {
            "correct": "Christopher Brookmyre",
            "incorrect": ["James Kelman", "Alasdair Gray", "Archie Hind"],
        },
        "question": "Name this Glasweigan author",
        "image": "question_images/031.jpg",
        "category": "P",
        "learn_text": "Christopher Brookmyre is a novelist whose novels mix comedy, politics, social comment and action with a strong narrative."
    },
    {
        "answers": {
            "correct": "Martin Creed",
            "incorrect": ["Douglas Gordon", "Jim Lambie", "Nathan Coley"],
        },
        "question": "Name this Glasweigan artist",
        "image": "question_images/032.jpg",
        "category": "P",
        "learn_text": "Martin Creed won the Turner Prize in 2001 for Work No. 227: The lights going on and off."
    },
    {
        "answers": {
            "correct": "Glasgow Green",
            "incorrect": ["Kelvingrove Park", "Botanic Gardens", "Queen's Park"],
        },
        "question": "Which of these parks is the oldest in the city",
        "image": "question_images/033.jpg",
        "category": "H",
        "learn_text": "Glasgow Green was established in the 15th century, making it the oldest park in the city."
    },
    {
        "answers": {
            "correct": "Tennents",
            "incorrect": ["Innis & Gunn", "Orkney", "Belhaven"],
        },
        "question": "Which Scottish beer companies has a brewery on Duke Street?",
        "image": "question_images/034.jpg",
        "category": "T",
        "learn_text": "Tennents lager is produced in the Wellpark Brewery on Duke Street which was established in 1740."
    },
    {
        "answers": {
            "correct": "Sauchiehall Street",
            "incorrect": ["Argyle Street", "Byres Road", "Jamaica Street"],
        },
        "question": "On which Glasgow street would you find the Royal Concert Hall",
        "image": "question_images/035.jpg",
        "category": "L",
        "learn_text": "The Royal Concert Hall opened in 1990. It's address is Buchanan Galleries, 2 Sauchiehall Street."
    },
    {
        "answers": {
            "correct": "Sauchiehall Street",
            "incorrect": ["Argyle Street", "Byres Road", "Jamaica Street"],
        },
        "question": "On which Glasgow street would you find the Royal Concert Hall",
        "image": "question_images/035.jpg",
        "category": "L",
        "learn_text": "The Royal Concert Hall opened in 1990. It's address is Buchanan Galleries, 2 Sauchiehall Street."
    },
    {
        "answers": {
            "correct": "Glasgow City Chambers",
            "incorrect": ["St. Vincent Street Church", "Holmwood House", "Walmer Cresent"],
        },
        "question": "Which one of these buildings wasn't designed by Alexander Thomson, a Glasweigan architect",
        "image": "question_images/036.jpg",
        "category": "P",
        "learn_text": "Glasgow City Chambers was designed by William Young and housed Glasgow Town Council from 1888 to 1895."
    },
    {
        "answers": {
            "correct": "Billy Connolly",
            "incorrect": ["Kevin Bridges", "Frankie Boyle", "Gregor Fisher"],
        },
        "question": "Which Glasweigan comedian is known as 'The Big Yin'?",
        "image": "question_images/029.jpg",
        "category": "T",
        "learn_text": "Billy Connolly was born in Anderston in 1942. He worked as a welder before becoming a comedian"
    },
    {
        "answers": {
            "correct": "1941",
            "incorrect": ["1939", "1943", "1945"],
        },
        "question": "In which year did the Clydebank Blitz take place?",
        "image": "question_images/037.jpg",
        "category": "H",
        "learn_text": "As a result of the raids on 13th and 14th March 1941, the town was largely destroyed and suffered the worst destruction and civilian loss of life in all of Scotland. 528 people died and many more were injured."
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

def add_profile(user, picture, score, total_score, location):
    p = UserProfile.objects.get_or_create(
        user=user,
        picture=picture,
        score=score,
        total_score=total_score,
        location=location
    )[0]
    return p

def populate():
    Question.objects.all().delete()
    UserProfile.objects.all().delete()
    User.objects.all().delete()
    for profile in profiles:
        user = User.objects.create_user(
            profile["username"],
            profile["email"],
            profile["password"]
        )
        add_profile(
            user,
            profile["picture"],
            profile["score"],
            total_score(profile["score"]),
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
