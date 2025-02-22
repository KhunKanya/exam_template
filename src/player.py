class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = int(x)
        self.pos_y = int(y)
        self.inventory = []

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy

    def can_move(self, x, y, grid):
        # Fix for version 1-C Man ska inte kunna gå igenom väggar.
        if grid.get(self.pos_x + x, self.pos_y + y) == grid.wall:
            return False
        else:
            return True

    # Fix version 1-E, F Inventory - alla saker som man plockar upp ska sparas i en lista
    def add_item(self, item):
        self.inventory.append(item)

    def print_inventory(self):
        retlist = []
        for item in self.inventory:
            retlist.append(item.name)
        retstring = ", ".join(retlist)
        return retstring








        # if direction == "d" and player.can_move(1, 0, g):  # move right
        #     # TODO: skapa funktioner, så vi inte behöver upprepa så mycket kod för riktningarna "W,A,S"
        #     maybe_item = g.get(player.pos_x + 1, player.pos_y)  # ตรวจสอบว่ามีไอเท็มอยู่ในตำแหน่งที่จะย้ายไปหรือไม่
        #     player.move(1, 0)  # เพื่อย้ายผู้เล่นไปทางขวา
        #
        #     if isinstance(maybe_item, pickups.Item):
        #         # we found something
        #         score += maybe_item.value
        #         print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
        #         # g.set(player.pos_x, player.pos_y, g.empty)
        #         g.clear(player.pos_x, player.pos_y)