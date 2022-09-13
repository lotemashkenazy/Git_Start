import datetime

books= 18
notebooks= 23
pens= 9

user_books= int(input("enter number of books:"))
user_notebooks= int(input("enter number of notebooks:"))
user_pens= int(input("enter number of pens:"))

books= books-user_books
notebooks= notebooks-user_notebooks
pens= pens-user_pens

x = datetime.datetime.now()
print("the update stock after the purchase that made on " , x , "is:")
print("books: " , books)
print("notebooks: " , notebooks)
print("pens: " , pens)

books+=4
notebooks+=2
pens+=5

print("enter the date of purchase: ")
year1= int(input("year:"))
month1= int(input("month:"))
day1= int(input("day:"))

user_books= int(input("enter the number of books:"))
user_notebooks= int(input("enter the number of notebooks:"))
user_pens= int(input("enter the number of pens:"))

books= books-user_books
notebooks= notebooks-user_notebooks
pens= pens-user_pens

print("enter the date of purchase: ")
year2= int(input("year:"))
month2= int(input("month:"))
day2= int(input("day:"))

user_books= int(input("enter the number of books:"))
user_notebooks= int(input("enter the number of notebooks:"))
user_pens= int(input("enter the number of pens:"))

books= books-user_books
notebooks= notebooks-user_notebooks
pens= pens-user_pens

print("the update stock after the purchase that made on " , x , "is:")
print("books: " , books)
print("notebooks: " , notebooks)
print("pens: " , pens)

d1 = datetime.datetime(year1, month1, day1)
d2 = datetime.datetime(year2, month2, day2)
if d1 > d2:
    print("d1 is greater than d2")
elif d1 < d2:
    print("d2 is greater than d1")
elif d1 == d2:
    print("d1 is equal to d2")