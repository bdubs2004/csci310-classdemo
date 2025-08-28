"""
demo_script.py
====================================
Demonstration of basic Python concepts like math, bools, strings, and etc.

| Author: Bryce Kwiecinski
| Date: 2025 August 28
"""
#Math
print(1+5*2)
print((1+5)*3)
print(1**12)
print(27/9)
print(83/9)
print(83//9)
print(83%9)
print(10/5)
print(5//10)
print(5%10)
print(4**2)

#Bool Statements
print("5==5")
print("10<3")
print("7>=2")
print("4!= 4")
#Lists
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
A = [my_list] * 3   
B = my_list * 3     
my_list[6] = 45     
print("A =", A)
print("B =", B)
print("Modified list =", my_list)
#Strings
string1 = "Hello"
print(string1.upper())
print(string1.lower())
print("string1 =", string1)
print( string1 * 3)
print(string1[0])
print( string1[1:4])

#variables
x = 10
y = 3
z = x + y
print("x =", x, "y =", y, "z =", z)

x = x * 2
print("New value of x:", x)

# Swapping variables
a, b = 5, 7
print("Before swap: a =", a, "b =", b)
a, b = b, a
print("After swap: a =", a, "b =", b)
#Inputs
print("Before swap: a =", a, "b =", b)
a, b = b, a
print("After swap: a =", a, "b =", b)
num2 = float(input("Enter a decimal number: "))
print("Square of your number is:", num2 ** 2)
#If/Else
x = 5
if x == 5:
    print("x is exactly 5")
else:
    print("x is not 5")
if y > 10:
    print("y is greater than 10")
else:
    print("y is 10 or less")
#Dictionaries, Sets, and Tuples
#Dictionaries
student_grades = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 92
}
#Sets
print("Alice's grade:", student_grades["Alice"])
student_grades["Bob"] = 88  
print("Updated dictionary:", student_grades)

fruits = {"apple", "banana", "cherry", "apple"}
print("Set contents (no duplicates):", fruits)

fruits.add("orange")
fruits.remove("banana")
print("Updated set:", fruits)
#Tuples
point = (3, 4)
print("Point coordinates:", point)
print("X value:", point[0])
print("Y value:", point[1])

(x, y) = point
print("Unpacked X:", x)
print("Unpacked Y:", y)

if __name__ == "__main__":
    """
    I figure I have to put something here
    """