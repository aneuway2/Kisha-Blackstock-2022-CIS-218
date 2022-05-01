""" Kisha Blackstock Lab 12"""
import sqlite3


class GradeBook:
    "This is a GradeBook class to play with Database"

    def __init__(self):
        con = sqlite3.connect(":memory:")
        self.__database = con.cursor()
        self.__database.execute(
            """CREATE TABLE grades
               (name text,score real)"""
        )

    def upload_grades(self, name, score):
        """upload grades"""
        self.__database.execute("insert into grades values (?,?)", (name, score))

    def student_grade(self, name):
        """Student grades"""
        data = self.__database.execute(
            "SELECT score FROM grades WHERE name = '%s'" % name
        )
        for row in data:
            return row[0]

    def test_gradebook(self, name, score):
        """ test gradebook"""
        self.upload_grades(name, score)
        print(float(score) == float(self.student_grade(name)))
        if float(score) == float(self.student_grade(name)):
            return "Inserted"
        return "Insertion Failed"


obj = GradeBook()

# calling the instance method using the object obj
obj.upload_grades("manigi", "3.8")
print(obj.student_grade("manigi"))
print(obj.test_gradebook("manigi", "3.5"))
obj.upload_grades("sara", "4")
print(obj.student_grade("sara"))
obj.upload_grades("carol", "2.5")
print(obj.student_grade("carol"))
obj.upload_grades("akhil", "3")
print(obj.student_grade("akhil"))
obj.upload_grades("sam", "3.85")
print(obj.student_grade("sam"))
obj.upload_grades("joey", "4")
print(obj.student_grade("joey"))
