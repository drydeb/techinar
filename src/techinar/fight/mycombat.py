from random import randint
class Fighter:
    """This class represents a generic fighter character."""

    def __init__(self, name, health, defense, power, damage):
        """Initialize the fighter with the given attributes."""
        self.name = name
        self.health = health
        self.defense = defense
        self.power = power
        self.damage = damage


    def alive(self):
        """Determine if the fighter is alive."""

        return self.health > 0


    def attack(self, opponent):
        """Have the fighter attack an opponent."""

        roll = randint(1, 20)
        if roll + self.power - opponent.defense > 12:
            print(f"{self.name} hits {opponent.name} for {self.damage} points")
            opponent.wound(self.damage)
            if not opponent.alive():
                print(f"{self.name} won!")
        else:
            print(f"{self.name} missed.")


    def wound(self, amount):
        """Apply damage to the fighter."""

        self.health -= amount
        if not self.alive():
            print(f"{self.name} died.")


    def print_status(self):
        """Print the current status of the fighter."""
        print(f"{self.name} has {self.health} health.")

class Knight:
    """This class represents a generic knight character."""

    def __init__(self, name, health, defense, power, damage, energ):
        """Initialize the knight with the given attributes."""
        self.name = name
        self.health = health
        self.defense = defense
        self.power = power
        self.damage = damage
        self.energ=energ


    def alive(self):
        """Determine if the knight is alive."""

        return self.health > 0

    def energy(self):
        self.energy+=1
    def attack(self, opponent):
        """Have the knight attack an opponent."""

        roll = randint(1, 20)
        if roll == 20:
            print(f"{self.name} fatally wounded {opponent.name} for {self.damage*5} points")
            opponent.wound(self.damage*5)
        elif roll + self.power - opponent.defense > 12:
            text=randint(1,5)
            if text==5:
                print(f"{self.name} slashed {opponent.name} dealing {self.damage*roll/10} damage")
            elif text==4:
                print(f"{self.name} threw their shield towards {opponent.name} dealing {self.damage*roll/10} damage")
            elif text==3:
                print(f"{self.name} appeared behind {opponent.name} dealing {self.damage*roll/10} damage")
            if text==2:
                print(f"{self.name} landed a hit on {opponent.name} dealing {self.damage*roll/10} damage")
            if text==1:
                print(f"{self.name} hits {opponent.name} for {self.damage*roll/10} points")
            opponent.wound(self.damage*roll/10)
            if not opponent.alive():
                print(f"{self.name} won!")
        else:
            print(f"{self.name} missed.")
    def lunge(self,opponent):
        roll=randint(1,20)
        print(f"{self.name} swiftly lunged forward going past {opponent.name} dealing {self.damage*2.5}")
        opponent.wound(self.damage*2.5)
        if not opponent.alive():
            print(f"{self.name} won!")
    def wound(self, amount):
        """Apply damage to the knight."""

        self.health -= amount
        if not self.alive():
            print(f"{self.name} died.")


    def print_status(self):
        """Print the current status of the knight."""
        print(f"{self.name} has {self.health} health.")

class Alchemist:
    """This class represents a generic fighter character."""

    def __init__(self, name, health, defense, power, damage,potency):
        """Initialize the fighter with the given attributes."""
        self.name = name
        self.health = health
        self.defense = defense
        self.power = power
        self.damage = damage
        self.potency=potency


    def alive(self):
        """Determine if the fighter is alive."""

        return self.health > 0
    def heal(self):
        roll=randint(1,20)
        self.health+=self.potency*roll/10
        print(f"{self.name} heals for {self.potency*roll/10} points to {self.health}")
    def brew(self):
        roll=randint(10, 20)/10
        self.potency+=roll
        print(f"potency increased to {self.potency}")

    def poison(self, opponent):
        """Have the fighter attack an opponent."""

        roll = randint(1, 20)
        if roll + self.power - opponent.defense > 12:
            print(f"{self.name} hits {opponent.name} for {self.potency*roll/2} points")
            opponent.wound(self.potency*roll/2)
            if not opponent.alive():
                print(f"{self.name} won!")
        else:
            print(f"{self.name} missed.")


    def wound(self, amount):
        """Apply damage to the fighter."""

        self.health -= amount
        if not self.alive():
            print(f"{self.name} died.")


    def print_status(self):
        """Print the current status of the fighter."""
        print(f"{self.name} has {self.health} health.")

f3 = Fighter(name="Joe", health=10, defense=4, power=5, damage=3)
f2 = Knight(name="Frank", health=11, defense=8, power=4, damage=2, energy=0)
f1= Alchemist(name="Bob", health=10, defense=4, power=5, damage=3, potency=1)

print(f"{f1.name} vs {f2.name}")
round = 1

while f1.alive() and f2.alive():
    print(f"\nRound {round}")
    f1.print_status()
    f2.print_status()
    if f1.alive():
        answer = input(f"What should {f1.name} do? (Brew, Heal, Poison) ")
        if answer.lower() == "brew":
            f1.brew()
        elif answer.lower()=="heal":
            f1.heal()
        elif answer.lower()=="poison":
            f1.poison(f2)
    if f2.alive():
        answer = input(f"What should {f2.name} do? (Attack, Conserve, Lunge[2 energy]) ")
        if answer.lower() == "attack":
            f2.attack(f1)
        elif answer.lower()=="conserve":
            f2.energ()
        elif answer.lower()=="lunge" or answer.lower()=="lunge[2 energy]":
            f2.lunge(f1)
    round += 1

print("Fight over.")
