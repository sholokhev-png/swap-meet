class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return None

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None    
    
    def swap_items(self, other_vendor, my_item, their_item):
        if (my_item not in self.inventory) or (their_item not in other_vendor.inventory):
            return False
        else:
            self.remove(my_item)
            self.add(their_item)
            other_vendor.remove(their_item)
            other_vendor.add(my_item)        
            return True

    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0:
            return False    
        if len(other_vendor.inventory) == 0:
            return False
        
        my_first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]

        self.remove(my_first_item)
        other_vendor.remove(their_first_item)

        self.add(their_first_item)
        other_vendor.add(my_first_item)

        return True

        

    
    