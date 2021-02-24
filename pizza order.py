print("Welcome to my pizza delivery program!")
size = input("What size of pizza do you want? S,M or L? ")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

pepper = input("Do you want to add Pepperoni? ")
if pepper == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
cheese = input("Do you want extra cheese? Y/N")
if cheese == "Y":
    bill += 1
print(f"Your final bill is £{bill}")