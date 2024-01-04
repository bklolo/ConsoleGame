class Player:
    
    def __init__(self, name, player_class, max_health, melee_attack, magic_attack,
    max_mana, max_stamina, defense):
        
        self.name = name
        self.player_class = player_class
        self.level = 1
        self.exp = 0

        # Health
        self.max_health = max_health
        self.health = self.max_health  ##-- Not sure if this is smart but this should only set health to max on making the character --##
        # Attack
        self.melee_attack = melee_attack
        self.magic_attack = magic_attack
        # Mana
        self.max_mana = max_mana
        self.mana = self.max_mana
        # Stamina
        self.max_stamina = max_stamina
        self.stamina = self.max_stamina
        # Defense
        self.defense = defense

def level_up(player):
    player.level += 1
    player.max_health = player.max_health + player.level
    player.armor = player.armor + player.level
    player.mana = player.mana + player.level
    player.stamina = player.stamina + player.level

