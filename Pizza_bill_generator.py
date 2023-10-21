size = input("what size of pizza do u want? ")
bill = 0
if size == 'S' or size == 's':
    bill += 100
    print("Small pizza price is 100")
elif size == 'M' or size == 'm':
    bill += 200
    print("Medium pizza cost is 200")
elif size == 'L' or size == 'l':
    bill += 300
    print("Large pizza cost is 300")
add_pepperoni = input("Do you want pepperoni (Y/N)")
if add_pepperoni == 'Y' or add_pepperoni == 'y':
    if size == 'S' or size == 's':
        bill += 30
    else:
        bill += 50
extra_cheese = input("Do you want extra cheese? (Y/N)")
if extra_cheese == 'Y' or extra_cheese == 'y':
    bill += 20
print(f"Your final bill is {bill}.")

