#main.py

#Add an import statement for Vehicle class
from vehiclePackage.vehicleClass import *

if __name__ == "__main__":
    #Instantiate an object of type Vehicle
    myCorvette = Vehicle("Car", 120) #Trigger a call to constructor
    myCorvette.printType() #invoking the method on object
    
    #invoke the getter for maximum speed, store the return value in a variable, print it out
    maximum_speed = myCorvette.getSpeed()
    print("Maximum Speed: ", maximum_speed)
    
    #Instantiate another Vehicle object
    myFord = Vehicle("Truck")  #myFord is an object of type Vehicle
    
    #maximum_speed = myFord.getSpeed()
    #print("Maximum Speed: ", maximum_speed)
    
    #I want a list of three Vehicles: a Car, a boat, a Spaceship
    #pick names and properties
    # friendly output to demonstrate what you did
    myVehiclesList = [Vehicle("Ford", 160), 
                      Vehicle("Sailboat", 20),
                     Vehicle("Falcon Heavy", 4000)]
    #iterate over the list
    for vehicle in myVehiclesList:
        vehicle.printType()
        print (vehicle.getSpeed())
    
    
    