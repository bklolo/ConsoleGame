import Items

class PlayerInventory:

    def __init__(self):

        self.items = []
    
    def add_item(self, new_item): 

        # If max inventory limit then do check here.
        self.items.append(new_item)

    def remove_item(self, item):
        self.items.remove(item)