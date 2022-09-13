import math

#
x= float(input("enter number-"))
print(math.floor(x))

#
x= float(input("enter number-"))
print(math.pow(x,0.5))

#
x=int(input("enter number-"))
y=int(input("enter number-"))
print(math.pow(x,y))

#
x=int(input("enter number-"))
print(math.exp(x))

#
x=int(input("enter number-"))
num1= 3*math.atan(x)
num2= (math.acos(x))**2
print(num1-num2)