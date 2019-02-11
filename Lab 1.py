from bs4 import BeautifulSoup
import urllib.request

#Question 1: Bank Account class
class BankAccount:
    #Class variables
    name = ""
    totalAmount = 0

    #Constructor setting name and initial amount
    def __init__(self, name, initial_deposit):
        self.name = name
        self.totalAmount = initial_deposit

    #Deposit method
    def deposit(self, amount):
        self.totalAmount += amount

    #Withdrawal method
    def withdrawal(self, amount):
        self.totalAmount -= amount

    #For User Input to Account
    def User_deposit(self):
        self.totalAmount+=int(input("Enter Amount that you want to deposit: "))

    #For User withdrawal from Account
    def User_withdrawal(self):
        self.totalAmount-=int(input("Enter Amount that you want to withdraw: "))

#Bank Account uses for question 1
myAccount = BankAccount("Andrew", 0)
myAccount.User_deposit()
myAccount.User_withdrawal()
myAccount.deposit(300)
myAccount.deposit(250)
myAccount.withdrawal(100)
myAccount.deposit(50)

print(myAccount.totalAmount)

#Question 2: Initialize our list of tuples and an empty dictionary
listofTuples = [( 'John', ('Physics', 80)), ( 'Daniel', ('Science', 90)), ('John', ('Science', 95)), ('Mark',('Maths', 100)), ('Daniel', ('History', 75)), ('Mark', ('Social', 95))]
dictofTuples = {}
#for every tuple in out list...
for tup in listofTuples:
    #If the name is not in our dictionary
    if tup[0] not in dictofTuples.keys():
        #add the tuple to the dictionary
        dictofTuples.setdefault(tup[0], [tup[1]])
    #Otherwise, add the class and score to the corresponding key value name
    else:
        dictofTuples[tup[0]] += [tup[1]]

print(dictofTuples)

#Question 3: initialize our list of students by class and 2 empty lists for common names, and not common names
pythonStudents = ['John', 'Mark', 'Sally']
webAppStudents = ['Jane', 'Mark', 'Jones', 'Gordon']
both = []
notCommon = []
temp=""
print("Current Python Students: ", pythonStudents)
while temp!="x":
    temp=str(input("Please Enter Name of Student in Python else enter x: "))
    if temp!="x":
        pythonStudents.append(temp)
print("Current Python Students: ", pythonStudents)
print("Current WebApp Students: ", webAppStudents)
temp=""
while temp!="x":
    temp=str(input("Please Enter Name of Student in webApp else enter x: "))
    if temp!="x":
        webAppStudents.append(temp)
print("Current WebApp Students: ", webAppStudents)
#for eeach person in our first class
for person in webAppStudents:
    #if that person is in the second class
    if person in pythonStudents:
        #add that person to our both list
        both.append(person)
#for each person in our first class
for person in webAppStudents:
    #if that person isn't in both class list
    if person not in both:
        #add that person to not common list
        notCommon.append(person)
#do the same for the second class
for person in pythonStudents:
    if person not in both:
        notCommon.append(person)
print("Students in Both Classes: ",both,"\n","Students Not Common in both Classes: ", notCommon)

#Question 4:
#enter any string from the console
inputString = input("enter a string\n")

#grab first character in string
string = inputString[0]
#length will be at least 1
length = 1
#add the first character to our dictionary of string and length
stringDict = {1: inputString[0]}

#for each character in our input string starting with the second character
for x in range(1, len(inputString)):
    #if character is not the same as the last
    if inputString[x] != inputString[x-1]:
        #add that character to our string
        string += inputString[x]
        #increase the length by 1
        length+=1
        #otherwise
    else:
        #reset length to 1
        length = 1
        #reset search string to our current character
        string = inputString[x]
    #add our current string and length to our dictionary
    stringDict[length] = string

#print out the entry with the highest length in our dictionary
print("Max Substring length: ",max(stringDict)," Max Substring being: ", stringDict[max(stringDict)])

#Question 5:
#Person class
#Class 1
class Person:
    #Person class variable
    name = ""

    #constructor setting name
    def __init__(self, name):
        self.name = name
#Employee class derived from Person
#Class 2
class Employee(Person):
    #Employee class variables
    id = 0
    dept = ""

    #constructor setting id and dept
    def __init__(self, id, dept):
        self.id = id
        self.dept = dept
        #super call to Person class
        super(Person, self).__init__()
#Pilot class derived from Employee
#Class 3
class Pilot(Employee):
    #Pilot class variables
    license_number = 0

    #constructor setting license
    def __init__(self, license):
        self.license_number = license
        #super call to Employee class
        super(Employee, self).__init__()
#Passenger class derived from Person
#Class 4
class Passenger(Person):
    #Person class variables
    flight_number = 0
    __credit_card_num = 0

    #constructor setting flight number
    def __init__(self, flight_number):
        self.flight_number = flight_number
        #super call to Person class
        super(Person, self).__init__()

    #add card number method
    def add_card(self, card):
        self.__credit_card_num = card
#Flight class
#Class 5
class Flight:
    #Flight class variables
    number = 0
    pilot = ""
    passengers =[]

    #constructor setting number and pilot
    def __init__(self, number, pilot):
        self.number = number
        self.pilot = pilot

    #method adding passenger to list of passengers
    def add_passenger(self, passenger):
        self.passengers.append(passenger)

#Question 6:
#input search term
search = input("Enter Wikipedia search term\n")
#replace spaces with underscores
search.replace(' ', '_')
#open that Wikipedia link
with urllib.request.urlopen('https://en.wikipedia.org/wiki/' + search) as response:
    #open link for parsing and initialize list of data
    soup = BeautifulSoup(response, 'html.parser')
    data = []
    #find all occurrences of tables
    tables = soup.findAll('table')
    #open a file for writing
    file = open("Table_Info", 'w')
    #for every table in out collection of tables...
    for table in tables:
        #find the body of the table
        table_body = table.find('tbody')
        #find all rows in the table
        rows = table_body.findAll('tr')
        #for every row in our current table
        for row in rows:
            #find all the column values in our row
            cols = row.find_all('td')
            #clean the column entry
            cols = [ele.text.strip() for ele in cols]
            #add that column entry to it's row and that row to our list of data
            data.append([ele for ele in cols if ele])

    #for all rows in our list of data...
    for x in range(0, len(data)):
        #for all column entries in our row...
        for y in range(0, len(data[x])):
            #write that column entry followed by a newline for formatting
            file.write(data[x][y] + "\n")
        print(data[x])
