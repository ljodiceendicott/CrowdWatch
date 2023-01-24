import sys

if len(sys.argv) < 2: #This means that the user does not have a file
    with open('../Documentation/intro.txt','r') as f:
        contents = f.read()
        print(contents)
        manual_input=input('would you like to enter the data manually?\n'+
        '(Y/N)')
        manual_input = manual_input.capitalize()
        if manual_input == 'N':
            print('have a good day. GoodBye!')
        elif manual_input == 'Y':
            print('Alright time to get started!')
        else:
            print('invalid response! try again') 

def accountMake():
    #Make user
    businessname =input('What is the name of the business?')
    num_loc = int(input('how many locations are trying to be kept track of?'))
    locations = []
    for i in num_loc:
        name = input('What is the nickname for this location?')
        maxcap = int(input('what is the maximum capacity for this location?'))
        loc = location(name, maxcap)
        locations.append(loc)
    account = Account(businessname, locations)

class Account:
    def __init__(self , name, locations) -> None:
        self.name = name
        self.locations = locations
    def filecreation():
        print('file Creation')

class location:
    def __init__(self, name, maxCap):
        self.name = name
        self.maxCap = maxCap

# How many different locations/sublocations are trying to be counted?
# (insert a real whole number)
# **Based on this number Loop to **

