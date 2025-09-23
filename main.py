# We use this to allow type hinting before finishing declarations
from __future__ import annotations
from characters import (
    Archer,
    Mage,
    Paladin,
    Warrior,
    EvilWizard,
    Character,
)
from input_utils import wait_for_enter
from stdout_coloring import RESET, YELLOW, BRIGHT_RED, GREEN, RED
import random
import time


class GamePlay:
    def __init__(self, player: Character, enemy: Character):
        self.player = player
        self.enemy = enemy

    @staticmethod
    def prompt_user_to_create_character(enemy: bool = False) -> Character:
        if enemy:
            print(f"{YELLOW}Choose enemy's character class: {RESET}")
        else:
            print(f"{YELLOW}Choose your character class: {RESET}")
        print("1. Warrior")
        print("2. Mage")
        print("3. Archer")
        print("4. Paladin")
        if enemy:
            print("5. Evil Wizard")

        class_choice = input(f"{YELLOW}Enter the number of your class choice: {RESET}")

        if enemy:
            name = input(f"{YELLOW}Enter your enemy's name: {RESET}")
        else:
            name = input(f"{YELLOW}Enter your character's name: {RESET}")

        print(f"{YELLOW}------------------------------ {RESET}")

        if class_choice == "1":
            return Warrior(name)
        elif class_choice == "2":
            return Mage(name)
        elif class_choice == "3":
            return Archer(name)
        elif class_choice == "4":
            return Paladin(name)
        elif enemy and class_choice == "5":
            return EvilWizard(name)
        else:
            print(f"{BRIGHT_RED}Invalid choice. Defaulting to Warrior.{BRIGHT_RED}")
            print()
            return Warrior(name)

    def battle(self):
        while self.player.health > 0 and self.enemy.health > 0:
            self.player_turn()
            if self.enemy.health <= 0:
                return self.player  # battle ends, player wins
            self.enemy_turn()
            if self.player.health <= 0:
                return self.enemy  # battle ends, enemy wins

    def player_turn(self):
        """Collect player move decision and play it out"""

        while True:
            print(f"{GREEN}\n--- Your Turn ---{RESET}")
            print("1. Basic Attack")
            print("2. Use Special Ability")
            print("3. Heal")
            print("4. View Stats")

            choice = input(f"{GREEN}Choose an action: {RESET}")

            match choice:
                case "1":
                    self.player.base_attack(self.enemy)
                case "2":
                    special_ability_choice = self.record_special_ability_choice(
                        self.player
                    )
                    self.player.perform_special(self.enemy, special_ability_choice)
                case "3":
                    self.player.heal(5)
                case "4":
                    self.player.display_stats()
                    wait_for_enter()
                    continue
                case _:
                    print(
                        f"{BRIGHT_RED}Invalid selection made for turn choice. Try again.{RESET}"
                    )
                    wait_for_enter()
                    continue

            return

    def enemy_turn(self):
        print(f"{RED}\n--- Enemy's Turn ---{RESET}")

        # Simulate computer making a choice
        picking_move_text = f"{RED}Enemy is picking their move.{RESET}"
        for _ in range(3):
            print(picking_move_text + "\r")
            picking_move_text = picking_move_text + f"{RED}.{RESET}"
            time.sleep(0.5)
        print()

        # enemy just does base attack but will regenerate if it's a wizard
        attack_type_roll = random.choice(["base_attack", "special_attack"])
        if attack_type_roll == "base_attack":
            self.enemy.base_attack(self.player)
        else:
            special_attack_roll = random.choice(
                [spec_abil for spec_abil in self.enemy.special_abilities.keys()]
            )
            self.enemy.perform_special(self.player, special_attack_roll)

        # If the enemy is an Evil Wizard
        if isinstance(self.enemy, EvilWizard):
            self.enemy.regenerate()

    def record_special_ability_choice(self) -> str:
        """Display special abilities and have player choose one via stdin"""

        # List available abilities
        print(f"{YELLOW}*** Your Abilities ***{RESET}")
        special_ability_names = list(self.player.special_abilities.keys())
        for i, ability in enumerate(special_ability_names, start=1):
            print(f"{YELLOW}{i}: {ability}{RESET}")

        while True:
            ability_choice = input(f"{YELLOW}Choose an Ability: {RESET} ")

            # validate numeric input
            if not ability_choice.isdigit():
                print(f"{BRIGHT_RED}Please enter a number!{RESET}")
                continue

            ability_choice = int(ability_choice)
            if ability_choice in range(1, len(special_ability_names) + 1):
                return special_ability_names[ability_choice - 1]
            else:
                print(
                    f"{BRIGHT_RED}Invalid selection made for special ability. Try again.{RESET}"
                )


def main():
    game = GamePlay(
        player=GamePlay.prompt_user_to_create_character(),
        enemy=GamePlay.prompt_user_to_create_character(enemy=True),
    )
    game.battle()


if __name__ == "__main__":
    main()
