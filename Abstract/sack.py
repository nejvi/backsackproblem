import Abstract

class Sack(object):
    sack_items = []
    max_capacity = 100
    value = 0

    def __init__(self):
        self.max_capacity = 100
        self.value = 0

    def showItems(self):

        for sack_item in self.sack_items:
            sack_item.printItem()
    
    def addItemToSack(self, itemToAdd):
        # if not is isinstance(itemToAdd, Item) return

        self.sack_items.append(itemToAdd)
        self.max_capacity += itemToAdd.weight
        self.value += itemToAdd.value