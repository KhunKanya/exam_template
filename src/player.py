class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = int(x)
        self.pos_y = int(y)
        self.inventory = []
        # version 2.J, shovel. see game.py for more explaination
        self.has_shovel = False
        # For version 2.L Count total steps taken
        self.steps_taken = 0

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy
        self.steps_taken += 1

    def can_move(self, x, y, grid):
        # Fix for version 1-C Man ska inte kunna gå igenom väggar och inte kunna hoppa utanfor kartan
        if grid.get(self.pos_x + x, self.pos_y + y) == grid.wall or grid.get(self.pos_x + x, self.pos_y + y) == None:
            return False
        else:
            return True
    
    def can_move_through_wall(self, x, y, grid):
        # Check if next move is wall with self.can_move, False means wall so negating the result from it
        # Also checking we are not trying to destroy on of the outer walls with all of the x and y checks
        if (not self.can_move(x, y, grid)
            and self.has_shovel == True
            and self.pos_x + x > 0 and self.pos_x + x < grid.get_width() - 1
            and self.pos_y + y > 0 and self.pos_y + y < grid.get_height() - 1
        ):
            return True
        else:
            return False
    # Fix version 1-E, F Inventory - alla saker som man plockar upp ska sparas i en lista
    def add_item(self, item):
        self.inventory.append(item)
        if item.type == 'shovel':
            self.has_shovel = True        
    
    # Function to remove a specific type of item from the inventory. Used for removing shovel once used and key when used
    def remove_item(self, type):
        to_remove = next((item for item in self.inventory if item.type == type), None)
        if to_remove:
            self.inventory.remove(to_remove)
    
    # Returns true if key in inventory list
    def has_key(self):
        return any(item.type == 'key' for item in self.inventory)

    def print_inventory(self):
        retlist = []
        for item in self.inventory:
            retlist.append(item.name)
        retstring = ", ".join(retlist)
        return retstring

    # For version 2.L return our steps taken
    def get_steps_taken(self):
        return self.steps_taken
