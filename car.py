class Car:
    """
    A class for cars, with make, type and mileage
    """
    def __init__(self, make, car_type, color, mileage=0):
        """
        Creates a new car object with mileage set to 0

        Arguments:
        - make (str): the make of the car
        - car_type: the type of the car
        - color: the color of the car
        """
        self.make = make
        self.car_type = car_type
        self.color = color
        self.mileage = mileage

    def info(self):
        """
        Returns as string with information about the car

        Returns:
        - string: information about the car
        """
        return f'This is a {self.color} {self.make} {self.car_type} with a mileage of {self.mileage} '

    def drive(self, km):
        """
        Drives a distance, changing the milaege  

        Arguments:
        - km (float): number of kilometers to drive      
        """
        if km < 0:
            raise Exception('You can not drive a negative distance')
        else:
            self.mileage += km
    

    def __eq__(self, other):
        return self.make == other.make and self.car_type == other.car_type



car1 = Car('Jeep', 'Grand', 'Black') # -> Car.__init__(Jeep)
car2 = Car('Jeep', 'Grand', 'White')

print(car1 == car2) # -> Car.__eq__(car1, car2)