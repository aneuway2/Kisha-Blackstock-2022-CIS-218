# superclass
"""Lab 13"""


class Person:
    """Creating the class of Person"""

    def __init__(self, per_name, per_age):
        self.name = per_name
        self.age = per_age

    def display1(self):
        """Display Function"""
        print("name:", self.name)
        print("age:", self.age)

    def getname(self):
        """getname Function"""
        return self.name

    def setname(self, _name):
        """setName Function"""
        self.name = _name

    def getage(self):
        """getAge Function"""
        return self.age

    def setage(self, _age):
        """setAge Function"""
        self.age = _age

    def compare_age(self, other):
        """compare_age Function"""
        if self.age > other.age:
            return self.name + " have greater age"
        if self.age < other.age:
            return other.name + " have greater age"

        return "both have same gpa"

    def test_getname(self, __name):
        """Testing getname Function"""
        if self.name == __name:
            return "test_getname :  Passed"

        return "test_getname :  Failed"

    def test_setname(self, __name):
        """Testing setname Function"""
        self.name = __name
        if self.name == __name:
            return "test_setname :  Passed"

        return "test_setname :  Failed"

    def test_getage(self, __age):
        """Testing getage Function"""
        if self.age == __age:
            return "test_getage :  Passed"

        return "test_getage :  Failed"

    def test_setage(self, __age):
        """Test setage Function"""
        self.age = __age
        if self.age == __age:
            return "test_setage :  Passed"

        return "test_setage :  Failed"

    def test_compare_age(self, other, message):
        """Test compare age Function"""
        if self.compare_age(other) == message:
            return "test_compare_age :  Passed"

        return "test_compare_age :  Failed"


# subclass


class Student(Person):
    """Create Student subclass"""

    def __init__(self, _name, _age, _points_earned, _credits_taken):
        self.points_earned = _points_earned
        self.credits_taken = _credits_taken
        Person.__init__(self, _name, _age)

    def calc_gpa(self):
        """Function Description"""
        return self.points_earned / self.credits_taken

    def __str__(self):
        """Function Description"""
        return self.name + " - " + self.calc_gpa()

    def __repr__(self):
        """string representation of an object"""
        return f'Student("{self.name}","{self.age}","{self.points_earned}","{self.credits_taken}","{self.calc_gpa()}")'

    def compare_gpa(self, other):
        """Function Description"""
        if self.calc_gpa() > other.calc_gpa():
            return self.name + " have greater gpa"
        if self.calc_gpa() < other.calc_gpa():
            return other.name + " have greater gpa"

        return "both have same gpa"

    def test_calc_gpa(self, gpa):
        """Function Description"""
        if self.calc_gpa() == gpa:
            return "test_calc_gpa :  Passed"

        return "test_calc_gpa :  Failed"

    def test_compare_gpa(self, other, message):
        """Function Description"""
        if self.compare_gpa(other) == message:
            return "test_compare_gpa :  Passed"

        return "test_compare_gpa :  Failed"


name1 = input("Enter name of the student : ")
age1 = float(input("Enter age of the student : "))
points_earned1 = float(input("Enter points earned by the student : "))
credits_taken1 = float(input("Enter credits taken by the student : "))
student1 = Student(name1, age1, points_earned1, credits_taken1)
print("GPA of the student : " + str(student1.calc_gpa()))
name2 = input("Enter name of the student : ")
age2 = float(input("Enter age of the student : "))
points_earned2 = float(input("Enter points earned by the student : "))
credits_taken2 = float(input("Enter credits taken by the student : "))
student2 = Student(name2, age2, points_earned2, credits_taken2)
print(student1.compare_gpa(student2))
print(student1.compare_age(student2))
print(student1.test_getname(name1))
print(student1.test_setname("Test Name"))
print(student1.test_getage(age1))
print(student1.test_setage(26))
print(student1.test_calc_gpa(points_earned1 / credits_taken1))
print(student1.test_compare_age(student2, "Test Name have greater age"))
print(student1.test_compare_gpa(student2, "Test Name have greater gpa"))
