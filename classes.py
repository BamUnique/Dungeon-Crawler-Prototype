from enum import Enum


class CharacterClass(Enum):
    ARCHER = {
        "Basic Attack": "Quick Shot",
        "Powerful Attack": "Charge Shot",
        "Heal Ability": "Bandage",
        "Dodge": "Roll",
        "Stat Multipliers": {
            "Health Multiplier": 1,
            "Defence Multiplier": 1,
            "Strength Multiplier": 4,
            "Wisdom Multiplier": 1,
            "Agility Multiplier": 4
        }
    }
    BERSERKER = {
        "Basic Attack": "Slash",
        "Powerful Attack": "Stab",
        "Heal Ability": "Potion",
        "Dodge": "Dash",
        "Stat Multipliers": {
            "Health Multiplier": 1.5,
            "Defence Multiplier": 1,
            "Strength Multiplier": 5,
            "Wisdom Multiplier": 1,
            "Agility Multiplier": 2.5
        }
    }
    MAGE = {
        "Basic Attack": "Fireball",
        "Powerful Attack": "Mage Lightning",
        "Heal Ability": "Heal  Spell",
        "Dodge": "Mage Barier",
        "Stat Multipliers": {
            "Health Multiplier": 1,
            "Defence Multiplier": 0.6,
            "Strength Multiplier": 1,
            "Wisdom Multiplier": 8,
            "Agility Multiplier": 2.5
        }
    }
    TANK = {
        "Basic Attack": "Shield Bash",
        "Powerful Attack": "Shield Throw",
        "Heal Ability": "Potion",
        "Dodge": "Block",
        "Stat Multipliers": {
            "Health Multiplier": 3,
            "Defence Multiplier": 2,
            "Strength Multiplier": 4,
            "Wisdom Multiplier": 1,
            "Agility Multiplier": 1.5
        }
    }
    
    
class Character():
    def __init__(self, char_class):
        self.base_health = 100
        self.base_defence = 50
        self.base_strength = 10
        self.base_wisdom = 10
        self.base_agility = 10
        
        self.player_abilities = {}
        char_class = CharacterClass[char_class.upper()].value
        for key, value in char_class.items():
            if key == ("Stat Multipliers"):
                for stat, multiplier in value.items():
                    setattr(self, "base_" + stat.split()[0].lower(), getattr(self, "base_" + stat.split()[0].lower()) * multiplier)
            else:
                self.player_abilities[key] = value
                
        self.inventory = {
            "Equipped Weapon": None,
            "Equipped Armour": None,
            "Inventory": [{
                "Armour": [],
                "Weapons": [],
                "Other": []
            }]    
        }


        
if __name__ == "__main__":
    chose_char = Character("archer")
