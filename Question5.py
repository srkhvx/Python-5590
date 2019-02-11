from math import sin, cos, sqrt, atan2, radians
import csv
import datetime
import os
import csv

#CLASS 1, THIS CLASS IS ABOUT GENERATING AND REPORTING SCHEDULE TO THE AIRLINE CLASS
class Schedule():
    FlightID=""
    Date=datetime.datetime.now()+datetime.timedelta(hours=7)
    def __int__(self,depart=datetime.datetime.now()):
        super(Schedule, self).__int__()
        super(customer, self).__int__()
        self.date=depart
        self.day=0
        self.month=0
        self.year=0
        self.flightID=""
    def get_date(self):
        self.day=int(input("Enter Date of Flight: "))
        self.month=int(input("Enter Month of Flight: "))
        self.year=int(input("Enter Year of Flight: "))
        Schedule.Date=\
        Schedule.Date.replace(year=self.year,month=self.month,day=self.day)
        self.FlightID=str(Schedule.Date.time().hour)
    def print_det(self):
        print(self.FlightID)
        print(self.Date)


#CLASS 2, THIS CLASS IS ABOUT GETTING THE DIFFERENT SEAT OPTIONS AVAILABLE AND THE SEAT NUMBERS AND THE FARES FOR THOSE SEATS
class Airline(Schedule):
    seat = [["Economy Class", 100], ["Economy Plus", 100], ["Business Class", 100]]
    economy_class = "Economy Class"
    economy_plus = "Economy Plus"
    business_class = "Business Class"
    def __init__(self):
        super(Schedule, self).__init__()
        self.fares = [["Economy Class",500],["Economy Plus",1200],["Business Class",2000]]
        self.price=0
        self.seat_type=""
        self.AD=Schedule.FlightID
#CHECKS IF A SEAT IS AVAILABLE
    def is_available(self, booking_class):
        for i in self.seat:
            if booking_class in i:
                return self.seat[self.seat.index(i)][1] > 0
#IF SEAT IS AVAILABLE IT OKAY'S THE TRANSACTION AND REDUCES 1 SEAT FROM THE LOT
    def make_reservation(self, seat_class):
        if self.is_available(seat_class):
            for i in Airline.seat:
                if seat_class in i:
                    Airline.seat[Airline.seat.index(i)][1] = \
                    Airline.seat[Airline.seat.index(i)][1] - 1
                    self.price+=int(self.fares[self.seat.index(i)][1])
                    break
#IF RESERVATION IS CANCELLED, THIS CREDITS BACK THE SEAT WHICH WAS DEDUCTED
    def cancel_reservation(self, seat_class):
        for i in self.seat:
            if seat_class in i:
                if Airline.seat[Airline.seat.index(i)][1]<100:
                    Airline.seat[Airline.seat.index(i)][1] = \
                    Airline.seat[Airline.seat.index(i)][1] + 1
                break
#HERE OPTIONS ARE GIVEN TO THE CUSTOMER WHICH SEAT HE WANTS TO TAKE DEPENDING UPON THE FARES
    def Fares(self,distance):
        print("Please Select from below available Seats and their Fares in USD: ")
        for i in range(0,3):
            if self.is_available(Airline.seat[i][0]):
                print(i ,Airline.seat[i][0]," ",Airline.seat[i][1]," Seats available each priced at: $", (self.fares[i][1]+(distance/(4-i))))
        i=int(input("Please Enter the Seat Class number you want to reserve: "))
        if(i==0):
            self.price+=distance/4
            self.seat_type=self.economy_class
            return self.economy_class

        elif(i==1):
            self.price+=distance/3
            self.seat_type=self.economy_plus
            return self.economy_plus

        elif(i==2):
            self.price+=distance/2
            self.seat_type=self.business_class
            return self.business_class
#CLASS 4
#THIS CLASS IS ABOUT TAKING THE DESTINATION AND SOURCE INPUT FROM THE USER AND CALCULATING THE DISTANCE AND UPON WHICH THE FARES ARE CALCULATED IN AIRPLANE CLASS
class Destination(Airline):
    #__distancex is a private variable and is not accessible from any other class
    __distancex=0
    def __init__(self):
        super(Airline, self).__init__()
        self.source_city="Kansas City"
        self.destination ="New York"
        self.source_cood="0"
        self.destination_cood="0"
        self.distance=0
    def Departure_date(self):
        self.get_date()
