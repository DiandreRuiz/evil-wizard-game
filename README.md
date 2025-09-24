# 🧙‍♂️ Defeat the Evil Wizard

A turn-based battle game built with Python Object-Oriented Programming where you create a hero character and battle against the powerful Evil Wizard!

## 🎮 Game Overview

Choose from four unique character classes, each with their own special abilities, and engage in strategic turn-based combat against the Evil Wizard. Use attacks, special abilities, healing, and defensive tactics to emerge victorious!

## 🏰 Character Classes

### 🛡️ Warrior
- **Health**: 140 HP
- **Attack Power**: 25
- **Special Abilities**:
  - **Big Sword Swing**: Devastating 50 damage attack
  - **Angel's Blessing**: Heals 25 HP and blocks next attack

### 🔮 Mage
- **Health**: 100 HP  
- **Attack Power**: 35
- **Special Abilities**:
  - **Fireball**: Powerful 50 damage magical attack
  - **Arcane Forcefield**: Blocks the next incoming attack

### 🏹 Archer
- **Health**: 75 HP
- **Attack Power**: 50
- **Special Abilities**:
  - **Flaming Arrow**: High-damage 50 attack with fire element
  - **Archer Shield**: Defensive block against next attack

### ⚔️ Paladin
- **Health**: 150 HP
- **Attack Power**: 30
- **Special Abilities**:
  - **Holy Strike**: Divine 50 damage attack
  - **Hero's Touch**: Restores 25 HP

### 🧙‍♂️ Evil Wizard (Enemy)
- **Health**: 150 HP
- **Attack Power**: 15
- **Special Abilities**:
  - **Evil Laugh**: 50 damage attack + 5 HP regeneration
  - **Evil Smile**: 25 damage attack + blocks next attack
- **Unique Trait**: Regenerates 5 HP after every attack!

## 🎯 Game Features

- **Turn-Based Combat**: Strategic gameplay with player and enemy turns
- **Randomized Damage**: Attack damage varies within a range for unpredictability
- **Special Abilities**: Each character has two unique special moves
- **Healing System**: Restore health without exceeding maximum HP
- **Blocking Mechanics**: Defensive abilities to negate incoming attacks
- **Colorful Interface**: Enhanced visual experience with terminal colors
- **Victory/Defeat Conditions**: Clear end-game messaging

## 🚀 How to Play

1. **Run the game**:
   ```bash
   python main.py
   ```

2. **Choose your character** from the four available classes

3. **Name your hero** and your enemy

4. **Battle!** Each turn you can:
   - **Basic Attack**: Deal damage with randomized power
   - **Use Special Ability**: Choose from your character's unique moves
   - **Heal**: Restore 5 HP
   - **View Stats**: Check current health and attack power

5. **Defeat the Evil Wizard** to win!

## 🛠️ Technical Implementation

### Object-Oriented Design
- **Base Character Class**: Common functionality for all characters
- **Inheritance**: Each character class extends the base Character class
- **Special Abilities System**: Modular ability framework with attack, healing, and blocking components
- **Polymorphism**: Different character behaviors through method overriding

### Key Classes
- `Character`: Base class with health, attack, and special ability management
- `SpecialAbility`: Defines ability effects (damage, healing, blocking)
- `GamePlay`: Manages battle flow and user interaction
- Character subclasses: `Warrior`, `Mage`, `Archer`, `Paladin`, `EvilWizard`

## 📁 Project Structure

```
defeat-evil-wizard/
├── main.py              # Main game logic and battle system
├── characters.py        # Character classes and abilities
├── input_utils.py       # Input handling utilities
├── stdout_coloring.py   # Terminal color definitions
└── README.md           # This file
```

## 🎓 Learning Objectives

This project demonstrates:
- **OOP Principles**: Inheritance, polymorphism, and encapsulation
- **Interactive Programming**: Menu systems and user input handling
- **Game Logic Design**: Turn-based combat mechanics
- **Code Organization**: Modular design with separate concerns

## 🏆 Victory Conditions

- **Player Wins**: Reduce the Evil Wizard's health to 0 or below
- **Enemy Wins**: Your character's health reaches 0 or below

## 🎨 Features

- Colorful terminal output for enhanced visual experience
- Randomized attack damage for unpredictable gameplay
- Strategic depth through special abilities and blocking mechanics
- Clear victory/defeat messaging with celebratory formatting

---

*Defeat the Evil Wizard and save the realm!* ⚔️✨
