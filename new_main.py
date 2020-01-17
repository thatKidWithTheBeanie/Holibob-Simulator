'''
  ___               _     _                                                       
 | _ )  ___   ___  | |_  | |_  ' ___    ___   _ _    ___    __ __ __  __ _   _  _ 
 | _ \ / _ \ / _ \ |  _| | ' \  (_-<   / _ \ | ' \  / -_)   \ V  V / / _` | | || |
 |___/ \___/ \___/ _\__| |_||_| /__/   \___/ |_||_| \___|    \_/\_/  \__,_|  \_, |
 | |_    ___  | | (_)  __| |  __ _   _  _   ___ | |                          |__/ 
 | ' \  / _ \ | | | | / _` | / _` | | || | (_-< |_|                               
 |_||_| \___/ |_| |_| \__,_| \__,_|  \_, | /__/ (_)                               
                                     |__/                                         
'''

def welcome():
    print ("  ___           _   _    _                   ")
    print (" | _ ) ___  ___| |_| |_ ( )___  ___ _ _  ___  ")
    print (" | _ \/ _ \/ _ \  _| ' \|/(_-< / _ \ ' \/ -_) ")
    print (" |___/\___/\___/\__|_||_| /__/ \___/_||_\___| ")
    print ("                     __ _ _      _   _      _ ")
    print ("__ __ ____ _ _  _   / _| (_)__ _| |_| |_ __| |")
    print ("\ V  V / _` | || | |  _| | / _` | ' \  _(_-<_|")
    print (" \_/\_/\__,_|\_, | |_| |_|_\__, |_||_\__/__(_)")
    print ("              |__/          |___/              ")                                        
    print ("Hello and welcome to Booth's one way flights!")
    gap()
    print ("If you are looking to escape an extistenial crisis, this is the place")
    print ("We can book your flight and expensive hotel with ease, just follow the prompts")

import random

def gap():
    print ("")
    print ("")
    
hotels = []
class Hotel():
    def __init__(self, hotelName, city):
        self.hotelName = hotelName
        self.city = city
        hotels.append([hotelName, city])

flights = []
class Flight():
    def __init__(self, flightCode, fromCity, toCity, dayOfWeek, leaveTime):
        self.flightCode = flightCode
        self.fromCity = fromCity
        self.toCity = toCity
        self.dayOfWeek = dayOfWeek
        self.leaveTime = leaveTime
        flights.append([flightCode, fromCity, toCity, dayOfWeek, leaveTime])

    def getFlightInfo():
        print ("Flight ", flightCode, " details:")
        print ("Departing ", fromCity)
        print ("Arriving at ", toCity)
        print ("On ", dayOfWeek, " at ", leavetime)
        
bookings = []
class Booking():
    def __init__(self, bookingCode, username, flightCode, hotelName, authNum):
        self.bookingCode = bookingCode
        self.username = username
        self.hotelName = hotelName
        self.flightCode = flightCode
        self.authNum = authNum
        bookings.append([bookingCode, username, flightCode, hotelName, authNum])

    def getBookingInfo(self):
        print ("Your booking info")
        print ("booking code", self.bookingCode)
        print ("name ", self.username)
        print ("Flight ", self.flightCode)
        print ("Hotel name ", self.hotelName)
        print ("auth number ", self.authNum)
        gap()        

### Static variables
### Hotel name, city, available rooms
### TD: Maybe add website link for each hotel?
Hilton = Hotel("Hilton", "london")
BurjAl = Hotel("Burj Al Arab", "dubai")
Plaza = Hotel("Plaza Hotel", "new york")
MarinaBay = Hotel("Marina Bay Sands", "singapore")
TravelLodge = Hotel("Lisbon Travel Lodge", "lisbon")

### Flight name, from, to, day of week (1-7), time (00.00 - 24.00) 
MH5230 = Flight("MH5230", "london", "lisbon", "Monday", 05.00)
MH5231 = Flight("MH5231", "lisbon", "london", "Sunday", 20.00)
MH5232 = Flight("MH5232", "london", "paris", "Thursday", 07.30)

