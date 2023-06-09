#This is Framber's Hut
from sys import exit
import time
import random 


#exit module for testing
def test_exit(from_module):
    print(f"ok, exited from {from_module}. bye")
    exit(0)

yes = 'Yes' 'yes' 'Y' 'y' 'ya' 'Ya'
no = 'No' 'no' 'n' 'N' 'na' 'Na'
a = 'a' 'A' 
b = 'b' 'B'
c = 'c' 'C'

#Collected items
gg_diary_note = False
gator_statue = False
hut_chest1_done = False
sandwich = False
frambers_spectacles = False
frambers_sword = False

print("This is a text based game. Input your answers as simply as possible and lowercase.\nTry things like 'look' if you feel stumped.\n")
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
        input(">> [PRESS ANY KEY TO EXIT]")
        exit(0)





#Forest
#write more ambient forest story
def forest():
    print("""...
        You are in a dark and deeply green forest.
        There is a mist creeping all around.
        The trees reach to the the very heavens, and nothing but thin streams of light reach down to the forest floor.
        A path lies ahead, through the hazy forest gloom...
    """)

    forest_choice1(False)



def forest_choice1(map_done):
    print("What do you do next?\nA. Check pack. \nB. Climb roots.\nC. Slog through mud.")
    
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
    print("""
        The roots of the giant cypress are growing from the muck and mud.
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
    if 'yes' in choice or 'y' in choice:
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
    print("""
        The letters rearrnage themselves slowly on the creased parchment...
        ...
        shapes slowly begin to take form
        ...
        it look like a map!
        At the top it says Framber's Hut,
        and it shows a diagram of each room.
        In the corner, there's a list that reads:
        \t* Hut\n\t* Study \n\t* Tunnel \n\t* Workshop  
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








#Path to them gators


def path_to_gators(map_done):
    print("""
        You walk carefully along a muddy path, that slowly winds past the house and off to to right,
        back into the woods.
        As you continue along, your boots slurp in the muds,
        and the dense forest on either side slowly gives way to pools of water.
        Tall grasses stick out amidst the massive and gnarled tress,
        reigning like kings within their own small water kigndom.
        You think you see a log with yellow eyes, but turns out it was just a evil looking gator.
        You've reached the end of the path, and you find yourself before a boggy pool, silently surging with gators.
        You spot something semi-submerged in the water, about 10 feet out.
        Moss and algae are growing on it.
        You wonder what else there is around here...
    """)
    gator_pool(False, 0)

def gator_pool(fishing_hook, looked_nu, look='', hook_c='', boat_c='', sandwich_c=''):
    global sandwich
    look = ['look', 'around', 'help', 'check']
    choice = input("What do you do?>> ")
    if any(ele in choice for ele in look) and looked_nu < 3:
        print("You see a few different things.\n\t*1. A fishing rod with a hook.\n\t*2. A boat.\n\t*3. A sandwich.")
        looked_nu += 1
        gator_pool(fishing_hook, looked_nu)
    elif any(ele in choice for ele in look) and looked_nu == 3:
        print("Bud, stop stalling. You've seen what there is to see. Do something.")
        looked_nu += 1
        gator_pool(fishing_hook, looked_nu)
    elif any(ele in choice for ele in look) and looked_nu == 4:
        print("""Bud, stop stalling. You've seen what there is t...
        ...
        o.
        Theres's a old note on the ground, directly in front of you.
        You open it and it reads: 
        'Today I decided to throw my sweet gator statue into the water. 
        It was a tough decision, but its clearly alive and has tried to eat me various times.
        Still, it was a sweet statue. The cursed red eyes were my favorite.""")
        global gg_diary_note
        gg_diary_note = True
        looked_nu += 1 
        gator_pool(fishing_hook, looked_nu)
    elif any(ele in choice for ele in look) and looked_nu > 4:
        print("You see the same 3 things that you saw before.\n\t*1. A fishing rod with a hook.\n\t*2. A boat.\n\t*3. A sandwich.")
        print("There's nothing else. Stop.")
        gator_pool(fishing_hook, looked_nu)
    elif '1' in choice:
        print("You grab the hook and rod. You're too far from the statue to try and hook it.")
        fishing_hook = True
        gator_pool(fishing_hook, looked_nu)
    elif '2' in choice:
        gg_boat(fishing_hook, looked_nu)
    elif '3' in choice and sandwich == False:
        print("You pick up the sandwich.")
        choice = input("Do you A. want to keep, or B. feed the sandwich to the gators?\n>> ")
        if choice in a or choice in "keep":
            print("A delightful jingle plays, and you jump and hold the sandwich aloft.")
            print("A little box pops up that says 'A tuna fish sandwich. This is the most powerful item in the game'")
            print("That was neat. Anyway, you eat the sandwich and it is quite tasty.")
            sandwich = True
            gator_pool(fishing_hook, looked_nu)
        else:
            print("""
        Why? 
        Why would you try to feed a sandwich to a murky pool of terrifying gators?
        Why?
        Anyway, you bend down to feed some sandwich, and you instantly are chomped upon by a horde of vicious, yellow eyed monsters.
        Good job.
        """)
            dead("You tried to feed gators, jesus christ.")
    elif '3' in choice and sandwich == True:
        print("You already got the sandwich. Try something else")
        gator_pool(fishing_hook, looked_nu)
    else:
        print("What does that mean? Try do something clever or even coherent. [PICK A NUMBER]")
        gator_pool(fishing_hook, looked_nu)
            

        

def gg_boat(fishing_hook, looked_nu, fishing_hook_c=''):
    fishing_hook_c = ['fishing', 'rod', 'hook']
    print("You spot an ancient and quite trusty looking wooden rowboat.\nAs you climb in, a particularly meaty looking gator give you a knowing snarl\nThis is seems vaguely unwise.")
    choice = input("Do you want to give it a shot?>> ")
    if choice in yes:
        print("You row towards the object. As you get closer, you begin to see that it is a wicked gator statue with reddish glowing jewels for eyes.")
        choice = input("Do you want to grab it with your hand? btw, that meaty gator is lying nearby, his mouth open, just waiting.\nYes or no?>> ")
        if choice in yes:
            print("The second you reach your hand out of the boat, the gator lunges up and literally pulls you under water, while biting your arm off.")
            dead("You spend your final seconds grasping for breath and being chomped by gator.")
        else:
            print("Good choice. The gator looks particularly unhappy. Any other ideas?")
            choice = input(">> ")
            if choice in no:
                print("Alright, you row boack to shore.")
                gator_pool(fishing_hook, looked_nu)
            elif fishing_hook == True and any(ele in choice for ele in fishing_hook_c):
                print("""
        From this distance, you can easily snag an tooth on the gator statue.
        You firmly wedge the hook in a the ring for the oar and begin to row backwards.
        With a delightful squelch, the gator slowly slinks up from the mud,
        water and green sliding down from its mouth.
        The gators in the water move about in a frenzy, but you're not in some kind of flimsy boat.
        You head back to shore with the figurine in tow, and you pull the beautiful, glowing eyed statue on to dry land.
                """)
                print("You head back towards the house.")
                global gator_statue
                gator_statue = True
                hut(True)
            elif fishing_hook == False and any(ele in choice for ele in fishing_hook_c):
                print("I think there was a fishing rod back at the shore...")
                gator_pool(fishing_hook, looked_nu)
    else:
        print("Ok")
        gator_pool(fishing_hook, looked_nu)   








#Hut


def hut(map_done):
    print("""
        The wooded walls of the hut are grey and green.
        Ivy and moss drip from the eaves, and thick grasses snake their way up the sides.
        You walk up to the stairs before you...
    """)
    hut_choice1(map_done, 'nonlooped', 'none', 0, False)



def hut_choice1(map_done, from_door, choice_loop, times_tried, scared):
    #from_door = from_door
    if from_door != 'loop':
        print("What do you do next?")
        print("A. Try the door. \nB. Hmmmmmm... \nC. Go back into the forest.")
        choice = input("Pick a letter:>> ")
    elif from_door == 'loop' and choice_loop not in a:
        choice = input("Pick a letter:>> ")
    else:
        choice = choice_loop

    if choice in a:
        print("The door seems jammed from damp.")
        choice_d = input("What do you do?>> ")
        choice_d = choice_d.strip(); choice_d = choice_d.casefold()
        break_door = ['kick', 'kick door', 'push', 'push door', 'wack', 'break', 'break down door', 'bash']
        if any(ele in choice_d for ele in break_door):
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
    global gator_statue
    if map_done == False:
        print("Hmmmmmm.")
        hut_choice1(map_done, 'nonlooped', 'none', times_tried, scared)
    elif scared == True:
        print("You tremble before the deepening of the shrouded cedar trees.")
        hut_choice1(map_done, 'nonlooped', 'none', times_tried, scared)
    elif gator_statue == True:
        print("You've already gone there.")
        hut_choice1(map_done, 'nonlooped', 'none', times_tried, scared)
    else:
        print("""
        You seem to vaguely recall an interesting something on the map.
        You take a look...
        ...
        there's a nifty little trail that goes from here around the edge of the forest,
        to an area on the map marked with a picture of a gator and a skull.
        You look up and there, overgrown and muddy, a trail twists off into the gloom.
        The growl of a distant gator can be heard.
        Do you want to follow the path?
        """)
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
        print("""
        You wearily turn back towards the forest.
        As you do, a glint catches your eye.
        Something is buried in the mud at the entrance to the forest!
        Do you want to go check it out?
        """)

        choice = input("Yes or No?>> ")

        if choice in yes:
            print("""
        Carefully, you walk towards the speck of metal.
        From the mud, you dig out a chest.
        It appears to be locked.
            """)
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
    print("""
        You walk inside the house.
        Everything is covered in a thick layer of dust.
        The sunlight wriggles through the windows, tinted green by the mildew.
        *cough* *cough*
        Before you lies a *table. To your right, along the wall, a *shelf stands. 
        The room recedes in to the deeper shadows, but at the far end, just beyond two saggy chairs,
        the faint outline of a door is visible. 
        It's clearly not accessible. 
        Maybe it will be someday, but not today.
        To your left, there is another *door, old and wooden.
     """)
    living_room_choice1(map_done, False, False, False, False, False)



def living_room_choice1(map_done, table, shelf, left_door, frambers_spectacles, frambers_sword):
    print("What do you want to do?")
    check_specs = ['put', 'wear', 'spectacle']
    choice = input(">> ")
    choice = choice.rstrip("s")
    if "look" in choice or "help" in choice or "remind" in choice:
        print("You see a table in front of you, a shelf, and a door to the left")
        living_room_choice1(map_done, table, shelf, left_door, frambers_spectacles, frambers_sword)
    elif table == False and frambers_sword == False and "table" in choice:
        print("The floorboards creak as you approach the table.")
        lr_table(map_done, table, shelf, left_door, frambers_spectacles, frambers_sword)
    elif table == False and frambers_sword == True and "table" in choice:
        print("The floorboards creak as you approach the table.")
        lr_table_cleared(map_done, table, shelf, left_door, frambers_spectacles, frambers_sword)
    elif table == True and "table" in choice:
        print("After swiping the table clean and picking through the wreckage, there isn't much left to see there.")
        living_room_choice1(map_done, table, shelf, left_door, frambers_spectacles, frambers_sword)
    elif shelf == False and "shelf" in choice:
        print("You make your way carefully towards the shelf, making a trail through the dust choking the floor.")
        shelf = True
        lr_shelf(map_done, table, shelf, left_door, frambers_spectacles, frambers_sword)
    elif shelf == True and "shelf" in choice:
        print("You've already checked out the shelf. It's not that interesting.")
        living_room_choice1(map_done, table, shelf, left_door, frambers_spectacles, frambers_sword)
    elif left_door == False and table == False and "door" in choice or "left" in choice:
        print("You take a step towards the next room, and then pause to look around. Maybe there's something useful in here?")
        living_room_choice1(map_done, table, shelf, left_door, frambers_spectacles, frambers_sword)
    elif left_door == False and table == True and "door" in choice or "left" in choice:
        print("The door swings open.")
        left_door = True
        lr_left_door(map_done, table, shelf, left_door, frambers_spectacles, frambers_sword)
    elif left_door == True and "door" in choice or "left" in choice:
        print("Now that you have the items you need, you head back through the door to the Closet of Saphire.")
        closet_saphire(frambers_spectacles, frambers_sword)
        #print("There is no logical way that you've gotten back into this room in this context. So i guess yer ded.")
        #dead("Teleportation / breaking the laws of physics / illicit magical items.")
    elif frambers_spectacles == True and any(ele in choice for ele in check_specs):
        print("You try on the specs. They feel comfy, but they make everything too bright, so you take them back off.")
        living_room_choice1(map_done, table, shelf, left_door, frambers_spectacles, frambers_sword)
    else:
        print("Try something else. You feel a deep wisdom swelling within you.")
        living_room_choice1(map_done, table, shelf, left_door, frambers_spectacles, frambers_sword)


def lr_table_cleared(map_done, table, shelf, left_door, frambers_spectacles, frambers_sword):
    print("Everything you swept off the table lies in a heap on the floor. There's a pair of spectacles lying on an overturned book.")
    lr_table_choice1(map_done, table, shelf, left_door, frambers_spectacles, frambers_sword)


def lr_table(map_done, table, shelf, left_door, frambers_spectacles, frambers_sword):
    print("""
        The table is heaped with clutter, as though someone left in a hurry.
        There are piles of *books and papers.
        One of the *papers appears to be a map, but its been damaged by a large splotch of ink.
        You can't even see the table *underneath all the stuff.
        There's a pair of *spectacles on top of a stack of books.
    """)
    lr_table_choice1(map_done, table, shelf, left_door, frambers_spectacles, frambers_sword)

def lr_table_choice1(map_done, table, shelf, left_door, frambers_spectacles, frambers_sword):
    print("What do you do?")
    clear_table = ['clear', 'table', 'wipe', 'check', 'under', 'uderneath'] 
    check_specs = ['glasse', 'spectacle']
    choice = input(">> ")
    choice = choice.rstrip("s")
    choice = choice.split(" ")
    if "read" in choice or "book" in choice or "paper" in choice or "map" in choice:
        print("You can't uderstand any of the languages, and the map is damaged.")
        lr_table_choice1(map_done, table, shelf, left_door, frambers_spectacles, frambers_sword)
    elif frambers_sword == False and frambers_spectacles == False and any(ele in choice for ele in check_specs):
        print("You grab the spectacles. They buzz ever so slightly. I wonder what they'll help you see?")
        frambers_spectacles = True
        lr_table_choice1(map_done, table, shelf, left_door, frambers_spectacles, frambers_sword)
    elif frambers_spectacles == True and any(ele in choice for ele in check_specs):
        print("You try on the spectacles. They make everything bright and fuzzy, as though everything was on fire. Too bright. You take them back off.")
        lr_table_choice1(map_done, table, shelf, left_door, frambers_spectacles, frambers_sword)
    elif frambers_sword == False and any(ele in choice for ele in clear_table):
        print("""
        You (violently) clear everything off the table in one sweeping motion.
        Underneath it all, a beautiful sword lies.
        It appears to be of a silver blue metal, with the finest inlay of orange in the blade.
        The handle is wrapped in leather. 
        An inscription reads: 'Yus dunha strohs.'
        Off in the distance, you hear a muffled thump.
        Weird.
        You sheath the sword in your belt.
    """)
        frambers_sword = True
        lr_table_choice1(map_done, table, shelf, left_door, frambers_spectacles, frambers_sword)
    elif frambers_sword == True and any(ele in choice for ele in clear_table):
        print("You already cleared everything off the table.")
        lr_table_choice1(map_done, table, shelf, left_door, frambers_spectacles, frambers_sword)
    elif frambers_sword == True and frambers_spectacles == False and any(ele in choice for ele in check_specs):
        print("You bend down to pick up the spectacles. They buzz ever so slightly. I wonder what they'll help you see?")
        frambers_spectacles = True
        lr_table_choice1(map_done, table, shelf, left_door, frambers_spectacles, frambers_sword)
    elif frambers_sword == True and frambers_spectacles == True and "step" in choice or "back" in choice:
        table = True
        print("You step back from the table.")
        living_room_choice1(map_done, table, shelf, left_door, frambers_spectacles, frambers_sword)
    elif "step" in choice or "back" in choice:
        print("You step back from the table.")
        living_room_choice1(map_done, table, shelf, left_door, frambers_spectacles, frambers_sword)
    else:
        print("Thats not something you can do. Do you want to *A try something else, or *B step back from the table?")
        choice = input(">> ")
        if frambers_sword == True and frambers_spectacles == True and "b" in choice or "B" in choice:
            print("You step back from the table.")
            table = True
            living_room_choice1(map_done, table, shelf, left_door, frambers_spectacles, frambers_sword)
        elif "b" in choice or "B" in choice:
            print("You step back from the table.")
            living_room_choice1(map_done, table, shelf, left_door, frambers_spectacles, frambers_sword)
        else:
            print("You look around the table to see what else to try.")
            lr_table_choice1(map_done, table, shelf, left_door, frambers_spectacles, frambers_sword)


def lr_shelf(map_done, table, shelf, left_door, frambers_spectacles, frambers_sword):
    print("""
        The shelf has some leather bound books.
        Beneath them there's a jar with some strange liquid that appears to be dimly glowing in the dying sun.
        Next to it lies another jar, empty, with traces of black residue.
        You pick up the jar and peer inside. Not much to see.
        The sunlight continues its valiant effort against the incoming dusk, 
        as you step back from the shelf.
    """)
    living_room_choice1(map_done, table, shelf, left_door, frambers_spectacles, frambers_sword)

def lr_left_door(map_done, table, shelf, left_door, frambers_spectacles, frambers_sword):
    print("""
        You find yourself in a something like a library.
        There's piles and piles of books, and shelves everywhere.
        The day has given way to a burning dusk, and light squeezes its way through cracks
        in the teetering pile of *books stacked against the windows.
        There's a *blank space on the opposite wall and slivers of light are glowing softly on it.
        There's a *single small table and an oversized armchair.
    """)
    study(map_done, False, False, False)





#Study

def study(map_done, small_table, stack_books, blank_wall):
    print("What do you want to do?")
    check_table = ['table', 'small', 'armchair', 'chair']
    check_stacks = ['stack', 'book']
    check_wall = ['wall', 'blank', 'opposite']
    check_specs = ['put', 'wear', 'spectacle', 'glasse']
    choice = input(">> ")
    choice = choice.rstrip("s")
    choice = choice.split(" ")
    if small_table == False and stack_books == False and any(ele in choice for ele in check_table):
        print("On the table is a key. You pick it up. There doesn't appear to be anywhere to use this.")
        small_table = True
        study(map_done, small_table, stack_books, blank_wall)
    elif small_table == False and stack_books == True and any(ele in choice for ele in check_table):
        print("On the table is a key. You pick it up. It probably goes into the keyhole in the wall!")
        small_table = True
        study(map_done, small_table, stack_books, blank_wall)    
    elif small_table == True and any(ele in choice for ele in check_table):
        print("You already grabbed the key from the table. See if you can find where it goes.")
        study(map_done, small_table, stack_books, blank_wall)
    elif stack_books == False and small_table == False and any(ele in choice for ele in check_stacks):
        print("""
        You start to move the stacks of books and papers, trying to let the light in.
        The orange glow is dimming quickly as you move.
        Suddenly, you hear a hissing sound behind you.
        You turn quickly.
        The space on the wall behind you has trails of sparks running all over the wall, tracing their way up and down.
        The shape of a door is being revealed in the burnt markings.
        As all the sparks converge on a final spot, a small keyhole becomes visible.
        Maybe there's a key somewhere around here?
        """)
        stack_books = True
        study(map_done, small_table, stack_books, blank_wall)
    elif stack_books == True and small_table == False and any(ele in choice for ele in check_stacks):
        print("There's no key in these books.")
        study(map_done, small_table, stack_books, blank_wall)
    elif stack_books == False and small_table == True and any(ele in choice for ele in check_stacks):
        print("""
        You start to move the stacks of books and papers, trying to let the light in.
        The orange glow is dimming quickly as you move.
        Suddenly, you hear a hissing sound behind you.
        You turn quickly.
        The space on the wall behind you has trails of sparks running all over the wall, tracing their way up and down.
        The shape of a door is being revealed in the burnt markings.
        As all the sparks converge on a final spot, a small keyhole becomes visible.
        You put the key in the the hole and the door swings inwards with a sigh.
        There's a flight of steps that trail of into the darkness.
        """)
        stack_books = True
        hallway_doom(map_done)
    elif blank_wall == False and stack_books == False and any(ele in choice for ele in check_wall):
        print("""
        Amidst all the clutter, this wall is starkly cleared.
        The stacks of books are so high, they appear almost to form a doorway,
        but it leads into solid wood.
        As you approach, you notice footprints trailing through the dust on the floor, heading right through the arch of books.
        The wall is completely smooth, save for the creases in the decaying wood.
        The light filtering through the window seems to be trying to burn through the wall.
        You give it a shove and hurt your shoulder. It appears as though it is just a wall.
        """)
        blank_wall = True
        study(map_done, small_table, stack_books, blank_wall)
    elif stack_books == True and small_table == False and any(ele in choice for ele in check_wall):
        print("You need to look around for a key.")
        study(map_done, small_table, stack_books, blank_wall)
    elif blank_wall == True and stack_books == False and any(ele in choice for ele in check_wall):
        print("That wall sure seems weird, but there isn't much else you can learn about it.")
        study(map_done, small_table, stack_books, blank_wall)
    elif small_table == True and stack_books == True and any(ele in choice for ele in check_wall):
        print("""
        You put the key in the the hole and the door swings inwards with a sigh.
        There's a flight of steps that trail of into the darkness.
        """)
        hallway_doom(map_done)
    elif any(ele in choice for ele in check_specs):
        print("You try on the specs. They feel comfy, but they make everything too bright, so you take them back off.")
        study(map_done, small_table, stack_books, blank_wall)
    else:
        print("All these books are making you smarter. That gives you an idea to try something else. Something better. Something I can understand.")
        study(map_done, small_table, stack_books, blank_wall)





#Hallway of doom
def hallway_doom(map_done):
    spectacles_on = False
    wear_specs = ['wear', 'put', 'spectacle', 'glasse']
    print("You see a torch by the door, do you want to grab it? How else will you see in the dark?")
    choice = input(">> ")
    choice = choice.rstrip("s")
    if "yes" in choice or "y" in choice:
        hallway_doom_torch()    
    elif any(ele in choice for ele in wear_specs):
        hallway_doom_specs()

def hallway_doom_torch():
    print("""
        You grab a torch by the door and make your way down.
        After a few steps, the floor levels out and and a tunnel twists off ahead.
        You make your way along, feeling the wood panels as you go.
        A light appears up ahead.
        Fire.
        ...
        ...
    """)
    workshop_room(False)

def hallway_doom_specs():
    print("""
        You put on the spectacles. They feel warm on your face.
        The darkness is now glowing and you can see easily.
        The steps before you are beautifully crafted of deep oak wood,
        and the paneled wall have words carved all along them.
        They're burning.
        You make your way down the steps, and feel the walls as the floor levels off into a tunnel.
        Up ahead, a light is growing.
        Fire.
        ...
        ...
    """)
    workshop_room(True)

def workshop_room(spectacles_on):
    print("Flames and metal. An evil sword. A shield painted with a black heart. A tall knight stands before you.")
    ws_combat_timer(spectacles_on)





#combat sytem


def retry_combat(why_combat, spectacles_on):
    global lives_lost
    lives_lost += 1
    retry_phrases = ['Give it another go.', 'Have another shot at it.', 'You arise valiantly to try again.', 'ANOTHER!', 'Try again.', 'A hero never stays down for long!', 'Your soul flows back into your body', 'Arise, fighter!']
    print(why_combat)
    choice = input("You died. Do you want to try again?>> ")
    if 'yes' in choice or 'y' in choice:
        print(random.choice(retry_phrases))
        global amount_base
        ws_combat1(spectacles_on, amount_base)
    else:
        dead("You were killed by the Knight of Darkness.")


def ws_combat_timer(spectacles_on, t1=0, t2=0, tt=0):
    input("Press ENTER when you're ready!")
    t1 = time.time()
    print("The knight will attack, and you must fight back!")
    print("If you take too long to choose, you will not survive.")
    print("But you have as many chances as you need.")
    input("Hit ENTER when that all makes sense.>> ")
    t2 = time.time()
    global amount_base
    amount_base = t2 - t1
    print(f"You'll have around {int(amount_base + 4)} seconds to make your move!")
    ws_combat1(spectacles_on, amount_base)


def ws_combat1(spectacles_on, amount_base, why_combat=None, t1=0, t2=0, tt=0, correct=None, amount=0):
    amount = amount_base + 3
    amount = int(amount)
    if spectacles_on == False:
        correct = "Dodge"
    else:
        correct = "DODGE"
    input("Ready?>> [ENTER] ")
    t1 = time.time()
    print("His giant sword comes swinging down towards you.")
    print(f"a. Parry with your sword.\nb. {correct}\nc. Jump")
    answer = input(">> ")
    t2 = time.time()
    tt = t2 - t1
    if tt > amount:
        why_combat = "You delayed too long. The swords slices right through you. The last things you see is black flames..."
        retry_combat(why_combat, spectacles_on)
    elif 'a' in answer:
        why_combat = "You attempt to block, but his sword's black flames shear right through your sword, piercing your mind..."
        retry_combat(why_combat, spectacles_on)
    elif 'b' in answer:
        ws_combat2(spectacles_on, amount_base)
    elif 'c' in answer:
        why_combat = "You jump directly into his swinging blade. It cleaves you straight in two."
        retry_combat(why_combat, spectacles_on)
    else:
        why_combat = "You try something incoherent, and the delay costs you your life."
        retry_combat(why_combat, spectacles_on)

def ws_combat2(spectacles_on, amount_base, why_combat=None, t1=0, t2=0, tt=0, correct=None, amount=0):
    amount = amount_base + 2
    amount = int(amount)
    #print(amount)
    if spectacles_on == False:
        correct = "Dodge"
    else:
        correct = "DODGE"
    print("You roll away, but he quickly turns around with a shield bash!")
    t1 = time.time()
    print(f"a. Block with your arms.\nb. Strike with your sword! \nc. {correct}")
    answer = input(">> ")
    t2 = time.time()
    tt = t2 - t1
    if tt > amount:
        why_combat = "You delayed too long. The shield crashes through your mind and soul..."
        retry_combat(why_combat, spectacles_on)
    elif 'a' in answer:
        why_combat = "You lift your arms in a pathetic attempt, but his monstrous shield shatters your very essence. You are dead"
        retry_combat(why_combat, spectacles_on)
    elif 'c' in answer:
        ws_combat3(spectacles_on, amount_base)
    elif 'b' in answer:
        why_combat = "You try to counter with a strike of your own, but his shield knocks the sword harmlessly to the floor."
        retry_combat(why_combat, spectacles_on)
    else:
        why_combat = "You try something incoherent, and the delay costs you your life."
        retry_combat(why_combat, spectacles_on)


def ws_combat3(spectacles_on, amount_base, why_combat=None, t1=0, t2=0, tt=0, correct=None, amount=0):
    amount = amount_base + 3
    amount = int(amount)
    if spectacles_on == False:
        correct = "Quick strike"
    else:
        correct = "QUICK STRIKE"
    print("The black flames flicker as he growls and turns, 'ENOUGH!.' Now is your chance to...")
    t1 = time.time()
    print(f"a. {correct}.\nb. Hit him with an icy blast. \nc. Look around for something to use.")
    answer = input(">> ")
    t2 = time.time()
    tt = t2 - t1
    if tt > amount:
        why_combat = ("You delayed too long. His anger is terrible...")
        retry_combat(why_combat, spectacles_on)
    elif 'b' in answer:
        why_combat = "His fire is a terror, but you have no combatant. He recovers and strikes..."
        retry_combat(why_combat, spectacles_on)
    elif 'a' in answer:
        ws_combat4(spectacles_on, amount_base)
    elif 'c' in answer:
        why_combat = "You look around and see something quite interesting, but in your delay, he cleaves your head right off."
        retry_combat(why_combat, spectacles_on)
    else:
        why_combat = "You try something incoherent, and the delay costs you your life."
        retry_combat(why_combat, spectacles_on)


def ws_combat4(spectacles_on, amount_base, why_combat=None, t1=0, t2=0, tt=0, correct=None, amount=0):
    amount = amount_base + 10
    amount = int(amount)
    if spectacles_on == False:
        correct = "You look around"
    else:
        correct = "YOU LOOK AROUND"
    print("With incredible dexterity, you slide your sword along his molten armor.")
    print("A crack of white light burns him where you struck. He howls in pain, but the black flames grow stronger! You must think quick, because you may not get another shot!")
    t1 = time.time()
    print(f"a. {correct}\nb. You attempt to disarm him. \nc. You strike again, more mightily.")
    answer = input(">> ")
    t2 = time.time()
    tt = t2 - t1
    if tt > amount:
        why_combat = ("You delayed too long. He recovers his wits, and strikes you down...")
        retry_combat(why_combat, spectacles_on)
    elif 'b' in answer:
        why_combat = "As you grab at his sword, the flames grow magnificent. The hilt of his sword burns your hand."
        retry_combat(why_combat, spectacles_on)
    elif 'a' in answer:
        ws_combat5(spectacles_on, amount_base)
    elif 'c' in answer:
        why_combat = "He was ready. He knocks away your puny strike, and retaliates with epic might."
        retry_combat(why_combat, spectacles_on)
    else:
        why_combat = "You try something incoherent, and the delay costs you your life."
        retry_combat(why_combat, spectacles_on)


def ws_combat5(spectacles_on, amount_base, why_combat=None, t1=0, t2=0, tt=0, correct=None, amount=0):
    amount = amount_base + 3
    amount = int(amount)
    if spectacles_on == False:
        correct = "A silver necklace"
    else:
        correct = "A SILVER NECKLACE"
    print("You take advantage of his mometary weakness to look for something mighty. You grab...")
    t1 = time.time()
    print(f"a. A golden shield. \nb. A flask with blue liquid. \nc. {correct}")
    answer = input(">> ")
    t2 = time.time()
    tt = t2 - t1
    if tt > amount:
        why_combat = ("While you were taking your time perusing, he was hacking you to bits.")
        retry_combat(why_combat, spectacles_on)
    elif 'a' in answer:
        why_combat = "You lift up the shield to block his incoming blow, but its bends beneath his ultimate strength!"
        retry_combat(why_combat, spectacles_on)
    elif 'c' in answer:
        ws_combat6(spectacles_on, amount_base)
    elif 'c' in answer:
        why_combat = "You drink the flask, and you feel your inside melting. His evil laughter is the final sound..."
        retry_combat(why_combat, spectacles_on)
    else:
        why_combat = "You try something incoherent, and the delay costs you your life."
        retry_combat(why_combat, spectacles_on)


def ws_combat6(spectacles_on, amount_base, why_combat=None, t1=0, t2=0, tt=0, correct=None, amount=0):
    amount = amount_base + 5
    amount = int(amount)
    if spectacles_on == False:
        correct = "Hold up the necklace"
    else:
        correct = "HOLD UP THE NECKLACE"
    print("The knecklace has an deep blue gem in it. It seems to be alive.")
    print("Suddenly, you become aware of the black sword dropping calamitously upon you! In a panic, you...")
    t1 = time.time()
    print(f"a. Dodge. \nb. {correct}. \nc. Strike")
    answer = input(">> ")
    t2 = time.time()
    tt = t2 - t1
    if tt > amount:
        why_combat = ("You do not react in time, and your skull is splintered...")
        retry_combat(why_combat, spectacles_on)
    elif 'a' in answer:
        why_combat = "He is ready for your tricks this time, and he stuns you with his shield."
        retry_combat(why_combat, spectacles_on)
    elif 'b' in answer:
        ws_combat7(spectacles_on)
    elif 'c' in answer:
        why_combat = "You attempt to slip under his blow and strikes, but he is too quick."
        retry_combat(why_combat, spectacles_on)
    else:
        why_combat = "You try something incoherent, and the delay costs you your life."
        retry_combat(why_combat, spectacles_on)

def ws_combat7(spectacles_on):
    print("""
        ...lift up the necklace before you.
        A burst of lighting shines forth and an icy blast frosts over his black flames.
        The molten armor and mighty shield are covered in a frozen crust.
        The sword in your hand begins to glow a mighty orange.
        Mustering all your strength, you plunge your sword deep into his heart, piercing the black armor.
        His frozen form begins to crumble like ice and you step back, breathing heavily.
        As the sword in your hand begins to cool, you look around you.
        ...
        ...
        This room is built into the cliffside. 
        Windows afford you a majestic view of the land, as the mooon turns the sky from orange to purple.
        Everywhere you look, you see table and benches and shelves and tools.
        This must've been a mighty workshop.
        One wall is dominated by a huge forge, and swords of all shapes and sizes hang upon the walls.
        Before you a chest lies, and upon it a book.
    """)
    closet_saphire(frambers_spectacles)

def closet_saphire(frambers_spectacles):
    print("Inside the chest is a sack of coins, a sandwich that's still fresh, and a sweet helmet. You take all three")
    input("Now for the book...>> ")
    frambers_book(frambers_spectacles)
    

    
def frambers_book(frambers_spectacles):
    print("""
        You pick up the book, and open its worn pages.
    
        "This is the tale of Framber the blacksmith.
        If you are reading these words, than I am gone. Where, I can not say.

        I will start from the beginning.
        There was a beautiful town in the valley below, but on the day I arrived, it was in chaos.
        Smoke was in the air, and people were clogging the streets, yelling and screaming.
        I, a new arrival, grabbed at everyone, trying to learn of the terror.
        At last, I saw it. 
        Swooping down, its great wings creating dark shadows.
        A dragon.
        """)
    input("You turn the page...>> ")
    print(""" 
        I ran for cover as its flaming breath wreaked havoc on the streets around me. 
        Then, dodging flame and death, I made my way to the tower rising above the town.
        As I climbed its many steps, the dragon hissed and rumbled above.
        Dirt streaked my face as I stood upon the top, biding my time.
        When the dragon swooped close enough, I leapt upon his back!
        My trusty sword began its fiery glow, and I plunged it deep in the beasts head.
        Blood sprayed from his skull, and we went plunging down.
        But he was not yet ...
        ......... struck ..... ... fiery
        ... claws.............
        His heart ..........."

        The words are faded into dust.
        You close the books.
        ...
        ...

    """)
    if frambers_spectacles == True:
        print("""
        On the last page, there appears to be an inscription, written with a shimmering light.
        It reads, 'For my beloved Adina'
        ...
        """)
        end()
    else:
        end()





#End
def end():
    global lives_lost
    print("Thanks for playing Frambers Hut!")
    print(f"You lost {lives_lost} during your adventure.")
    print("Goodbye!")
    exit(0)








def hut_chest1(map_done, times_tried, scared):
    #puzzle
    print("a gnarly puzzle belongs here")
    print("a cool strand-type item belongs here")
    global cool_gem1
    global hut_chest1_done
    hut_chest1_done = True
    cool_gem1 = True
    hut_choice1(map_done, 'nonlooped', 'none', times_tried, scared)



#runit
forest()





