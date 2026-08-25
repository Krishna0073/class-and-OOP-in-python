class Student:

    school = "ABC University"

    def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no

        self.__group = "ECE"
        self.__report = "Fail"
        self.__marks = []

    def setDetails(self, group, report):
        self.__group = group
        self.__report = report

    def getDetails(self):
        print("\n----- STUDENT DETAILS -----")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Group:", self.__group)
        print("Report:", self.__report)

    def addMarks(self, marks):
        if 0 <= marks <= 100:
            self.__marks.append(marks)
        else:
            print("Marks must be between 0 and 100.")

    def getMarks(self):
        return self.__marks

    def calculateAverage(self):
        if len(self.__marks) == 0:
            return 0

        return sum(self.__marks) / len(self.__marks)

    def calculateGrade(self):
        average = self.calculateAverage()

        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"

    def updateReport(self):
        average = self.calculateAverage()

        if average >= 40:
            self.__report = "Pass"
        else:
            self.__report = "Fail"

    def displayMarks(self):
        print("\n----- MARKS -----")
        print("Marks:", self.__marks)
        print("Average:", self.calculateAverage())
        print("Grade:", self.calculateGrade())

    def __str__(self):
        return f"{self.name} - Roll No: {self.roll_no}"


class GraduateStudent(Student):

    def __init__(self, name, age, roll_no, specialization):
        super().__init__(name, age, roll_no)
        self.specialization = specialization

    def getDetails(self):
        super().getDetails()
        print("Specialization:", self.specialization)


name = input("Enter name: ")
age = int(input("Enter age: "))
roll_no = int(input("Enter roll number: "))

group = input("Enter group: ")
report = input("Enter report: ")

s1 = Student(name, age, roll_no)

s1.setDetails(group, report)

print("\nEnter 5 subject marks:")

for i in range(5):
    marks = int(input(f"Subject {i + 1}: "))
    s1.addMarks(marks)

s1.updateReport()

s1.getDetails()
s1.displayMarks()

print("\nStudent Object:")
print(s1)

print("\nSchool:", Student.school)


print("\n----- GRADUATE STUDENT -----")

g1 = GraduateStudent(
    "Rahul",
    22,
    101,
    "Artificial Intelligence"
)

g1.addMarks(85)
g1.addMarks(90)
g1.addMarks(78)

g1.updateReport()
g1.getDetails()
g1.displayMarks()
