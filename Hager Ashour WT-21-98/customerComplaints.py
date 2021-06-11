from datetime import datetime
userComplaints = {}


def registerComplaints():
    if userComplaints:

        complaintId = input("Kindly enter the id of your complaint: ")
        name = input("Dear Customer, kindly enter your name: ")
        complaint = input("Enetr your complaint: ")
        date = datetime.date(datetime.now())
        userComplaints[complaintId]={"Id":complaintId, "Name":name, "Complaint":complaint, "Date":date}
        print(userComplaints)
        print("Your complaint submitted at", date, " We can get back to you sooner")
        
        #if complaintId in userComplaints.keys():
        #     print('This Id already in the system, please try again!')
        #     print('*********************')
        # # else:
        #      for record in userComplaints.values():
        #          if name in record.values() or complaint in record.values():
        #             #  print('Data already exist, please try again!')
        #              print('*********************')
        #          else:
        #              userComplaints[complaintId] = {
        #                  "Id":complaintId, "Name":name, "Complaint":complaint, "Date":date}
        #              print('Data recorded!')
        #              print(userComplaints.values())
        #              print("Your complaints has been recorded at ,", date,  "we can get back to you sooner!")
        #              print('*********************')
        #              break
    else:
        complaintId = input("Kindly enter the id of your complaint: ")
        name = input("Dear Customer, kindly enter your name: ")
        complaint = input("Enetr your complaint: ")
        date = datetime.date(datetime.now())
        userComplaints[complaintId]={"Id":complaintId, "Name":name, "Complaint":complaint, "Date":date}
        print(userComplaints)
        print("We recorded your complaints at", date ," we can get back to you sooner")
        print("*****************************")
        

#Select Complain
def teamCheckComplaint(complaintName):
        for record in userComplaints.values():
            if complaintName in record.values():
                print("The user complaint is ",complaintName)
                tran_complaint(complaintName)
                print('*********************')  
            # else:
            #     print("This complaint is not in the system ")

# User Case Story (Team)

def userCase():
    runtime=1
    while runtime:
        print("*****************************")
        item = int(input("Enter 1 to show all complaint, or 2 to select complaint, or 3 to quit: "))
        if item ==1:
            print(userComplaints)
        elif item ==2:
            complaintName = input("Enter the complaint you want to investigate: ")
            teamCheckComplaint(complaintName)
        elif item == 3:
            break
        else:
            print("Invalid value!")
            

# Welcome message 

def welcomeMess():
    runtime = 1
    YourName = input("Kindly enter your name: ")
    print("Dear ",YourName, "Welcome to our Company,") 
    while runtime:
        checker = int(input("Enter 1 to sumbit a complaint, or 2 to quit: "))
        if checker == 1:
            registerComplaints()
        elif checker == 2:
            break
        else:
            print("Invalid value, Enter 1 to sumbit a complaint, or 2 to quit:") 

from googletrans import Translator

def tran_complaint(lanComplaint):
     translator = Translator()
     langComplaint = translator.translate(lanComplaint, dest="en")
     print("The translation of user complaint is",langComplaint.text)
     print("The Complaint language is",langComplaint.src)



welcomeMess()
print(userComplaints)
userCase()






   
      









