'''SystemUser = "French Customers & multi_langual customers
User Case Story (Customer)
1. The system should welcome me as a user
2. The system should ask me to submit complain
3. The system should tell me when my when my complain is submitted

User Case Story (Team)
1. The system should list all the complain
2. The system should ask me to pick a complain
4. The system should be able to detect the language used in a complain text
5. The system should be able to translate from one language to the other base on specification

'''

import json 
import requests 


name = input("Dear customer, enter your name: ")
location = input("May I know your location: ")
welcome = (" Hello {} from {}, Welcome to K & O, we are deeply sorry for the inconvince we have caused you, proceed to make your complains".format(name, location))
print(welcome)


complains = {}
next = 1
while next:
    sub = int(input(
            'Do you want to submit  a complain; Enter 1 to sumbit, 0 to quit: '))
    if sub == 1:         
        username= input('Please enter your 4_lettered username: ')
        new_complain = input('Enter your complain: ')
        print("Complain received!, you will get a feedback soon")
        complains[username] = {
            "id": username, "issue": new_complain}
        print(complains)
    elif sub == 0:
        print('Thanks for choosing us!') 
        break


print(complains)
checker = 1
while checker:
    team = int(input('Welcome team, enter 1 to view complains again, 2 to pick a complain, 3 to quit: '))
    if team == 1:
        print(complains)
    elif team == 2:
        num = input('Enter the id of complain you want to view: ') 
        data = complains[num]['issue']
        print(data)  
    elif team == 3:
        print("Goodbye team") 
        break

if data:
    detect = int(input('Do you want to detect the language, if Yes enter 1 if No enter 0: '))
    if detect == 1:

        url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"

        payload = "q=Hello%2C%20world!&target=es&source=en"
        headers = {
                    'content-type': "application/x-www-form-urlencoded",
                    'accept-encoding': "application/gzip",
                    'x-rapidapi-key': "8a0acd6838msh71c872c49d7c169p12a8b3jsn1a0f03d938f5",
                    'x-rapidapi-host': "google-translate1.p.rapidapi.com"
                      }

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)
   
    elif detect == 0:
        print('Thank you for your time')

trans = int(input('Do you want to translate the language? Yes, Enter 1 No, Enter 0: '))   
if trans == 1:

    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    payload = "q=Hello%2C%20world!&target=es&source=en"
    headers = {
               'content-type': "application/x-www-form-urlencoded",
               'accept-encoding': "application/gzip",
               'x-rapidapi-key': "8a0acd6838msh71c872c49d7c169p12a8b3jsn1a0f03d938f5",
               'x-rapidapi-host': "google-translate1.p.rapidapi.com"
               }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
elif trans == 0:
    print("Ok. Thank you for your time")

