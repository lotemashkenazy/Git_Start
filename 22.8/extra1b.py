print("enter a")
a= int(input())
print("enter b")
b= int(input())
print("enter c")
c= int(input())
num1= (b**2 - 4*a*c)**0.5
num2= num1/(2*a)
num3= -b/(2*a)
solution1= num3+num2
solution2= num3-num2
print("x1=" , solution1 , " , " , "x2=" , solution2)