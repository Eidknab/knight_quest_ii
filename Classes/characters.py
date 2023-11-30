class Character:
    def __init__(self, character_type, name, class_name, 
                 level_max, level, xp_max, xp, hp_max, hp, mp_max, mp, 
                 strength, dexterity, vitality, spirit,  
                 gold, critical, armor,
                 inventory, spellbook):
        self.caractere_type = character_type    # player, monster, boss, merchant
        self.name = name
        self.class_name = class_name            # warrior, mage, rogue and all monsters types
        self.level = level
        self.level_max = level_max
        self.xp_max = xp_max
        self.xp = xp
        self.hp_max = hp_max
        self.hp = hp
        self.mp_max = mp_max
        self.mp = mp
        # attributes 80 points to share + 5 points per level
        self.strength = strength                # add physical damage
        self.dexterity = dexterity              # add hit, critical & dodge chance
        self.vitality = vitality                # add health points
        self.spirit = spirit                    # add mana points and increase spellbook size
        # base stats
        self.critical = critical                # base critical chance
        self.armor = armor                      # base armor
        # gold and futur currencies
        self.gold = gold
        # whithout constructor
        # equiped
        self.weapon = None
        self.shield = None
        self.helmet = None
        self.chest = None
        self.ring_left = None
        self.ring_right = None
        self.amulet = None
        # inventory
        self.inventory = []
        self.inventory_max_size = 10
        # spellbook
        self.spellbook = []
        self.spellbook_max_size = spirit // 10 + 1
        