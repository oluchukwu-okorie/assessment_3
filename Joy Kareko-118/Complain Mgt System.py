import json
'storing name,addresses and complains in a dictionary'
fstname = {}
custaddr = {}
complain = {}
user_id={}
mgt_name={}
'defining the customer function to input name,address and complains'



def customer ():
    fstname = input("Your name?: \n")
    custaddr = input("Your Address Please: \n")
    complain = input("Please let us know what your complain is:\n")
    complain = {}

def management ():
    
        mgt_name = input("Your name?\n")
        user_id = input("Your user_id?\n")
def complaints ():       
        counters = 1
        while counters:
          checker = int(input("Enter 1 to view complains, 2 to exit:\n"))
          if  checker == 1:
               complain = {
                      "Name:": fstname,"Complain:":complain,"Address:":custaddr}
          elif checker ==2:
                  print("System Logged Off.You have exited!\n")
                  break
          else:
                print("=========Invalid==========")

def main():
    runtime = 1
    print("Welcome to Sparkle\'s Gift House")
    while runtime:
        checker = int(input(
            'Enter 1 for Returning Customer, 2 for staff, 4 to choose again \n'))
        if checker == 1:
            customer()
            print("Your complain has been received successfully.We will get back to you within 24 hrs")
        elif checker == 2:
            management()
            complaints()
        elif checker == 4:
            break
        else:
            print('Invalid Request, try again')
            main()
main()