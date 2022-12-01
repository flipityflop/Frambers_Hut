fffff

yes = 'Yes' 'yes' 'Y' 'y' 'ya' 'Ya'
no = 'No' 'no' 'n' 'N' 'na' 'Na'
a = 'a' 'A' 
b = 'b' 'B'
c = 'c' 'C'
#delete line on import
map_done = True

def hut_choice1(map_done, from_door, choice_loop, times_tried, scared):
    #from_door = from_door
    if from_door != 'loop':
        print("What do you do next?")
        print("""\tA. Try the door.
        B. Hmmmmmm...
        C. Go back into the forest.""")
        choice = input("Pick a letter:>> ")
    elif from_door == 'loop' and choice_loop not in a:
        choice = input("Pick a letter:>> ")
    else:
        choice = choice_loop

    if choice in a:
        print("The door seems jammed from damp.")
        choice_d = input("What do you do?>> ")
        choice_d = choice_d.strip()
        if choice_d == 'kick' or choice_d == 'push':
            print("The door gives way with a dusty squelch...")
            living_room()
        elif choice_d == 'knock':
            print("Bro, I think there's no one home. Do you wanna bust in?")
            choice_k = input("Yes or No?>> ")
            if choice_k in yes:
                print("The door gives way with a dusty squelch")
                living_room()
            else:
                hut_choice1(map_done, 'nonlooped', 'a', times_tried, scared)
        elif choice_d == 'go back' or choice_d == 'turn around' or choice_d == 'back':
            hut_choice1(map_done, 'nonlooped', 'none', times_tried, scared)
        else:
            print("You actions are unclear. \nYou must decide, for darkness seeps from the forest.")
            hut_choice1(map_done, 'loop', 'a', times_tried, scared)
    elif choice in b:
        print("Hmmmmmmm...")
        hut_choice1b(map_done, times_tried, scared)
    elif choice in c:
        times_tried += 1
        hut_choice1c(times_tried, scared)
    else:
        print("You must pick a letter.")
        hut_choice1(map_done, 'loop', 'none')



def hut_choice1b(map_done, times_tried, scared):
    if map_done == False:
        print("Hmmmmmm.")
        hut_choice1(map_done, 'nonlooped', 'none', times_tried, scared)
    else:
        print("""\tYou seem to vaguely recall an intersting something on the map.
        You take a look...
        ...
        there's a nifty little trail that goes from here around the edge of the forest,
        to an area on the map marked with a picture of a gator and a skull.
        You look up and there, overgrown and muddy, a trail twists off into the gloom.
        The growl of a distant gator can be heard.
        Do you want to follow the path?""")

    choice = input("Yes or No?>> ")
    if choice in yes and scared == False:
        path_to_gators(map_done)
    else:
        scared = True
        print("You tremble before the deepening of the shrouded cedar trees.")
        hut_choice1(map_done, 'nonlooped', 'none', times_tried, scared)


    
def hut_choice1c(times_tried, scared):
    if times_tried < 2 and scared == False:
        print("The darkness creeps ever closer.")
        hut_choice1(map_done, 'nonlooped', 'none', times_tried, scared)
    elif times_tried == 2 and scared == False:
        print("Why? The seeping yellow-green color is quite dark.")
        hut_choice1(map_done, 'nonlooped', 'none', times_tried, scared)
    elif times_tried > 2 and scared == False: 
        print("""\tYou wearily turn back towards the forest.
        As you do, a glint catches your eye.
        Something is buried in the mud at the entrance to the forest!
        Do you want to go check it out?""")

        choice = input("Yes or No?>> ")

        if choice in yes:
            print("""\tCarefully, you walk towards the spec if metal poking out.
            From the mud, you dig out a chest.
            It appears to be locked.""")
            hut_chest1()
        else:
            print("The darkness of the murky cedars is truly menacing.")
            scared = True
            hut_choice1(map_done, 'nonlooped', 'none', times_tried, scared)
    else:
        print("You are simply too frightened of the deepening jungle.")
        hut_choice1(map_done, 'nonlooped', 'none', times_tried, scared)



    




def living_room():
    print("Hey you've reached the living room. placeholder")

def hut_chest1():
    #puzzle
    print("a gnarly puzzle belongs here")
    print("a cool strand-type item belongs here")
    global cool_gem1
    cool_gem1 = True

hut_choice1(map_done, 'nonlooped', 'none', 0, False)