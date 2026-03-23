#oop practice

class Phighter:
    def __init__(self,gear,health,sheild,category,is_playable):
        self.gear = gear
        self.health = health
        self.sheild = sheild
        self.category = category
        self.is_playable = is_playable

    def pick(self):
        print(f"You picked {self.gear}!")

    def describe(self):
        print(f"This is {self.gear}, he has {self.health} health and {self.sheild} sheild. He's apart of the {self.category} class!")

    #specifically for phighter 1
    def primary(self):
        print("You used your slingshot!")

    def secondary(self):
        print("You used Heavy Hurler!")

    def ricochet(self):
        print("You used Scattershot!")

    def dash(self):
        print("You used Sidestep!")

    def ult(self):
        print("You activated Leg Day!")

phighter_1 = Phighter("Slingshot", 175, 100, "Ranged", True )

def ability():
    phighter_1.describe()
    phighter_1.pick()
    while True:
        use_ability = input("Which ability would you like to use? (primary, heavy hurler, scatter shot, sidestep, leg day): ").lower()
        if use_ability in ["primary", "heavy hurler", "scatter shot", "sidestep", "leg day"]:
            break
        else:
            print("Invalid ability. Please try again.")

    match use_ability:
        case "primary":
            phighter_1.primary()
        case "heavy hurler":
            phighter_1.secondary()
        case "scatter shot":
            phighter_1.ricochet()
        case "sidestep":
            phighter_1.dash()
        case "leg day":
            phighter_1.ult()

#ability()
