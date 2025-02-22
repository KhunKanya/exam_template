from .grid import Grid
from .player import Player
from . import pickups
import os

score = 0
inventory = []

g = Grid()
start_center = g.get_center_pos()     # Fix for version 1-A Spelaren ska börja nära mitten av rummet.
player = Player(start_center[0], start_center[1])  # X, Y
#player = Player(2, 1)
g.set_player(player)
g.make_walls()
pickups.randomize(g)
g.create_random_walls(5)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


command = "a"
# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    g.print_status(score)

    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1]

    # Fix for version 1-B Förflyttningar i alla 4 riktningar. (WASD)
    directions = {
        'a': [-1, 0], # left
        'd': [1, 0],  # right
        'w': [0, -1], # up
        's': [0, 1]   # down
    }
    if command not in ['w','a','s','d','q','x','i']:
        print("Invalid command.")
        continue
    
    if command in ['w', 'a', 's', 'd']:

        if player.can_move(directions[command][0], directions[command][1], g):
            maybe_item = g.get(player.pos_x + directions[command][0], player.pos_y + directions[command][1])
            player.move(dx=directions[command][0], dy=directions[command][1])

            if isinstance(maybe_item, pickups.Item):
                # we found something
                score += maybe_item.value
                print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
                player.add_item(maybe_item)
                # g.set(player.pos_x, player.pos_y, g.empty)
                g.clear(player.pos_x, player.pos_y)
            else:
                score -= 1  # fix version1 G. The floor is lava - för varje steg man går ska man tappa 1 poäng.

    if command == "i":
        clear_screen()
        print(player.print_inventory())
        continue
    clear_screen()
    

# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")
