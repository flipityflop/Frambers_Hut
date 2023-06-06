from sys import exit 

yes = 'Yes' 'yes' 'Y' 'y' 'ya' 'Ya'
no = 'No' 'no' 'n' 'N' 'na' 'Na'
a = 'a' 'A' 
b = 'b' 'B'
c = 'c' 'C'
#delete line on import
#Collected items
gg_diary_note = False
gator_statue = False
hut_chest1_done = False
sandwich = False

map_done = True

def dead(why):
    global lives_lost
    #lives_lost += 1
    print(why, "You're dead. \nDo you wanna try again?")
    choice = input("Yes or no?>> ")
    if choice in yes:
        print("go")
        path_to_gators(True)
    else:
        print(f"Thanks for playing, you lost {lives_lost} lives in your journey through Framber's Hut. \nGoodbye!")
        exit(0)

def hut(map_done):
    print("sucess")
    exit(0)

#Path to them gators


def path_to_gators(map_done):
    print("""
    You walk carefully along a muddy path, that slowly winds past the house and off to to right,
    back into the woods.
    As you continue along, your boots slurp in the muds,
    and the dense forest on either side slowly gives way to pools of water.
    Tall grasses stick out amidst the massive and gnarled tress,
    reigning like kings within their own small water kigndom.
    You think you see a log with yellow eyes, but turns it it was just a evil looking gator.
    You've reached the end of the path, and you find yourself before a boggy pool, silently surging with gators.
    You spot something semi-submerged in the water, about 10 feet out.
    Moss and algae are growing on it.
    """)
    gator_pool(map_done, False, 0)

def gator_pool(map_done, fishing_hook, looked_nu):
#    fishing_hook = False
    choice = input("What do you do?>> ")
    if "look" in choice and looked_nu < 3:
        print("You see a few different things.\n\t*A. A fishing rod with a hook.\n\t*B. A boat.\n\t*C. A sandwich.")
        looked_nu += 1
        gator_pool(map_done, fishing_hook, looked_nu)
    elif "look" in choice and looked_nu == 3:
        print("Bud, stop stalling. You've seen what there is to see. Do something.")
        looked_nu += 1
        gator_pool(map_done, fishing_hook, looked_nu)
    elif "look" in choice and looked_nu == 4:
        print("""Bud, stop stalling. You've seen what there is t...
    ...
    o.
    Theres's a old note on the ground, directly in front of you.
    You open it and it reads: 
    'Today I decided to throw my sweet gator statue into the water. 
    It was a tough decision, but its clearly alive and has tried to eat me various times.
    Still, it was a sweet statue. The cursed red eyes were my favorite.'
    You put the note in your pocket.""")
        global gg_diary_note
        gg_diary_note = True
        looked_nu += 1 
        gator_pool(map_done, fishing_hook, looked_nu)
    elif "look" in choice and looked_nu > 4:
        print("You see the same 3 things that you saw before.\n\t*A. A fishing rod with a hook.\n\t*B. A boat.\n\t*C. A sandwich.")
        print("There's nothing else. Stop.")
        gator_pool(map_done, fishing_hook, looked_nu)
    elif fishing_hook == False and choice in a or "hook" in choice or "rod" in choice:
        print("You grab the hook and rod. You're too far from the statue to try and hook it.")
        fishing_hook = True
        gator_pool(map_done, fishing_hook, looked_nu)
    elif fishing_hook == True and choice in a or "hook" in choice or "rod" in choice:
        print("You already have the fishing hook, what are you gonna do about it?")
        gator_pool(map_done, fishing_hook, looked_nu)
    elif choice in b or "boat" in choice:
        gg_boat(map_done, fishing_hook, looked_nu)
    elif choice in c or "sandwich" in choice and sandwich == False:
        print("You pick up the sandwich.")
        choice = input("Do you A. want to keep, or B. feed the sandwich to the gators?\n>> ")
        if choice in a or choice in "keep":
            print("A delightful jingle plays, and you jump and hold the sandwich aloft.")
            print("A little box pops up that says 'A tuna fish sandwich. This is the most powerful item in the game'")
            print("That was neat. Anyway, you eat the sandwich and it is quite tasty.")
            #global sandwich
            sandwich = True
            gator_pool(map_done, fishing_hook, looked_nu)
        else:
            print("""
            Why? 
            Why would you try to feed a sandwich to a murky pool of terrifying gators?
            Why?
            Anyway, you bend down to feed some sandwich, and you instantly are chomped upon by a horde of vicious, yellow eyed monsters.
            Good job.""")
            dead("You tried to feed gators, jesus christ.")
    elif choice == 3 or "sandwich" in choice and sandwich == True:
        print("You already got the sandwich. Try something else")
        gator_pool(map_done, fishing_hook, looked_nu)
    else:
        print("What does that mean? Try do something clever or even coherent.")
        gator_pool(map_done, fishing_hook, looked_nu)
            

def gg_boat(map_done, fishing_hook, looked_nu):
    print("You spot an ancient and quite trusty looking wooden rowboat.\nAs you climb in, a particularly meaty looking gator give you a knowing snarl\nThis is seems vaguely unwise.")
    choice = input("Do you want to give it a shot?>> ")
    if choice in yes:
        print("You row towards the object. As you get closer, you begin to see that it is a wicked gator statue with reddish glowing jewels for eyes.")
        choice = input("Do you want to grab it? btw, that meaty gator is lying nearby, his mouth open, just waiting.\nYes or no?>> ")
        if choice in yes:
            print("The second you reach your hand out of the boat, the gator lunges up and literally pulls you under water, while biting your arm off.")
            dead("You spend your final seconds grasping for breath and being chomped by gator.")
        else:
            print("Good choice. The gator looks particularly unhappy. Any other ideas?")
            choice = input(">> ")
            if choice in no:
                print("Alright, you row boack to shore.")
                gator_pool(fishing_hook, looked_nu)
            elif fishing_hook == True and "hook" in choice or "rod" in choice or "fishing" in choice:
                print("""
        From this distance, you can easily snag an tooth on the gator statue.
        You firmly wedge the hook in a the ring for the oar and begin to row backwards.
        With a delightful squelch, the gator slowly slinks up from the mud,
        water and green sliding down from its mouth.
        The gators in the watermove about in a frenzy, but you're not in some kind of flimsy boat.
        You head back to shore with the figurine in tow, and you pull the beautiful, glowing eyed statue on to dry land.
                """)
                print("You head back towards the house.")
                #global gator_statue
                gator_statue = True
                hut(map_done)
            elif fishing_hook == False and "hook" in choice or "rod" in choice or "fishing" in choice:
                print("You dont have anything to grab it with. There was something on shore, I think.")
                print("You head back to shore.")
                gator_pool(map_done, fishing_hook, looked_nu)
            else:
                print("Well, I guess you should head back to shore.")
                gator_pool(map_done, fishing_hook, looked_nu)
    else:
        print("Ok")
        gator_pool(map_done, fishing_hook, looked_nu)            


path_to_gators(map_done)