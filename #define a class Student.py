class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__group = "ECE"
        self.__report = "fail"

    def setDetails(self, group, report):
        self.__group = group
        self.__report = report

    def getDetails(self):
        print(self.name)
        print(self.age)
        print(self.__group)
        print(self.__report)


name = input("name: ")
age = int(input("age: "))
group = input("group: ")
report = input("report: ")

print("Student Report Card")

s1 = Student(name, age)

s1.setDetails(group, report)

s1.getDetails()
