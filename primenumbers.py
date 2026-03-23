from sympy import *
#a library that checks if a number is prime

def test_primality():

    print("Test for primality")
    n = int(input("Enter an integer: "))

    if n <=1: #if its negative, 0, or 1 then its automatically not prime
        print(f"{n} is not a prime number.")
    elif n % 2 == 0 and n!= 2: #if its even and not 2 then its not prime
        print(f"{n} is not a prime number.")
    else: #checks for other numbers to see if they're prime or not.
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                print(f"{n} is not a prime number.")
                break
        print(f"{n} is a prime number.")

    print_all_primes(n)


def print_all_primes(n):

    print(f"List of primes leading up to {n}: ")
    print("-"*15)
    count = 0
    while count <= n: #this makes sure we dont print numbers past n
        if isprime(count) == False: #if its not prime the count goes up by 1 and loop restarts
            count+= 1
            continue #skips printing non-prime numbers and goes back to the loop
        print(count) #if its prime it'll print the number and add to the count
        count+= 1

test_primality()
