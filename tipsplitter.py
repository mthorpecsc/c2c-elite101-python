def tip_splitter(bill, percentage, group_size):
    print("You got to the tip splitter")

    tip = bill * (percentage * 0.01) #times it by 0.01 to make it a percent
    print(f"Tip: {tip:.2f}") #:.2f is used to round it 2 decimal places
    total_bill = tip + bill #combine the tip amount and bill to get the total bill
    print(f"Total Bill: {total_bill:.2f}")
    per_person = total_bill / group_size #divide the total by the group size to get the amount per person
    print(f"Per Person: {per_person:.2f}")


def main():
    print("Welcome to the TIP SPLITTER Program! Easily split a bill amongst friends!")
    while True:
        try:
            bill = float(input("Enter the Bill Amount: ")) #a float for cents
            if bill < 1: #bill must cost something
                print("Please enter an integer above 0.")
                print("-"*15)
            else:
                break
        except ValueError: #edgecase for unexpected inputs
            print("Please enter an integer above 0.")
            print("-"*15)
    while True:
        try:
            percentage = float(input("Enter the tip percentage: "))
            if percentage <0:
                print("Please enter a positive integer or 0.")
                print("-"*15)
            else:
                break
        except ValueError:
            print("Please enter a positive integer or 0.")
            print("-"*15)

    while True:
        try:
            group_size = int(input("Enter the group size: "))
            if group_size < 1:
                print("Minimum size must be 1. No decimals.")
                print("-"*15)
            else:
                break
        except ValueError:
            print("Minimum size must be 1. No decimals.")
            print("-"*15)

    tip_splitter(bill, percentage, group_size)

main()
