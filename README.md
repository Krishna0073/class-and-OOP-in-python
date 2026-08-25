Student Report Card — Python OOP

A beginner-friendly Python program that demonstrates Object-Oriented Programming (OOP) concepts by creating a Student class and managing student details using methods and private attributes.

Features
Create a Student class
Store student name and age
Use private variables for group and report
Assign default values to private variables
Update student details using a setter method
Display student information using a getter method
Demonstrate encapsulation
Concepts Used
Classes and Objects
__init__() Constructor
Instance Variables
Private Attributes
Methods
Encapsulation
Getters and Setters
User Input
Default Values

The program initially assigns:

Group  → ECE
Report → fail

These values can later be updated using setDetails().

Program Flow
User Input
    ↓
Create Student Object
    ↓
__init__() stores name and age
    ↓
Private variables get default values
    ↓
setDetails() updates group and report
    ↓
getDetails() displays student information
Example Input
name: Krishna
age: 20
group: CSE
report: Pass
Example Output
Student Report Card
Krishna
20
CSE
Pass
OOP Structure
Student

The Student class represents a student and contains their personal and academic information.

__init__()

The constructor initializes:

self.name
self.age
self.__group
self.__report
setDetails()

Updates the private attributes:

self.__group = group
self.__report = report
getDetails()

Displays the stored student information.

Learning Outcomes

This project helps understand:

How to define and use classes
How objects store data
How constructors initialize objects
How private attributes work in Python
How encapsulation protects object data
How getter and setter methods are used
Author

Krishna Sharma

B.Tech Computer Science & Engineering (AI & ML)

Lovely Professional University
