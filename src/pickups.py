import random

class Item:
    """Representerar saker man kan plocka upp."""
    def __init__(self, name, value=20, symbol="?", type='fruit'):
        self.name = name
        self.value = value
        self.symbol = symbol
        self.type = type


    def __str__(self):
        return self.symbol

# For version 2.K. Create function to make pairs of key+chests. Defaults to just 1 pair
def create_chest_keys(amount=1):
    retlist = []
    for _ in range(amount):
        retlist.append(Item("chest", value=100, symbol='𝦳', type='chest'))
        retlist.append(Item("key", value=0, symbol='⚿', type='key'))
    
    return retlist
        


pickups = [Item("carrot"), Item("apple"), Item("strawberry"), Item("cherry"), Item("watermelon"), Item("radish"), Item("cucumber"), Item("meatball"), Item("shovel", value=0, symbol='♠', type="shovel"), Item("Exit", value=0, symbol='E', type='exit')]
# Create a trap
traps = [Item("rävsax", -10, symbol='☠', type="trap")]


# For version 2.L Add new variable all, and when its false, only one random item from the pickups is chosen and placed onto the map
def randomize(grid, all=True):
    # add the trap to the list of items
    
    if all:
        items = pickups + traps + create_chest_keys(2)
    else:
        # Exclude exit and shovel from being randomly created on the map every 25 step
        excluded_types = {'exit', 'shovel'}
        filtered_pickups = [item for item in pickups if item.type not in excluded_types]
        items = []
        items.append(random.choice(filtered_pickups))
    for item in items:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen

