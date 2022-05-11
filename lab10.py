"""Lab 10 Kisha Blackstock"""
class Car:
    """Parent Class"""
    __name = None
    __color = None
    __miles = None
    __gallons = None
    __mpg = 0
    def __init__(self,_name,_color,_miles,_gallons):
        """Constructor"""
        self.__name = _name
        self.__color = _color
        self.__miles = float(_miles)
        self.__gallons = float(_gallons)
        self.__mpg = self.__miles/self.__gallons
    def get_miles(self):
        """Method to return miles"""
        return self.__miles
    def get_gallons(self):
        """method to get gallons"""
        return self.__gallons
    def __repr__(self):
        """string representation of an object"""
        return f'Car("{self.__name}","{self.__color}","{self.__miles}","{self.__gallons}","{self.__mpg}")'
    def __eq__(self, other):
        """compare the Mileage of both cars and returns true if the are equal"""
        if self.__mpg == other.__mpg:
            return "Both are equal"
        #else:
            #return "Both are not equal"
        return None
    def __lt__(self, other):
        """compares the Mileage of both cars and returns the results """
        if self.__mpg < other.__mpg:
            return self.__name+"'s mileage is less than "+other.__name
        #else:
            #return self.__name+"'s mileage is not less than "+other.__name
        return None
    def __gt__(self, other):
        """compares the Mileage of both cars and returns the results """
        if self.__mpg > other.__mpg:
            return self.__name+"'s mileage is greater than "+other.__name
        #else:
            #return self.__name+"'s mileage is not greater than "+other.__name
        return None
    def get_mpg(self):
        """Constructor"""
        self.__mpg = self.__miles/self.__gallons
        if self.__mpg <= 0:
            print("Can't be 0")
        return self.__mpg

class Mileage(Car):
    """Child Class"""
    def main():
        """Main method"""
        name = input('Enter name of the car: ')
        color = input('Enter color of the car: ')
        miles = float(input('Enter miles driven today: '))
        gallons = float(input('Enter gas used today: '))
        car1 = Car(name,color,miles,gallons)
        print (car1.__repr__())
        print('Please enter other car details below')
        name = input('Enter name of the car: ')
        color = input('Enter color of the car: ')
        miles = float(input('Enter miles driven today: '))
        gallons = float(input('Enter gas used today: '))
        car2 = Car(name,color,miles,gallons)
        print (car2.__repr__())
        print(car1.__eq__(car2))
        print(car1.__lt__(car2))
        print(car1.__gt__(car2))
    if __name__ == "__main__":
        main()
