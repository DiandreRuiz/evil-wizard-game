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

    def battle(player: Character, opponent: Character):
        while opponent.health > 0 and player.health > 0:
            print("\n--- Your Turn ---")
            print("1. Basic Attack")
            print("2. Use Special Ability")
            print("3. Heal")
            print("4. View Stats")

            choice = input("Choose an action: ")

            match choice:
                case "1":
                    player.base_attack(opponent)
                case "2":
                    special_ability_choice = record_special_ability_choice(player)
                    player.perform_special(opponent, special_ability_choice.name)

            if choice == "1":
                player.attack(opponent)
            elif choice == "2":
                pass  # Implement special abilities
            elif choice == "3":
                pass  # Implement heal method
            elif choice == "4":
                player.display_stats()
            else:
                print("Invalid choice. Try again.")

            if opponent.health > 0:
                opponent.regenerate()
                opponent.attack(player)

            if player.health <= 0:
                print(f"{player.name} has been defeated!")
                break

        if opponent.health <= 0:
            print(f"The wizard {opponent.name} has been defeated by {player.name}!")


def record_special_ability_choice(player: Character) -> str:
    """Display special abilities and have player choose one via stdin"""

    # List available abilities
    print("*** Your Abilities ***")
    special_ability_names = list(player.special_abilities.keys())
    for i, ability in enumerate(special_ability_names, start=1):
        print(f"{i}: {ability}")

    while True:
        ability_choice = input("Choose an Ability: ")

        # validate numeric input
        if not ability_choice.isdigit():
            print("Please enter a number!")
            continue

        ability_choice = int(ability_choice)
        if ability_choice in range(1, len(special_ability_names) + 1):
            return special_ability_names[ability_choice - 1]
        else:
            print("Invalid selection made for special ability. Try again.")


def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)


if __name__ == "__main__":
    main()
