### NTS: only input in lower case
### TD: .lower()
### NTS: planes go two ways
'''
  ___               _     _                                                       
 | _ )  ___   ___  | |_  | |_  '  ___    ___   _ _    ___    __ __ __  __ _   _  _ 
 | _ \ / _ \ / _ \ |  _| | ' \  (_-<   / _ \ | ' \  / -_)   \ V  V / / _` | | || |
 |___/ \___/ \___/ _\__| |_||_| /__/   \___/ |_||_| \___|    \_/\_/  \__,_|  \_, |
 | |_    ___  | | (_)  __| |  __ _   _  _   ___ | |                          |__/ 
 | ' \  / _ \ | | | | / _` | / _` | | || | (_-< |_|                               
 |_||_| \___/ |_| |_| \__,_| \__,_|  \_, | /__/ (_)                               
                                     |__/                                         

'''
import random

def gap():
    print ("")
    print ("")
    
hotels = []
class Hotel():
    def __init__(self, hotelName, city, unitsAvai):
        self.hotelName = hotelName
        self.city = city
        self.unitsAvai = unitsAvai
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
        
bookings = []
class Booking():
    def __init__(self, bookingCode, username, flightCode, hotelName, authNum=None):
        self.bookingCode = bookingCode
        self.username = username
        self.hotelName = hotelName
        self.flightCode = flightCode
        ### Random int selected for when user makes/cancels bookings
        ### Not proper practice but i cba to do it and no one will be cracking this
        self.authNum = random.randint(100,1000)
        flights.append([bookingCode, username, flightCode, hotelName, authNum])

### Static variables
### Hotel name, city, available rooms
### TD: Maybe add website link for each hotel?
Hilton = Hotel("Hilton", "london", 900)
BurjAl = Hotel("Burj Al Arab", "dubai", 900)
Plaza = Hotel("Plaza Hotel", "new york", 500)
MarinaBay = Hotel("Marina Bay Sands", "singapore", 200)
TravelLodge = Hotel("Lisbon Travel Lodge", "lisbon", 50)

### Flight name, from, to, day of week (1-7), time (00.00 - 24.00) 
MH5230 = Flight("MH5230", "london", "lisbon", 1, 05.00)
MH5231 = Flight("MH5231", "lisbon", "london", 6, 20.00)
MH5232 = Flight("MH5232", "london", "paris", 4, 07.30)


### Test Booking
giovanni1234 = Booking("giovanniMH5231", "giovanni", "MH5231", "Lisbon Travel Lodge")


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
    print ("You are about to book a holiday, if you would like to be reminded of your options please enter 'remind', if not press return")
    usrin = input("")
    if usrin.lower() == "remind":
        designAtrip()
    x = 1
    while x == 1:
        print ("Please enter your desired flight number")
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
    print ("Booking the flight ", chsnFlight)
    print ("Booking the hotel ", chsnHotel)
    bookingCodeP = usrName + chsnFlight
    test = bookingCodeP
    test = Booking(bookingCodeP, usrName, chsnFlight, chsnHotel)
    gap()
    print ("booking code", test.bookingCode)
    print ("name ", test.username)
    print ("Flight ", test.flightCode)
    print ("Hotel name ", test.hotelName)
    print ("auth number ", test.authNum)
    
    
    



###  __  __          _        
### |  \/  |  __ _  (_)  _ _  
### | |\/| | / _` | | | | ' \ 
### |_|  |_| \__,_| |_| |_||_|
                          
designAtrip()
bookAtrip()
