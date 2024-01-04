class Item:
       def __init__(self, name, price):
                self.name = name
                self.price = price


class Consumable(Item):
        pass


class Weapon(Item):

        def __init__(self, name, price, melee_damage, action_word):
                super().__init__(name, price)
                self.melee_damage = melee_damage
                self.action_word = action_word


class Armor(Item):

        def __init__(self, name, price, melee_defence, magic_defence):
                super().__init__(name, price)
                self.melee_defence = melee_defence
                self.magic_defence = magic_defence


class Spells:

        def __init__(self, magic_damage):
                self.magic_damage = magic_damage


# TODO: Make our own weapons, armors, and spells.
                
##-- items --##

##-- weapons --##
short_sword = Weapon("Short Sword", 5, 10, "swung")
wooden_staff = Weapon("Wooden Staff", 6, 2, "swung")

##-- armor --##

##-- spells --##



# Item Database
items = {}

spells = {}
