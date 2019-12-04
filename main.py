### NTS: only input in lower case
### TD: .lower()
import random
hotels = []
class Hotel():
    def __init__(self, hotelName, city, unitsAvai, authNum=None):
        self.hotelName = hotelName
        self.city = city
        self.unitsAvai = unitsAvai
        if authNum is None:
            authNum = random.randint(0,100)
        hotels.append([hotelName, city, authNum])

    def book():
        if unitsAvai > 0:
            unitsAvai - 1
            print("You have booked this hotel")
flights = []
class Flight():
    def __init__(self, flightCode, fromCity, toCity, dayOfWeek, leaveTime, authNum=None):
        self.flightCode = flightCode
        self.fromCity = fromCity
        self.toCity = toCity
        self.dayOfWeek = dayOfWeek
        self.leaveTime = leaveTime
        ### Random int selected for when user makes/cancels bookings
        ### Not proper practice but i cba to do it and no one will be cracking this
        if authNum is None:
            authNum = random.randint(0,100)
        flights.append([flightCode, fromCity, toCity, authNum])
        

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

#### begin actual code

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
    print ("")
    TripDesignFacade(dest, home)

designAtrip()

bookATrip()
