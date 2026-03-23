def main():
    print("Welcome to the Temperature Converter!")
    print("-"*30)


    while True:
        convert_from = input("Enter the temperature scale you wish to convert from (Celsius, Fahrenheit, Kelvin): ").strip().lower()

        if convert_from == 'celsius':
            celsius()
            break
        elif convert_from == 'fahrenheit':
            fahrenheit()
            break
        elif convert_from == 'kelvin':
            kelvin()
            break
        else:
            print(f"You can not convert from {convert_from}, please choose from Celsius, Fahrenheit, or Kelvin.")
            print("-"*50)


def celsius():
    print("-"*50)
    while True:
        convert_to = input("Enter the temperature scale you wish to convert to (Fahrenheit, Kelvin): ").strip().lower()
        if convert_to == 'fahrenheit':
            amount = float(input("Enter the temperature you wish to convert in Celsius: "))
            converted = amount * 9/5 + 32
            print(f"{amount} degrees in Celsius is equal to {converted} degrees in Fahrenheit.")
            break

        elif convert_to == 'kelvin':
            amount = float(input("Enter the temperature you wish to convert in Celsius: "))
            converted = amount + 273.15
            print(f"{amount} degrees in Celsius is equal to {converted} degrees in Kelvin.")
            break

        else:
            print(f"You can not convert to {convert_to}, please choose from Fahrenheit or Kelvin.")
            print("-"*50)


def fahrenheit():
    print("-"*50)
    while True:
        convert_to = input("Enter the temperature scale you wish to convert to (Celsius, Kelvin): ").strip().lower()

        if convert_to == 'celsius':
            amount = float(input("Enter the temperature you wish to convert in Fahrenheit: "))
            converted = (amount -32)*5/9
            print(f"{amount} degrees in Fahrenheit is equal to {converted} degrees in Celsius.")
            break

        elif convert_to == 'kelvin':
            amount = float(input("Enter the temperature you wish to convert in Fahrenheit: "))
            converted = ((amount -32 )/1.8) + 273.15
            print(f"{amount} degrees in Fahrenheit is equal to {converted} degrees in Kelvin.")
            break

        else:
            print(f"You can not convert to {convert_to}, please choose from Celsius or Kelvin.")
            print("-"*50)


def kelvin():
    print("-"*50)
    while True:
        convert_to = input("Enter the temperature scale you wish to convert to (Celsius, Fahrenheit): ").strip().lower()

        if convert_to == 'celsius':
            amount = float(input("Enter the temperature you wish to convert in Kelvin: "))
            converted = amount - 273.15
            print(f"{amount} degrees in Kelvin is equal to {converted} degrees in Celsius.")
            break

        elif convert_to == 'fahrenheit':
            amount = float(input("Enter the temperature you wish to convert in Kelvin: "))
            converted = ((amount -273.15) * 9/5) + 32
            print(f"{amount} degrees in Kelvin is equal to {converted} degrees in Fahrenheit.")
            break

        else:
            print(f"You can not convert to {convert_to}, please choose from Celsius or Fahrenheit.")
            print("-"*50)


main()
