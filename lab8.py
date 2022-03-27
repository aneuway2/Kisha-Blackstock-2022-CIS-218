"""Kisha Blackstock Lab 8 Class for Calculating Miles Per Gallon
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


miles = input("Enter miles driven today: ")
gallons = input("Enter gas used today: ")
mileage = Mileage(miles, gallons)
print("Miles per gallon driven today is", mileage.get_mpg())
