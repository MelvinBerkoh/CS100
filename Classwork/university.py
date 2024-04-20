# Write a class definition line and a one line docstring for the class Course_Section. Write an
# __init__ method for the class Course_Section that gives each Course_Section its own section number
# and course name. Make sure that you test this on a successful creation of a Course_Section object.

class Course_Section:
    ''' holds the course name and section number for the object created'''

    universityName = "New Jersey Institute of Technology"

    def __init__(self, courseName, sectionNumber):
        self.courseName = courseName
        self.sectionNumber = sectionNumber
        self.enrolledStudents = []

    def enroll(self, student):
        if student not in self.enrolledStudents:
            self.enrolledStudents.append(student)
            print(f"Student {student[0]} with UCID {student[1]} has been enrolled in {
                  self.courseName} section {self.sectionNumber}")
        else:
            print(f"Student {student[0]} with UCID {student[1]} is already enrolled in {
                  self.courseName} section {self.sectionNumber}")

    def drop(self, student):
        if student in self.enrolledStudents:
            self.enrolledStudents.remove(student)
            print(f"Student {student[0]} with UCID {student[1]} has been dropped from {
                  self.courseName} section {self.sectionNumber}")
        else:
            print(f"Student {student[0]} with UCID {student[1]} does not exist in {
                  self.courseName} section {self.sectionNumber}")


class Student:
       ''' Write a class definition line and a one line docstring for the class Student. Write an
  __init__ method for the class Student that gives each student its own name and ucid. Make sure that
  you test this on a successful creation of a student object '''

       def __init__(self, name, ucid):
            self.name = name
            self.ucid = ucid
            self.transcript = {}

        def grade_obtained(self, course, grade):
            self.transcript[course] = grade
            print(f"Student {self.name} with UCID {
                  self.ucid} has obtained a grade of {grade} in {course}")

        def viewGrade(self, courseName):
            if courseName in self.transcript:
                print(f"{self.name}, your grade for {
                      courseName} is {self.transcript[courseName]}")
                return self.transcript[courseName]
            else:
                print(f"{self.name}, you have not taken {courseName}")
                return None
