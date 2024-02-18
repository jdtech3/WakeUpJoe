from flask import Flask
from flask import request
import requests
from flask import render_template, make_response
from spellchecker import SpellChecker

current_state = '' # take post
spellchecker = SpellChecker(distance=2)

def parse_string(string, keywords):
    found_keywords = []

    for keyword in keywords:
        for word in string.split():
            check = spellchecker.candidates(word)
            check = set() if check is None else check
            check.add(word)
            for w in check:
                if keyword.upper() == w.upper():
                    found_keywords.append(keyword)

    # for keyword in keywords:
    #     if keyword.upper() or spellchecker.correction(keyword).upper() in string:
    #         found_keywords.append(keyword)

    if found_keywords:
        return found_keywords[-1]
    else:
        return ''


    # string = "This is a sample string"
    # keywords = ["sample", "string", "example"]

    # found_keywords = parse_string(string, keywords)
    # print(found_keywords)

API_URL = "https://api-inference.huggingface.co/models/ai-forever/T5-large-spell"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
    
output = query({
    "inputs": "The answer to the universe is",
})


app = Flask(__name__)

#   flask --app webserver3 run --host 0.0.0.0

@app.route('/')
def index():
    return render_template('html5up-astral/index.html')

@app.route('/section')
def section():
    print(current_state)
    return render_template('section_js.html', section_id=current_state)

# @app.route('/section', methods=['GET','POST'])
# def section():
#     if request.method == 'POST':
#         data = request.form['command'] 
#         print(data)
#         current_state = data
#         return make_response('OK', 200)
#     else:
#         return render_template('section_js.html', section_id=current_state)


# @app.route('/command', methods=['POST'])
# def hdkCommands():
#     # if request.method == 'POST':
#     data = request.form['command'] 
#     print(data)
#     current_state = data
#     return 'OK'
#     # else:
#     #     return 'ok'
@app.route('/command/<command>', methods=['GET'])
def hdkCommands(command: str):
    global current_state
    command = parse_string(command, ['schedule', 'agenda', 'timetable', 'itinerary', 'appointment', 'timeline', 'program', 'planner', 'calendar', 'diary', 'temperature','climate','meteorology','forecast','prediction','outlook','conditions','elements','weather', 'eat','munch','brunch','meal','food','hungry','starving','famished','craving','appetite','nutrient','breakfast', 'outfit','attire','wardrobe','clothing','dress','clothes', 'closet'])
    print(command)
    command = command.lower()
    if command in ['schedule', 'agenda', 'timetable', 'itinerary', 'appointment', 'timeline', 'program', 'planner', 'calendar', 'diary']:
        current_state = 'calendar'
    elif command in ['temperature', 'climate','meteorology','forecast','prediction','outlook','conditions','elements','weather']:
        current_state = 'weather'
    elif command in ['eat','munch','brunch','meal','food','hungry','starving','famished','craving','appetite','nutrient','breakfast']:
        current_state = 'breakfast'
    elif command in ['outfit','attire','wardrobe','clothing','dress','clothes', 'closet']:
        current_state = 'closet'

    return 'OK'

