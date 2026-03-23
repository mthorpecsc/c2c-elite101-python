#interest calculator

principle = 0
rate = 0
time = 0
while principle <= 0:
    principle = float(input("Type in your principal: ").strip())
    if principle <= 0:
        print("Your principle can not be less or equal to zero")

while rate <= 0:
    rate = float(input("Type in your interest rate: ").strip())
    if rate <= 0:
        print("Your interest rate can not be less or equal to zero")

while time <= 0:
    time = float(input("Type in the amount of years: ").strip())
    if time <= 0:
        print("The amount of years can not be less or equal to zero")

total = principle*pow((1.0 + rate/100), time)
print(f"Your balance would be ${total:,.2f} after {time} year(s)!")
