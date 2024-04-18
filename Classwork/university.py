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

    ''' Write a method enroll as part of the class Course_Section. The method enroll should add a
passed tuple parameter to enrolled_students only if the tuple does not exists already in the list. The first
item in the tuple is the name of the student and the second item is the ucid of the students. The enroll
method will print a message confirming the enrollment of the student if the tuple gets added to the list
otherwise it will print a message that the students is already enrolled'''

    def enroll(self, student):
        if student not in self.enrolledStudents:
            self.enrolledStudents.append(student)
            print(f"Student {student[0]} with UCID {student[1]} has been enrolled in {
                  self.courseName} section {self.sectionNumber}")
        else:
            print(f"Student {student[0]} with UCID {student[1]} is already enrolled in {
                  self.courseName} section {self.sectionNumber}")

    ''' Write a method drop as part of the class Course_Section. The method drop should check
whether a passed tuple (student name, ucid) is in the enrolled_students list or not. If the tuple exists in
the list then the method removes that tuple and prints that the student is successfully dropped otherwise
prints that the student does not exist'''

    def drop(self, student):
        if student in self.enrolledStudents:
            self.enrolledStudents.remove(student)
            print(f"Student {student[0]} with UCID {student[1]} has been dropped from {
                  self.courseName} section {self.sectionNumber}")
        else:
            print(f"Student {student[0]} with UCID {student[1]} does not exist in {
                  self.courseName} section {self.sectionNumber}")


'''
Write a class definition line and a one line docstring for the class Student. Write an
__init__ method for the class Student that gives each student its own name and ucid. Make sure that
you test this on a successful creation of a student object.
'''


class Student:
    ''' holds the student name and ucid for the object created'''

    def __init__(self, name, ucid):
        self.name = name
        self.ucid = ucid
