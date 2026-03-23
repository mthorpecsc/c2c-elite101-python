import string
no_punct = str.maketrans('','', string.punctuation)

def pick_a_shape():
    print("I can calculate the area of a shape for you. Which shape do you want me to calculate the area of?")
    print("_"*15)
    while True:
        shape = input("Enter your shape (circle, rectangle, square, triangle): ").strip().lower().translate(no_punct)
        if shape in ['circle', 'rectangle', 'square', 'triangle']:
            if shape == 'circle':
                circle()
                break
            if shape == 'rectangle':
                rectangle()
                break
            if shape == 'square':
                square()
                break
            if shape == 'triangle':
                triangle()
                break
        else:
            print('_'*20)
            print("The available shapes are *circle, rectangle, square, and triangle* ")
            print('_'*20)

def circle():
    while True: #loops the program so users can try again
        try: #used a float for decimal inputs
            radius = float(input("Enter the radius of the circle: "))
            area = float(radius * radius)
            print(f"The area of the circle is *{area}𝝅*")
            break
        except ValueError: #edgecases of unexpected inputs
            print("Please enter numbers only.")
            print("_"*15)

def rectangle():
    while True:
        try:
            width = float(input("Enter the width of the rectangle: "))
            break
        except ValueError:
            print("Please enter numbers only.")
            print("_"*15)

    while True:
        try:
            length = float(input("Enter the length of the rectangle: "))
            break
        except ValueError:
            print("Please enter numbers only. ")
            print("_"*15)

    area = float(width * length)
    print(f"The area of the rectangle is *{area}*")

def square():
    while True:
        try:
            side = float(input("Enter the value of one side of the square: "))
            area = float(side * side)
            print(f"The area of the square is *{area}*")
            break
        except ValueError:
            print(f"Please enter numbers only")
            print("_"*15)

def triangle():
    while True:
        try:
            base = float(input("Enter in the base: "))
            break
        except ValueError:
            print("Please type in numbers only.")
            print("_"*15)
    while True:
        try:
            height = float(input("Enter in the height: "))
            break
        except ValueError:
            print("Please type in numbers only.")
            print("_"*15)
    area = float(1/2 *(base * height))
    print(f"The area of the triangle is *{area}*")

pick_a_shape()

