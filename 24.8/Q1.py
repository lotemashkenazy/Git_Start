sum = float(input("enter sum:"))
stock1 = 10
stock2 = 15

if sum >= 50000 and (sum%stock1==0 or sum%stock2==0):
    print("Rock on!")
else:
    print("can't Invest!")