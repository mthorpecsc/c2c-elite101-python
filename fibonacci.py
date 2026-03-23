# testing
"""
x = range(10)
count = 0
for n in x:
    print(n)
    count+= n
    print(count)

    """
"""
list = [1, 2, 3, 4, 5]
first_n = list.index(3)-1
second_n = list.index(3)-2

add_1 = list[first_n]
add_2 = list[second_n]

print(add_1 + add_2)

"""
def fibonacci_sequence():
    print("Welcome to Finobacci Sequence Generator!")
    list = [0,1]

    while True:
        try:
            range = int(input("How long do you want your sequence to be?: "))
            if range >= 0:
                break
            else:
                print("Please enter a positive integer.")
                print()
        except ValueError:
            print("Please enter a valid, positive integer.")
            print()

    if range == 1:
        list = [0]

    elif range == 2:
        list = list

    elif range == 0:
        list = []
        print("Enjoy your empty list!")

    while len(list) < range:
        num_1 = list[-1]
        num_2 = list[-2]

        total = num_1 + num_2
        list.append(total)

    print(list)

fibonacci_sequence()
