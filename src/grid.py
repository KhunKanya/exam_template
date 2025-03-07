import random
from . import pickups

class Grid:
    """Representerar spelplanen. Du kan ändra standardstorleken och tecknen för olika rutor. """
    width = 36 # x  == 18
    height = 12 # y == 6
    empty = "."  # Tecken för en tom ruta
    wall = "■"   # Tecken för en ogenomtränglig vägg

    def __init__(self):
        """Skapa ett objekt av klassen Grid"""
        # Spelplanen lagras i en lista av listor. Vi använder "list comprehension" för att sätta tecknet för "empty" på varje plats på spelplanen.
        self.data = [[self.empty for y in range(self.width)] for z in range(
            self.height)]
    
    # Crate function to return all the items on the map
    def get_items_on_map(self):
        item_list = []
        for x in range(self.width):
            for y in range(self.height):
                if isinstance(self.get(x, y), pickups.Item):
                    item_list.append(self.get(x, y))
        return item_list


    # Moved from game.py as requested
    def print_status(self, score):
        """Visa spelvärlden och antal poäng."""
        print("--------------------------------------")
        print(f"You have {score} points.")
        print(self)

    def get(self, x, y):
        """Hämta det som finns på en viss position"""
        try:
            return self.data[y][x]
        except IndexError:
            return None


    def set(self, x, y, value):
        """Ändra vad som finns på en viss position"""
        self.data[y][x] = value

    def set_player(self, player):
        self.player = player
    
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height

    def clear(self, x, y):
        """Ta bort item från position"""
        self.set(x, y, self.empty)

    def __str__(self):
        """Gör så att vi kan skriva ut spelplanen med print(grid)"""
        xs = ""
        for y in range(len(self.data)):
            row = self.data[y]
            for x in range(len(row)):
                if x == self.player.pos_x and y == self.player.pos_y:
                    xs += "@"
                else:
                    xs += str(row[x])
            xs += "\n"
        return xs

    def get_center_pos(self):         # fix for version1 A spelaren ska börja nära mitten av rummet.
        return [self.width / 2, self.height / 2]
    #   return [18, 6]


    def make_walls(self):
        """Skapa väggar runt hela spelplanen"""
        for i in range(self.height):
            self.set(0, i, self.wall)
            self.set(self.width - 1, i, self.wall)

        for j in range(1, self.width - 1):
            self.set(j, 0, self.wall)
            self.set(j, self.height - 1, self.wall)

    def create_random_wall(self):
        # randomize if wall is vertical or horizontal. If even, wall will be vertical
        if random.randint(0, 100) % 2 == 0:

            # Randomize how long the wall will bne
            wall_length = random.randint(1, self.height)
            # randomize on which X-axis it will be
            rand_x_pos = random.randint(2, self.width - 1)

            # Randomize where on the Y-axis it will begin
            # Had to move the random-int function inside a while True because sometimes it will randomize a non-range like randing(1,1). If that happens, try again
            while True:
                try:
                    start_pos = random.randint(2, self.height - wall_length)
                    break
                except ValueError:
                    start_pos = random.randint(2, self.height)
                    # print("Reached the exception")
                    break
            # Print the wall inside a loop
            for i in range(wall_length):
                # If the wall try to do an is_empty outside the list, ignore this wall-call with the break
                try:
                    if self.is_empty(rand_x_pos, start_pos + i):
                        self.set(rand_x_pos, start_pos + i, self.wall)
                    else:
                        break
                except IndexError:
                    break
        else:
            # Same code as above but for X axis instead
            wall_length = random.randint(1, self.width)
            # randomize on which Y-axis it will be. start from pos 2 becuase 1 is already occupied with a wall. Same goes for the -1
            rand_y_pos = random.randint(2, self.height - 1)

            # Randomize where on the Y-axis it will begin
            # Had to move the random-int function inside a while True because sometimes it will randomize a non-range like randing(1,1). If that happens, try again
            while True:
                try:
                    start_pos = random.randint(2, self.width - wall_length)
                    break
                except ValueError:
                    start_pos = random.randint(2, self.width)
                    break
            # Print the wall inside a loop
            for i in range(wall_length):
                # If the wall try to do an is_empty outside the list, ignore this wall-call with the break
                try:
                    if self.is_empty(start_pos + i, rand_y_pos):
                        self.set(start_pos + i, rand_y_pos, self.wall)
                    else:
                        break
                except IndexError:
                    break
                
    def create_random_walls(self, amount):
        for _ in range(amount):
            self.create_random_wall()

    # Används i filen pickups.py
    def get_random_x(self):
        """Slumpa en x-position på spelplanen"""
        return random.randint(0, self.width-1)

    def get_random_y(self):
        """Slumpa en y-position på spelplanen"""
        return random.randint(0, self.height-1)


    def is_empty(self, x, y):
        """Returnerar True om det inte finns något på aktuell ruta"""
        return self.get(x, y) == self.empty

