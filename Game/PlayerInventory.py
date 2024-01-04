import Items

class PlayerInventory:

    def __init__(self):

        self.inventory_item_limit = 10 
        self.bag = []
        self.equiped_weapon = Items.fist
        self.equiped_armor = Items.farm_clothing
    
    def add_to_inventory(self, add_item): 

        self.add_item = add_item
        if len(self.bag) < self.inventory_item_limit:
            self.bag.append(self.add_item)

    def remove_from_inv(self, remove_item):
        self.remove_item = remove_item