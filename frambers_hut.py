#This is Framber's Hut
from sys import exit 


#exit module for testing
def test_exit(from_module):
    print(f"ok, exited from {from_module}. bye")
    exit(0)

yes = 'Yes' 'yes' 'Y' 'y' 'ya' 'Ya'
no = 'No' 'no' 'n' 'N' 'na' 'Na'
a = 'a' 'A' 
b = 'b' 'B'
c = 'c' 'C'
hut_chest1_done = False

user1 = input("What is your name?\n>> ") 
print(f"Hello {user1},\nWelcome to\t\n...\n...\n...\nFRAMBER'S HUT!")
lives_lost = 0



def dead(why):
    global lives_lost
    lives_lost += 1
    print(why, "You're dead. \nDo you wanna try again?")
    choice = input("Yes or no?>> ")
    if choice in yes:
        forest()
    else:
        print(f"Thanks for playing, you lost {lives_lost} lives in your journey through Framber's Hut. \nGoodbye!")
        exit(0)





#Forest
#write more ambient forest story
def forest():
    print("""...
    You are in a dark and deeply green forest.
    There is a mist creeping all around.
    The trees reach to the the very heavens, and nothing but thin streams of light reach down to the forest floor.
    A path lies ahead, through the hazy forest gloom...""")

    forest_choice1(False)



def forest_choice1(map_done):
    print("""What do you do next?
    A. Check pack.
    B. Climb roots.
    C. Slog through mud.""")
    
    map_done = map_done
    
    choice = input("What do you pick?(CHOOSE A LETTER)\n>> ")

    if choice in a and not map_done:
        forest_1a()
    elif choice in a and map_done:
        print("You already checked your pack.")
        forest_choice1(map_done)
    elif choice in b:
        forest_1b(map_done)
    elif choice in c:
        forest_1c(map_done)
    else:
        exit(0)



def forest_1a():
    print("There are 2 items in your pack. Which do you want to see?")
    choice = input("'1' or '2'?>> ")

    if '1' in choice:
        print("A black, rusty key. Seems important.")
        forest_1a()
    elif '2' in choice:
        encrypt_map(0)
    else:
        print("Pick a number, fool.")
        forest_1a()



def forest_1b(map_done):
    print("""The roots of the giant cypress are growing from the muck and mud.
    You grab a hold of the nearest one and jump from root to root,
    making your way across the swampy forest floor.
    Off in the distance, you hear a low rumble... are there gators in these swamps???
    """)
    if map_done == True:
        print("You now stand before Framber's Hut!")
    else:
        print("You stand before a menacing and unknown hut!")

    hut(map_done)



def forest_1c(map_done):
    map_done = map_done
    choice = input("The mud looks deep and ferocious. \nAre you sure you want to slog?>> ")
    if choice != yes:
        print("The mud is deeper and more ferocious than ever you could've imagined. You sink down and down and down...")
        dead('The mud buried you alive.')
    else:
        forest_choice1(map_done)



def encrypt_map(n):
    print("In your hand, there's a folded and worn piece of parchment that seems to be in some sort of code.")
    print("The cypher is as follows:\n\t 5 + 4 * 3 - 2 = ??")
    answer = int(input("What is the answer?>> "))
    cypher = 5 + 4 * 3 - 2
    n = n
    
    if n < 3:
        map_burned = False
    else:
        map_burned = True

    if cypher == answer and not map_burned:
        decrypt_map()
    elif cypher != answer and not map_burned:
        print(f"Wrong, try again. {n}/3")
        n += 1
        encrypt_map(n)
    else:
        print("The map burns to ash in your hands, and crumbles forever into the dust.")
        forest_choice1(map_burned)


        
def decrypt_map():
    print("""The letters rearrnage themselves slowly on the creased parchment...
    ...
    shapes slowly begin to take form
    ...
    it look like a map!
    At the top it says Framber's Hut,
    and it shows a diagram of each room.
    In the corner, there's a list that reads:
    \t* Hut\n\t* Study \n\t* Lair \n\t* Tunnel  
    """) 
    
    # build working map
    #print("Congratulations, you've unlocked the map!\n If you ever want to access the map, use 'm' whenever you're at a fork in the road")
    print("There's something on the back, would you like to read it?")
    
    choice = input("Yes or no?>> ")

    if choice in yes:
        #write framber's lore
        # test_exit('frambers_lore')
        print("You cannot decipher these gibberish letters. You put away your pack and look around...")
        forest_choice1(True)
    else:
        print("Alright, thats all that's in your pack, you straighten up and look around...")
        forest_choice1(True)


    


#Hut


def hut(map_done):
    print("""
    The wooded walls of the hut are grey and green.
    Ivy and moss drip from the eaves, and thick grasses snake their way up the sides.
    You walk up to the stairs before you...""")
    hut_choice1(map_done, 'nonlooped', 'none', 0, False)



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
        choice_d = choice_d.strip(); choice_d = choice_d.casefold()
        break_door = 'kick' 'kick door' 'push' 'push door' 'wack' 'break' 'break down door'
        if choice_d in break_door:
            print("The door gives way with a dusty squelch...")
            living_room(map_done)
        elif choice_d == 'knock':
            print("Bro, I think there's no one home. Do you wanna bust in?")
            choice_k = input("Yes or No?>> ")
            if choice_k in yes:
                print("The door gives way with a dusty squelch")
                living_room(map_done)
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
        hut_choice1c(map_done, times_tried, scared)
    else:
        print("You must pick a letter.")
        hut_choice1(map_done, 'loop', 'none')



def hut_choice1b(map_done, times_tried, scared):
    if map_done == False:
        print("Hmmmmmm.")
        hut_choice1(map_done, 'nonlooped', 'none', times_tried, scared)
    elif scared == True:
        print("You tremble before the deepening of the shrouded cedar trees.")
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


    
def hut_choice1c(map_done, times_tried, scared):
    if hut_chest1_done == True:
        print("You already checked that out.")
        hut_choice1(map_done, 'nonlooped', 'none', times_tried, scared)
    elif times_tried < 2 and scared == False:
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
            hut_chest1(map_done, times_tried, scared)
        else:
            print("The darkness of the murky cedars is truly menacing.")
            scared = True
            hut_choice1(map_done, 'nonlooped', 'none', times_tried, scared)
    else:
        print("You are simply too frightened of the deepening jungle.")
        hut_choice1(map_done, 'nonlooped', 'none', times_tried, scared)
    

            


#Lving Room
def living_room(map_done):
    print("""\tYou walk inside the house.
    Everything is covered in a thick layer of dust.
    The sunlight wriggles through the windows, tinted green by the mildew.
    *cough* *cough*
    Before you lies a table. To your right, along the wall, a shelf stands. 
    The room recedes in to the deeper shadows, but at the far end, just beyond two saggy chairs,
    the faint outline of a door is visible.
    To your left, there is another door, old and wooden.
     """)
    living_room_choice1(map_done)



def living_room_choice1(map_done)
    print("What do you want to do?")
    choice = input(">> ")





def hut_chest1(map_done, times_tried, scared):
    #puzzle
    print("a gnarly puzzle belongs here")
    print("a cool strand-type item belongs here")
    global cool_gem1
    global hut_chest1_done
    hut_chest1_done = True
    cool_gem1 = True
    hut_choice1(map_done, 'nonloope', 'none', times_tried, scared)




forest()





