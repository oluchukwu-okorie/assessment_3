import numpy as np
import pandas as pd
import requests
import json

secrets = open('secrets.json',)
secrets = json.load(secrets)

complains = []
url_detect = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"
url_translate = "https://google-translate1.p.rapidapi.com/language/translate/v2"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-key': secrets['api_key'],
    'x-rapidapi-host': "google-translate1.p.rapidapi.com"
}

def initialize_system():
    print("Welcome! Are you a customer or a team user ?")
    print("Enter 0 for CUSTOMER: ")
    print("Enter 1 for TEAM: ")
    choice = input("Please select your user type: ")
    
    if choice not in ['0', '1']:
        print("YOU MUST SELECT EITHER 0 or 1")
    if choice == '0':
        initialize_customer_system()
    if choice == '1':
        initialize_team_system()
        

def initialize_customer_system():
    global complains
    
    print("Welcome Customer! ")
    print("Please submit your complain! ")
    complains.append(input())
    print("Your Complain has been submitted!")
    return complains
    

def initialize_team_system():
    global complains
    
    print("Your complains are:  SELECT A NUMBER BELOW!")
    
    count = 0
    for complain in complains:
        print(complain + ": " + str(count))
        count+=1
        
    print("Pick a complain from 0 to " + str(len(complains)-1))
    choice = input("Please select a complain: ")
    
    if int(choice) not in list(range(len(complains))):
        print("YOU MUST SELECT A NUMBER BETWEEN 0 AND UP TO " + str(len(complains)-1))
    if int(choice) in list(range(len(complains))): 
        complain_selected = complains[int(choice)]
        print("You selected: ", complain_selected)
        transform_complain_text = "q="+complain_selected
        detected_language = json.loads(detect_language(transform_complain_text))
        lang = detected_language['data']['detections'][0][0]['language']
        print("The language detected is: ", lang)
        target = input("Please type language you want to translate to: e.g type 'es' for spanish - check https://cloud.google.com/translate/docs/languages")
        translated_language = json.loads(translate_language(complain_selected, target, lang))
        print("The tranlslated text is: ", translated_language['data']['translations'][0]['translatedText'])
    


def detect_language(complain_text):
    response = requests.request("POST", url_detect, data=complain_text, headers=headers)
    return response.text

def translate_language(text, target, source):
    tranform_payload = "q="+text+"&target="+target+"&source="+source
    response = requests.request("POST", url_translate, data=tranform_payload, headers=headers)
    return response.text