from __future__ import annotations


# Base Character class
class Character:
    def __init__(self, name, health, attack_power, special_abilities=None):
        self.name: str = name
        self.health: int = health
        self.attack_power: int = attack_power
        self.max_health: int = health
        self.block_next: bool = False
        self.special_abilities: dict = special_abilities

    def base_attack(self, opponent: Character):
        """Perform basic attack for this character, dealing base level of attack power"""

        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def block(self):
        """Cancel out the next attack from opponent"""

        self.block_next = True
        print(f"{self.name} prepares to block the next attack!")

    def heal(self, healing_power: int = None):
        """Increase health of character by a set amount or 5 if not given"""

        if healing_power is None:
            healing_power = 5
        if self.health + healing_power > self.max_health:
            self.health = self.max_health
        else:
            self.health += healing_power
        print(f"{self.name} heals for {healing_power} hp -> now {self.health}hp")

    def custom_power_attack(self, opponent: Character, custom_attack_power: int):
        """Do an attack on an opponent with a set amount of attack_power"""

        opponent.health -= custom_attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def perform_special(self, opponent: Character, special_name: str):
        """Act out all attributes of this character\'s chosing special ability"""

        # Error checking if this character doesn't have specials
        if (self.special_abilities is None) or (
            special_name not in self.special_abilities.keys()
        ):
            raise ValueError("This character has no special abilities!")

        chosen_special_ability: SpecialAbility = self.special_abilities[special_name]

        # attack component
        if chosen_special_ability.attack_power != 0:
            custom_attack_power = chosen_special_ability.attack_power
            self.custom_power_attack(opponent, custom_attack_power)

        # healing component
        if chosen_special_ability.healing_power != 0:
            custom_healing_power = chosen_special_ability.healing_power
            self.heal(custom_healing_power)

        # blocking component
        if chosen_special_ability.blocking:
            self.block_next = True

    def display_stats(self):
        print(
            f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}"
        )


class SpecialAbility:
    def __init__(
        self, attack_power: int = 0, healing_power: int = 0, blocking: bool = False
    ):
        self.attack_power = attack_power
        self.healing_power = healing_power
        self.blocking = blocking


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(
            name,
            health=140,
            attack_power=25,
            special_abilities={
                "Big Sword Swing": SpecialAbility(50, 0, False),
                "Angel's Blessing": SpecialAbility(0, 25, True),
            },
        )


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(
            name,
            health=100,
            attack_power=35,
            special_abilities={
                "Fireball": SpecialAbility(50, 0, False),
                "Arcane Forcefield": SpecialAbility(0, 0, True),
            },
        )


# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(
            name,
            health=150,
            attack_power=15,
            special_abilities={
                "Evil Laugh": SpecialAbility(50, 0, False),
                "Evil Smile": SpecialAbility(0, 0, True),
            },
        )

    def regenerate(self):
        self.heal(5)
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")


# Create Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(
            name,
            health=75,
            attack_power=50,
            special_abilities={
                "Flaming Arrow": SpecialAbility(50, 0, False),
                "Archer Shield": SpecialAbility(0, 0, True),
            },
        )


# Create Paladin class
class Paladin(Character):
    def __init__(self, name):
        super().__init__(
            name,
            health=150,
            attack_power=30,
            special_abilities={
                "Holy Strike": SpecialAbility(50, 0, False),
                "Hero's Touch": SpecialAbility(0, 25, False),
            },
        )
