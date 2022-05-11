"""Kisha Blackstock Lab 9 Class for Calculating Miles Per Gallon
"""


class Mileage:
    """Define variables of miles and gallons"""

    def __init__(self, miles, gallons):
        self.__miles = float(miles)
        self.__gallons = float(gallons)
        self.__mpg = 0

    def get_miles(self):
        """Define miles getter"""
        return self.__miles

    def get_gallons(self):
        """Define gallons getter"""
        return self.__gallons

    def get_mpg(self):
        """Define calculate mpg"""
        self.__mpg = self.__miles / self.__gallons
        if self.__mpg <= 0:
            print("Can't be 0")
        return self.__mpg


class Car(Mileage):
    """Define type of car being driven"""

    def __init__(self, name, color, miles, gallons):
        self.__name = name
        self.__color = color
        super().__init__(miles, gallons)

    def __str__(self):
        car_details = (
            "\nOutput:\nName of the car : "
            + self.__name
            + "  \nColor of the car : "
            + self.__color
            + "\nMiles entered : "
            + str(super().get_miles())
            + "\nGallons entered : "
            + str(super().get_gallons())
            + " \nMiles per gallon driven today is :"
            + str(super().get_mpg())
        )
        return car_details


name = input("Enter name of the car: ")
color = input("Enter color of the car: ")
miles = input("Enter miles driven today: ")
gallons = input("Enter gas used today: ")
mileage = Mileage(miles, gallons)
car = Car(name, color, miles, gallons)
print(car.__str__())
