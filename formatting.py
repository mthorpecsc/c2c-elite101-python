
name1 = "Foxi"
name2 = "Mecha"
name3 = "Fish"

print(f"Hello! {name1:>10}") #rightaligned
print(f"Hello! {name2:<10}") #left aligned
print(f"Hello! {name3:^10}") #centered

number1 = 2763.1029
number2 = 36.09
number3 = -512

print(f"{number1:+,.3f}")
print(f"{number2:+,.2f}")
print(f"{number3:+,.1f}")
