# Now we have a premise. We are in a room and we have two door to choose from.
# Each door leads to a room and we need to do something, in the red room specifically.

##### ROOMS #####
def blissful_ignorance_of_illusion_room():
    # Nothing happens here, let's do one room at the time. :-)
    print("The door knob jiggles but nothing happens.")
    return

def painful_truth_of_reality_room():
    print("There you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    next_move = input("> ")

    # Flee to return to the start of the game, in the room with the blue and red door or die!
    if "flee" in next_move:
        start_adventure()
    else:
        print("You died. Well, that was tasty!")
### END ROOMS ###

def start_adventure():
    print("You enter a room, and you see a red door to your left and a blue door to your right.")
    door_picked = input("Do you pick the red door or blue door? > ")

    # Pick a door and we go to a room and something else happens
    if door_picked == "red":
        # This calls a function that contains stuff that happens in painful_truth_of_reality_room
        painful_truth_of_reality_room()
    elif door_picked == "blue":
        # This calls a function that contains stuff that happens in blissful_ignorance_of_illusion_room
        blissful_ignorance_of_illusion_room()
    else:
        print("Sorry, it's either 'red' or 'blue' as the answer. You're the weakest link, goodbye!")

def main():
    player_name =  input("What's your name? >")
    print("Your name is {}".format(player_name.upper()))

    start_adventure()

if __name__ == '__main__':
    main()