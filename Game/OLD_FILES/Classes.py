class Character():
    def __init__(self, health, stamina, symbol, position):
        # Character Traits
        self.health = health
        self.stamina = stamina
        self.symbol = symbol
        self.position = position

    def get_health(self):
        return self.health
    def get_stamina(self):
        return self.stamina


class Player(Character):
    def __init__(self,      health, stamina, symbol, position):
        super().__init__(   health, stamina, symbol, position)
        # Player traits
        self.inv = []

    def add_item(self, item):
        self.inv.append(item)

# aggro: chance on encounter()
class Enemy(Character):
    def __init__(self,      health, stamina, symbol, position, cooldown):
        super().__init__(   health, stamina, symbol, position)
        # Std Enemy traits
        self.cooldown = cooldown
        #self.aggro = aggro
    
    def get_aggro(self):
        return self.aggro
    def reduce_agrro(self):
        return self.aggro - 10

# greed: the more money you have, the more likely an encounter()
class Goblin(Enemy):
    def __init__(self, health, symbol, greed):
        super().__init__(health, symbol)
        # Goblin Traits
        self.greed = greed
    
    def get_greed(self):
        return  self.greed
    def lower_greed(self):
        return self.greed - 10