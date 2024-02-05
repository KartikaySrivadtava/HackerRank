#String Representation of Objects for representing maximum speed of Car and boat with respective units

#Initialize Car class
class Car:
    def __init__(self, max_speed, unit):
        #Initilizing constructor
        self.max_speed = max_speed
        self.unit = unit

    #Return result for car class
    def __str__(self):
        return 'Car with the maximum speed of ' + str(self.max_speed) + ' ' + str(self.unit)

#Initialize Boat class
class Boat:
    #Initilizing constructor
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def __str__(self):
        #Return result for boat class
        return 'Boat with the maximum speed of ' + str(self.max_speed) + ' knots'

#Sample Input argument for Car
car = Car(120, 'km/h')
print(car)
