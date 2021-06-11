from datetime import datetime
userComplaints = {}

def welcomeMess():
    runtime = 1
    YourName = input("Kindly enter your name: ")
    print("Dear ",YourName, "Welcome to our Company,") 
    while runtime:
        checker = int(input("Enter 1 to sumbit a complaint, or 2 to quit: "))
        if checker == 1:
            name = input("Please enter your name: ")
            complaint = input("Please submit your complaint: ")
            date = datetime.date(datetime.now())
            print("Your complaints has been recorded at ,", date,  "we can get back to you sooner!")
            print('==========================')
            userComplaints[name] = {complaint}
        elif checker == 2:
            break
        else:
            print("Invalid value, Enter 1 to sumbit a complaint, or 2 to quit:") 

            
welcomeMess()
print(userComplaints)


name = input("Please enter your name: ")
if name in userComplaints:
    print(userComplaints[name])
else: 
    print("This complaint is not in the system")


import requests
from urllib.parse import quote

def detectLangauge(text):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"
    payload = "q=" + quote(text)
    
    headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-key': "6464df7f3dmsh79109d96d292f30p1d2e4cjsn32767b241ca1",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com"
    }
    
    response = requests.request("POST", url, data=payload, headers=headers)
    
    return(response.text)


name = input("Please enter your name:")
if name in userComplaints:
    complain_string = list(userComplaints[name])[0]
    print(complain_string)
    print(detectLangauge(complain_string))
else:
    print("This complaint is not in the system")

import requests
from urllib.parse import quote

def translateComplaint(text, target_language):
    
    source_language = detectLangauge(text)
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    payload = "q=" + quote(text) + "&target=" + target_language + "&source=" + source_language
    
    headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-key': "6464df7f3dmsh79109d96d292f30p1d2e4cjsn32767b241ca1",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com"
    }
    response = requests.request("POST", url, data=payload, headers=headers)

    return response.text


name = input("Please enter your name:")
if name in userComplaints:
    complain_string = list(userComplaints[name])[0]
    translated_object = json.loads(translateComplaint(complain_string, "en"))
    translation = translated_object["data"]["translations"][0]["translatedText"]
    print(translation)
else:
    print("This complaint is not in the system")

import json

complaints_json = json.loads('{"data":{"detections":[[{"language":"en","isReliable":false,"confidence":0.8180167078971863}]]}}')
complaints_json["data"]["detections"][0][0]["language"]