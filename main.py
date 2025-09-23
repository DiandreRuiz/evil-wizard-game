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
from stdout_coloring import RESET, RED, GREEN, YELLOW, PURPLE, CYAN, BRIGHT_RED


class GamePlay:
    def __init__(self, player: Character, enemy: Character):
        self.player = player
        self.enemy = enemy

    def create_character() -> Character:
        print("Choose your character class:")
        print("1. Warrior")
        print("2. Mage")
        print("3. Archer")
        print("4. Paladin")

        class_choice = input("Enter the number of your class choice: ")
        name = input("Enter your character's name: ")

        if class_choice == "1":
            return Warrior(name)
        elif class_choice == "2":
            return Mage(name)
        elif class_choice == "3":
            return Archer(name)
        elif class_choice == "4":
            return Paladin(name)
        else:
            print("Invalid choice. Defaulting to Warrior.")
            return Warrior(name)

    def battle(self):
        while self.enemy.health > 0 and self.enemy.health > 0:
            print("\n--- Your Turn ---")
            print("1. Basic Attack")
            print("2. Use Special Ability")
            print("3. Heal")
            print("4. View Stats")

            choice = input("Choose an action: ")

            match choice:
                case "1":
                    self.player.base_attack(self.enemy)
                case "2":
                    special_ability_choice = self.record_special_ability_choice(
                        self.player
                    )
                    self.player.perform_special(self.enemy, special_ability_choice)

            if choice == "1":
                self.player.base_attack(self.enemy)
            elif choice == "2":
                pass  # Implement special abilities
            elif choice == "3":
                pass  # Implement heal method
            elif choice == "4":
                self.player.display_stats()
            else:
                print("Invalid choice. Try again.")

    def player_turn(self):
        """Collect player move decision and play it out"""

        while True:
            print("\n--- Your Turn ---")
            print("1. Basic Attack")
            print("2. Use Special Ability")
            print("3. Heal")
            print("4. View Stats")

            choice = input("Choose an action: ")

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

    def record_special_ability_choice(self) -> str:
        """Display special abilities and have player choose one via stdin"""

        # List available abilities
        print(f"{YELLOW}*** Your Abilities ***{RESET}")
        special_ability_names = list(self.player.special_abilities.keys())
        for i, ability in enumerate(special_ability_names, start=1):
            print(f"{YELLOW}{i}: {ability}{RESET}")

        while True:
            ability_choice = input(f"{YELLOW}Choose an Ability:{RESET} ")

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
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)


if __name__ == "__main__":
    main()
