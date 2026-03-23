#class variable practice

class Worker:
    #class variables shared among all objects
    company_name = "Thieve's Rest"
    boss = "Slingshot"
    num_employees = 0

    def __init__(self,name, role,age):
        self.name = name
        self.role = role
        self.age = age
        Worker.num_employees +=1 #every time a new worker is created, the num of employees increases by 1

worker1 = Worker("Vinestaff", "Front of House", 23)
worker2 = Worker("Shuriken", "Delivery", 21)

#print(f"{worker1.name} is {worker1.role} and is {worker1.age} years old.")
#print(f"{worker2.name} is {worker2.role} and is {worker2.age} years old.")
#print(f"There are currently {Worker.num_employees} workers employed at {Worker.boss}'s cafe, {Worker.company_name}.")

#inherability practice

#parent class
class Inphernal():
    def __init__(self, name, region): #attributes
        self.name = name
        self.is_alive = True
        self.region = region
    #methods
    def spawn(self):
        print(f"{self.name} is spawning into {self.region}!")

    def eat(self):
        print(f"{self.name} is eating some food!")

    def attack(self):
        print(f"{self.name} has attacked!")
#child classes
class Skateboard(Inphernal):
    def catchphrase(self):
        print("Watch this trick!")

class Slingshot(Inphernal):
    def catchphrase(self):
        print("Can't catch me!")

class Shuriken(Inphernal):
    def catchphrase(self):
        print("It's time to pick up the pace!")

skateboard = Skateboard("Skateboard","Playground")
slingshot = Slingshot("Slingshot","Crossroads")
shuriken = Shuriken("Shuriken","Thieves Den")

#print(skateboard.name, skateboard.is_alive, skateboard.region)
#skateboard.catchphrase()
#slingshot.catchphrase()
#shuriken.catchphrase()

