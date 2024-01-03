class Character():
    def __init__(self, health, stamina):
        # Character Traits
        self.health = health
        self.stamina = stamina
    def get_health(self):
        return self.health
    def get_stamina(self):
        return self.stamina

class Enemy(Character):
    def __init__(self, health, stamina, aggro):
        super().__init__(health, stamina)
        # Std Enemy Traits
        self.aggro = aggro
    
    def get_aggro(self):
        return self.aggro
    def reduce_agrro(self):
        return self.aggro - 10

class Goblin(Enemy):
    def __init__(self, health, aggro, greed):
        super().__init__(health, aggro)
        # Goblin Traits
        self.greed = greed
    def lower_greed(self):
        return self.greed - 20