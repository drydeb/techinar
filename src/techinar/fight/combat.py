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


f1 = Fighter(name="Joe", health=10, defense=4, power=5, damage=3)
f2 = Fighter(name="Frank", health=11, defense=5, power=4, damage=2)

print(f"{f1.name} vs {f2.name}")
round = 1

while f1.alive() and f2.alive():
    print(f"\nRound {round}")
    f1.print_status()
    f2.print_status()
    answer = input(f"Should {f1.name} attack? (Y or N) ")
    if answer.lower() == "y":
        f1.attack(f2)
    if f2.alive():
        answer = input(f"Should {f2.name} attack? (Y or N) ")
        if answer.lower() == "y":
            f2.attack(f1)
    round += 1

print("Fight over.")
