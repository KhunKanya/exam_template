from .grid import Grid
from .player import Player
from . import pickups


score = 0
inventory = []

g = Grid()
start_center = g.get_center_pos()
player = Player(start_center[0], start_center[1])
#player = Player(2, 1)
g.set_player(player)
g.make_walls()
pickups.randomize(g)



# TODO: flytta denna till en annan fil
def print_status(game_grid):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"You have {score} points.")
    print(game_grid)


command = "a"
# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    print_status(g)

    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1]

    directions = {
        'a': [-1, 0], # left
        'd': [1, 0], # right
        'w': [0, -1], # up
        's': [0, 1] # down
    }
    if command not in ['w','a','s','d','q','x']:
        print("Invalid command.")
        continue

    if player.can_move(directions[command][0], directions[command][1], g):
        maybe_item = g.get(player.pos_x + directions[command][0], player.pos_y + directions[command][1])
        player.move(directions[command][0], directions[command][1])

        if isinstance(maybe_item, pickups.Item):
            # we found something
            score += maybe_item.value
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            # g.set(player.pos_x, player.pos_y, g.empty)
            g.clear(player.pos_x, player.pos_y)


# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")
