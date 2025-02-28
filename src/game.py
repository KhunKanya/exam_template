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

# Function to make the playing experience much better. Clear the screen upon each refresh
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


command = "a"
# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    g.print_status(score)

    command = input("Use WASD to move, J+WASD to jump, Q/X to quit. ")
    clear_screen()

    # Version 2.N add Jump logic
    if command.casefold()[:1] == 'j':
        # Command will be taken from the 2nd character, jw, w will be taken
        command = command.casefold()[1]
        jump = True
    else:
        command = command.casefold()[:1]
        jump = False

    # Fix for version 1-B Förflyttningar i alla 4 riktningar. (WASD)
    directions = {
        'a': [-1, 0], # left
        'd': [1, 0],  # right
        'w': [0, -1], # up
        's': [0, 1]   # down
    }

    # If jump is true, double its value
    if jump:
        for key, list in directions.items():
            for i in range(len(list)):
                list[i] *= 2 

    if command not in ['w','a','s','d','q','x','i']:
        print("Invalid command.")
        continue
    
    if command in ['w', 'a', 's', 'd']:

        if player.can_move(directions[command][0], directions[command][1], g) or player.can_move_through_wall(directions[command][0], directions[command][1], g):
            if player.can_move_through_wall(directions[command][0], directions[command][1], g):
                g.clear(player.pos_x + directions[command][0], player.pos_y + directions[command][1])
                player.has_shovel = False
                player.remove_item('shovel')
            maybe_item = g.get(player.pos_x + directions[command][0], player.pos_y + directions[command][1])
            player.move(dx=directions[command][0], dy=directions[command][1])

            if isinstance(maybe_item, pickups.Item):
                # we found something
                score += maybe_item.value
                # Separated logic if player steps on trap, or not
                if  maybe_item.type == 'trap':
                    print(f"Oh noes, you stepped on a {maybe_item.name}. {maybe_item.value} points redacted")
                elif maybe_item.type == 'chest':
                    if player.has_key():
                        g.clear(player.pos_x, player.pos_y)                
                        print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
                        player.add_item(maybe_item)
                        player.remove_item('key')
                    else:
                        # Dont want to duplicate this add score code everywhere so removing the score where it shouldnt have been added in the first place
                        score -= maybe_item.value
                # Create exit function, will break if theres no chests or fruits on the game field
                elif maybe_item.type == 'exit' and not any(item.type == 'fruit' or item.type == 'chest' for item in g.get_items_on_map()):
                    break
                else:
                    if maybe_item.type != 'exit':
                        g.clear(player.pos_x, player.pos_y)                
                    print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
                    player.add_item(maybe_item)
                
                # g.set(player.pos_x, player.pos_y, g.empty)

            else:
                score -= 1  # fix version1 G. The floor is lava - för varje steg man går ska man tappa 1 poäng.

    if command == "i":
        print(player.print_inventory())
        continue

    # use the modular (%) to see if our total steps taken is dividable by 25, resulting in 0 every 25th time
    if player.get_steps_taken() % 25 == 0:
        pickups.randomize(g, False)
    
    

# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")