### Test Booking
giovanni1234 = Booking("giovanniMH5231", "giovanni", "MH5231", "Lisbon Travel Lodge", 420)

###    _        _           _        
###   /_\    __| |  _ __   (_)  _ _  
###  / _ \  / _` | | '  \  | | | ' \ 
### /_/ \_\ \__,_| |_|_|_| |_| |_||_|

adminCode = "6969"                                  

def ListAllBookings():
    for i in range(len(bookings)):
        print (bookings[i])
        
###  ___               _   
### | _ )  ___   ___  | |__
### | _ \ / _ \ / _ \ | / /
### |___/ \___/ \___/ |_\_\

### Design the trip                    
### parse in home and dest in function below

def FlightsFromPlaceToPlace(home, dest):
    for i in range(len(flights)):
        if home in flights[i][1] and dest in flights[i][2]:
            print ("Flights from ", home, " to ", dest, ":")
            print (flights[i])

def HotelsInPlace(dest):
    for i in range(len(hotels)):
        if dest in hotels[i]:
            print ("Hotels in ", dest, ": ")
            print (hotels[i])

def TripDesignFacade(dest, home):
    FlightsFromPlaceToPlace(home, dest)
    HotelsInPlace(dest)

def designAtrip():
    print ("Hello, where would you like to travel?")
    dest = input ("")
    print ("And where are you travelling from?")
    home =  input ("")
    gap()
    TripDesignFacade(dest, home)

### Book the trip
def bookAtrip():
    gap()
    print ("You are about to book a holiday, if you would like to review your options please enter 'remind', if not press return")
    usrin = input("")
    if usrin.lower() == "remind":
        designAtrip()
    x = 1
    while x == 1:
        print ("Please enter your desired flight code")
        chsnFlight = input("")
        for i in range(len(flights)):
            if chsnFlight in flights[i]:
                print ("You have selected the flight:")
                print (chsnFlight)
                x = 2
    while x == 2:
        print ("Please enter your desired Hotel")
        chsnHotel = input("")
        for i in range(len(hotels)):
            if chsnHotel in hotels[i]:
                print ("You have selected the hotel:")
                print (chsnHotel)
                x = 3
    print ("Please enter your first name")
    usrName = input("")
    print ("Please rate your happiness from 100 - 9999")
    usrNum = input("")
    print ("Booking the flight ", chsnFlight)
    print ("Booking the hotel ", chsnHotel)
    ### TD: Think of a new naming scheme that wont mix with the loops
    bookingCodeP = usrName + usrNum
    ### When searching in future, use bookingCode not var name - conflicts with bcodep
    ### New instance is placed in the list even after bcodep is overwritten
    bookingCodeP = Booking(bookingCodeP, usrName, chsnFlight, chsnHotel, usrNum)
    print (bookingCodeP.bookingCode)
    gap()
    print ("Your booking code is ", bookingCodeP.bookingCode, " do not forget it as it cannot be changed")
    gap()
    menu()

def viewBooking():
    bookatt = input ("What is your booking number?")
    for i in range(len(bookings)):
        if bookatt in bookings[i][0]:
            print ("Your flight code is", bookings[i][2])
            print ("Your hotel is", bookings[i][3])
    
###  __  __              
### |  \/  |___ _ _ _  _ 
### | |\/| / -_) ' \ || |
### |_|  |_\___|_||_\_,_|
def menu():
    while True:
        gap()
        print ("Menu: ")
        print ("1. Design a trip")
        print ("2. Book a trip")
        print ("3. View your booking")
        print ("4. View all bookings [ADMIN]")
        gap()
        print ("Please enter a number 1 - 4")
        menuChoice = input ("")
        if menuChoice == "1":
            designAtrip()
        if menuChoice == "2":
            bookAtrip()
        if menuChoice == "3":
            viewBooking()
        if menuChoice == "4":
            attempt = input ("Please enter the admin code")
            if attempt == adminCode:
                ListAllBookings()
            else:
                print ("Incorrect password")
                
###  __  __          _        
### |  \/  |  __ _  (_)  _ _  
### | |\/| | / _` | | | | ' \ 
### |_|  |_| \__,_| |_| |_||_|
welcome()
menu()                          
