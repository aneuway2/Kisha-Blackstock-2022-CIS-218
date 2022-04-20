"""Lab 11 Kisha Blackstock"""


class Car:
    """Parent Class"""

    __name = None
    __color = None
    __miles = None
    __gallons = None
    __mpg = 0

    def __init__(self, _name, _color, _miles, _gallons):
        """Constructor"""
        self.__name = _name
        self.__color = _color
        self.__miles = float(_miles)
        self.__gallons = float(_gallons)
        self.__mpg = self.__miles / self.__gallons

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
        return self.__mpg == other.__mpg

    def __lt__(self, other):
        """compares the Mileage of both cars and returns the results"""
        return self.__mpg < other.__mpg

    def __gt__(self, other):
        """compares the Mileage of both cars and returns the results"""
        return self.__mpg > other.__mpg

    def get_mpg(self):
        """Constructor"""
        self.__mpg = self.__miles / self.__gallons
        if self.__mpg <= 0:
            print("Can't be 0")
        return self.__mpg

    def test_getmiles(self, miles):
        """Test"""
        if self.get_miles() == miles:
            return "Test pass : results are equal"
        return "Test fail : results are not equal"

    def test___str__(self, name, color, miles, gallons, mpg):
        """Test"""
        message = f'Car("{name}","{color}","{miles}","{gallons}","{mpg}")'
        if self.__str__() == message:
            return "Test pass : results are equal"
        return "Test fail : results are not equal"

    def test___repr__(self, name, color, miles, gallons, mpg):
        """Test"""
        message = f'Car("{name}","{color}","{miles}","{gallons}","{mpg}")'
        if self.__repr__() == message:
            return "Test pass : results are equal"
        return "Test fail : results are not equal"

    def test___eq__(self, other, mpg1, mpg2):
        """test"""
        if self.__eq__(other) == (mpg1 == mpg2):
            return "Test pass : results are equal"
        return "Test fail : results are not equal"

    def test___lt__(self, other, mpg1, mpg2):
        """Test"""
        if self.__lt__(other) == (mpg1 < mpg2):
            return "Test pass : results are equal"
        return "Test fail : results are not equal"

    def test___gt__(self, other, mpg1, mpg2):
        """Test"""
        if self.__gt__(other) == (mpg1 > mpg2):
            return "Test pass : results are equal"
        return "Test fail : results are not equal"


class Mileage(Car):
    """Child Class"""

    def main():
        """Main method"""
        name_1 = input("Enter name of the car: ")
        color_1 = input("Enter color of the car: ")
        miles_1 = float(input("Enter miles driven today: "))
        gallons_1 = float(input("Enter gas used today: "))
        car_1 = Car(name_1, color_1, miles_1, gallons_1)
        print(car_1.__repr__())
        print(car_1.__str__())
        print(car_1.test_getmiles(miles_1))
        print(
            car_1.test___str__(name_1, color_1, miles_1, gallons_1, miles_1 / gallons_1)
        )
        print(
            car_1.test___repr__(
                name_1, color_1, miles_1, gallons_1, miles_1 / gallons_1
            )
        )
        print("Please enter other car details below")
        name_2 = input("Enter name of the car: ")
        color_2 = input("Enter color of the car: ")
        miles_2 = float(input("Enter miles driven today: "))
        gallons_2 = float(input("Enter gas used today: "))
        car_2 = Car(name_2, color_2, miles_2, gallons_2)
        print(car_2.__repr__())
        print(car_1.__eq__(car_2))
        print(car_1.__lt__(car_2))
        print(car_1.__gt__(car_2))
        print(car_1.test___eq__(car_2, miles_1 / gallons_1, miles_2 / gallons_2))
        print(car_1.test___lt__(car_2, miles_1 / gallons_1, miles_2 / gallons_2))
        print(car_1.test___gt__(car_2, miles_1 / gallons_1, miles_2 / gallons_2))

    if __name__ == "__main__":
        main()