#WE READ FROM A CSV FILE THE LIST OF CITIES THAT ARE AVAILABLE FOR TRAVELLING TO AND FROM
    def Departure(self):
        print(" Select from below list, your Departure City: ")
        with open('Destination.csv', 'r') as csvfile:
            source = []
            self.source_city = ""
            self.source_cood = ""
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            id = 0
            for row in spamreader:
                source.append([id, ','.join(row)])
                id += 1
            source.pop(0)
            for row in source:
                print(row)
            id = int(input("Source ID : "))
            for row in source:
                if (int(row[0]) == id):
                    self.source_city = row[1].split(",")[0]
                    self.source_cood = row[1].split(",")[-1]
            print(self.source_city)
            #print(source_cood)
    def Destination(self):
        print(" Select from below list, your Departure City: ")
        with open('Destination.csv', 'r') as csvfile:
            source = []
            self.destination = ""
            self.destination_cood = ""
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            id = 0
            for row in spamreader:
                source.append([id, ','.join(row)])
                id += 1
            source.pop(0)
            for row in source:
                print(row)
            id = int(input("Source ID : "))
            for row in source:
                if (int(row[0]) == id):
                    self.destination = row[1].split(",")[0]
                    self.destination_cood = row[1].split(",")[-1]
            print(self.destination)
            #print(destination_cood)

#THIS FUNCTION CALCULATES THE DISTANCE BETWEEN THE TWO SELECTED CITIES. THIS DISTANCE IS THEN LATER ADDED TO THE FARE RATE
    def Distance(self):
        R = 6373.0
        lat1 = radians(float(self.source_cood.split(" ")[1][:-1]))
        lon1 = radians(float(self.source_cood.split(" ")[0][:-1]))
        lat2 = radians(float(self.destination_cood.split(" ")[1][:-1]))
        lon2 = radians(float(self.destination_cood.split(" ")[0][:-1]))
        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        self.distance = R * c
        Destination.__distancex=self.distance
        print("Distance: ", Destination.__distancex)

#CLASS 5
#CUSTOMER CLASS IS RESPONSIBLE FOR TAKING CUSTOMER DETAILS SUCH AS NAME, AGE ETC
#FURTHER MORE THIS CLASS ALSO PRINTS OUT THE COMPLETE BOOKING DETAILS.
class customer(Destination,Airline,Schedule):
    def __init__(self,name="default",age="999",passport="NA"):
        super(Airline, self).__init__()
        super(Schedule,self).__init__()
        super(Destination, self).__init__()
        self.name=name
        self.age=age
        self.passport=passport

    def get_detail(self):
        self.name=input("Enter Name: ")
        self.age=int(input("Enter Age: "))
        self.passport=input("Enter Passport Number: ")
        self.Departure()
        self.Destination()
        self.Departure_date()
        self.Distance()
        Seat=self.Fares(self.distance)
        self.make_reservation(Seat)
    def print_details(self):
        print("Seat Type: ",self.seat_type)
        print("Customer Name: ",self.name)
        print("Customer Age: ",self.age)
        print("Customer Passport: ",self.passport)
        print("Departure City: ",self.source_city)
        print("Destination City: ",self.destination)
        print("Total Cost: $",self.price)
        print("AirPlane ID: ", (self.source_city[0:2]+self.FlightID+self.destination[0:2]) )
        print("Departure Time: ", self.Date)
    def save_ticket(self):
        self.ticket=[]
        self.ticket.append(["Seat Type: ",self.seat_type])
        self.ticket.append(["Customer Name: ",self.name])
        self.ticket.append(["Customer Age: ",self.age])
        self.ticket.append(["Customer Passport: ",self.passport])
        self.ticket.append(["Departure City: ",self.source_city])
        self.ticket.append(["Destination City: ",self.destination])
        self.ticket.append(["Total Cost: $",self.price])
        self.ticket.append(["AirPlane ID: ", (self.source_city[0:2]+self.FlightID+self.destination[0:2]) ])
        self.ticket.append(["Departure Time: ", self.Date])
        return self.ticket

#CLASS 6
#THIS CLASS IS RESPONSIBLE FOR GENERATING A CSV TICKET OF THE COMPLETE INFORMATION AND THE FLIGHT DETALS
#EACH TICKET IS SAVED WITH NAME OF THE CUSTOMER
class print_ticket(customer):
    def __int__(self):
        super(customer,self).__int__()
    def print_it(self):
        self.get_detail()
        self.print_details()
        self.ticketx=self.save_ticket()
        csv.register_dialect('myDialect',quoting=csv.QUOTE_ALL,skipinitialspace=True)
        with open(str(self.name)+".csv", 'w') as f:
            writer = csv.writer(f, dialect='myDialect')
            for row in self.ticketx:
                writer.writerow(row)

        f.close()


if __name__ == '__main__':
    ali = print_ticket()
    ali.print_it()
    ali.print_details()

    airline = Airline()
    seat_class=airline.Fares()
    airline.make_reservation(seat_class)

    alpha=Schedule()
    alpha.get_date()
    alpha.print_det()

    beta=Destination()
    beta.Departure()
    beta.destination()

    gamma=customer()
    gamma.get_detail()
    gamma.print_details()



