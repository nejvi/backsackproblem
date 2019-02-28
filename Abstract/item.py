class Item(object):
    name = None
    weight = 0
    value = 0

    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

    def printItem(self):
        print("Name of item {self.name} weight {self.weight} value {self.value}")