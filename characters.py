from __future__ import annotations
from stdout_coloring import RED, RESET, PURPLE, YELLOW, BRIGHT_GREEN, CYAN, WHITE
import random


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

        # Check for block from opponent and make sure to reset it
        if opponent.block_next:
            opponent.block_next = False
            print(f"{PURPLE}{opponent.name} blocks {self.name}'s attack!{RESET}")

        # if no block then carry out
        else:
            opponent.health -= self.roll_attack_power(self.attack_power)
            print()
            print(
                f"{YELLOW}{self.name} ATTACKS {opponent.name} for {self.attack_power} damage!{RESET}"
            )
            print()

    def block(self):
        """Cancel out the next attack from opponent"""

        self.block_next = True
        print(f"{CYAN}{self.name} prepares to block the next attack!{RESET}")
        print()

    def heal(self, healing_power: int = None):
        """Increase health of character by a set amount or 5 if not given"""

        if healing_power is None:
            healing_power = 5
        if self.health + healing_power > self.max_health:
            self.health = self.max_health
        else:
            self.health += healing_power

        print()
        print(f"{CYAN}{self.name} HEALS for {WHITE}{healing_power}{RESET} hp")
        print()

    def custom_power_attack(self, opponent: Character, custom_attack_power: int):
        """Do an attack on an opponent with a set amount of attack_power"""
        if opponent.block_next:
            opponent.block_next = False
            print()
            print(f"{PURPLE}{opponent.name} blocks {self.name}'s attack!{RESET}")
        else:
            opponent.health -= self.roll_attack_power(custom_attack_power)
            print(
                f"{CYAN}{self.name} ATTACKS {opponent.name} for {WHITE}{custom_attack_power}{WHITE} damage!{RESET}"
            )
            print()

    def perform_special(self, opponent: Character, special_name: str):
        """Act out all attributes of this character\'s chosing special ability"""

        # Error checking if this character doesn't have specials
        if (self.special_abilities is None) or (
            special_name not in self.special_abilities.keys()
        ):
            raise ValueError("This character has no special abilities!")

        chosen_special_ability: SpecialAbility = self.special_abilities[special_name]
        print(f"{PURPLE}{self.name} uses {special_name}!{RESET}")
        print()

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
            self.block()

    def display_stats(self):
        print(
            f"{BRIGHT_GREEN}{self.name}'s Stats - Health: {WHITE}{self.health}{BRIGHT_GREEN}/{WHITE}{self.max_health}{BRIGHT_GREEN} Attack Power: {WHITE}{self.attack_power}{RESET}"
        )
        print()

    # We use this to randomize the attack power to a certain extent for all attacks
    # to keep things interesting
    def roll_attack_power(self, attack_power):
        return random.randint(attack_power // 1.5, attack_power)


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
                # Both specials regen to satisfy project requirements
                "Evil Laugh": SpecialAbility(50, 5, False),
                "Evil Smile": SpecialAbility(25, 0, True),
            },
        )

    ### NOTE: We override here to satisfy requirement of all attacks doing regen for wizard ###
    def base_attack(self, opponent: Character):
        """Perform basic attack for this character, dealing base level of attack power"""

        opponent.health -= self.attack_power
        print(
            f"{YELLOW}{self.name} ATTACKS {opponent.name} for {self.attack_power} damage!{RESET}"
        )
        print()
        self.regenerate()

    ########################################################

    def regenerate(self):
        self.health += 5
        print(
            f"{PURPLE}{self.name} the evil wizard regenerates 5 health! Current health: {RESET}{self.health}"
        )
        print()


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
