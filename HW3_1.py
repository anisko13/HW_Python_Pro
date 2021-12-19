x = input('Print price of product ')
try:
    x = int(x)
except ValueError:
    print("You must print a number ")

if x <= 0:
    raise ValueError("")