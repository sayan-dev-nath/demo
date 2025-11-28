# Built-in Datetype
# -----------------
# 1. none type


# 2. number type(int, float, complex)
# y = 10
# print(y, type(y))
# price = 25.56
# value = 5.1e5
# print(type(price))
# print(type(value))
# com = 5 + 7j
# print(com, type(com))


# 3. bool type


# 4. sequence type(string, list, tuple, range)
str = "geekyshows"
print(str, type(str))

data = [10, 5.6, "geekyshows"]  # mutable
print(data, type(data))

data = (10, 5.6, "geekyshows")
print(data, type(data))  # immutable

rg = range(5)
print(rg, type(rg))
rg = range(10, 20, 2)
print(rg, type(rg))

# 5. set type
data = {10, 20, 10, 30, 40, "geekyshows"}
print(data, type(data))

# 6. mapping type/dict/dictionary
data = {
    101: "Rahul",
    102: "Sonam",
    103: "Raj",
}
print(data, type(data))
# TODO Declaring & initializing variable

a = b = c = d = 10
print(a, b, c, d)

a, b, c, d = 10, 10.25, "geekyshows", True
print(a, b, c, d)
# TODO operators

# arithmetic operators
print(
    (4 + 2),
    (4 - 2),
    (4 * 2),
    (4 / 2),
    (5 % 2),
    (5**2),
    (5 // 2),
    (-5 // 2),
)

# relational/comparison operators
print(
    (5 < 2),
    (5 > 2),
    (5 <= 2),
    (5 >= 2),
    (5 == 2),
    (5 != 2),
)

# logical operators
print(
    ((5 < 2) and (5 > 3)),
    ((5 < 2) or (5 > 3)),
    (not (5 < 2)),
)

# assignment operator
y = 10 + 20
print(y)

m = 15
m += 10
print(m)

m = 15
m -= 10
print(m)

m = 15
m *= 10
print(m)

m = 15
m /= 10
print(m)

m = 15
m %= 10
print(m)

m = 15
m **= 2
print(m)

m = 15
m //= 10
print(m)

# bitwise operators
a = 10
b = 15

print("~a = ", ~a)  # not a
print("a & b = ", a & b)  # a and b
print("a | b = ", a | b)  # a or b
print("a ^ b = ", a ^ b)  # a xor b
print("a << 2 = ", a << 2)  # a left shift b
print("a >> 2 = ", a >> 2)  # a right shift b


# membership operators(in, not in)
str = "welcome to geekyshows"
print("to" in str)

str = "welcome top geekyshows"
print("to" in str)

str = "welcome top geekyshows"
print("to" not in str)

str = "welcome to geekyshows"
print("subs" in str)

str = "welcome to geekyshows"
print("subs" not in str)


# identity operators(is, is not)
a = 10
b = 10
print(a is b)
a = 10
b = "10"
print(a is b)
a = 10
b = 10
print(a is not b)
a = 10
b = "10"
print(a is not b)
# Operator Precedence and Associativity

value = (1 + 1) * 2**4 // 3 + 4 - 1
print(value)


# Type Conversion

# implicit type conversion
a = 5
b = 2
value = a / b
print(value, type(value))

# explicit type conversion
n = 5.5
int(n), float(n), complex(n), str(n), list(n), tuple(n), bin(n), oct(n), hex(n)
# If-statement, Nested if-statement, Indentation, if-else-statement
"""
if (condition):
    statement1
    statement2
    if (condition):
        statement1
        statement2
elif (condition1 and condition2):
    statement1
    statement2
else:
    statement1
    statement2
"""
# a = int(input("Enter an integer :: "))
# if a > 5:
#     print("Greater")
#     print("Hello World")

# if (5 > 2) and (7 > 3):
#     print("if statement with logical operator")
# print("Rest of the code")


# while-loop, while-else-loop, nested while-loop
""" 

while (condition):
    statement

while (condition):
    statement
else:
    statement

while (condition):
    statement
    while (condition):
        statement

"""


# range() function
# range(start, stop, stepsize)


# for-loop
""" 

for var in sequence:
    statement

for var in sequence:
    statement
    for var in sequence:
        statement

for var in sequence:
    statement
else:
    statement

"""

# str = "geekyshows"
# for ch in str:
#     print(ch, end=" ")
# print()

# print(len(str))

# for i in range(10):
#     print(i, end=" ")
# print()


# break, continue & pass statement


# array
""" 
import array
array_name = array.array('type_code', [elements])
from array import *
array_name = array('type_code', [elements])
"""
# from array import array

""" 
stu_roll = array("i", [1, 2, 3, 4, 5])
stu_roll = array("f", [1.0, 2.0, 3.0, 4.0, 5.0])
stu_roll.append(6.0)
stu_roll.append(7.0)

for i in stu_roll:
    print(i, end=" ")
print()
print(len(stu_roll)) 

"""
# roll = array("i", [])
# n = int(input("Enter number of elements :: "))
# for i in range(n):
#     roll.append(int(input()))

# roll = array("i", [1, 2, 3, 4, 5, 5, 6])
# roll1 = array("i", [7, 8, 9, 10])
# roll.insert(0, 0)
# roll.pop()
# roll.pop(0)
# roll.remove(5)
# print(roll.index(1))
# roll.reverse()
# roll.extend(roll1)

# for e in roll:
#     print(e, end=" ")
# print()

# Slicing on Arrays
# newArrayName = arrayName[start:stop:stepsize]
# a = roll[:5]
# for i in a:
#     print(i)

# About pip
# About numpy
# one dimensional array
# two dimensional array
# array_name = numpy.array([elements])
# print(roll.dtype)
# print(roll)
