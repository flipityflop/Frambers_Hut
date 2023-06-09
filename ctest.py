from sys import exit 
import time
import random


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
frambers_spectacles = False
frambers_sword = False

map_done = True
lives_lost = 0

def dead(why):
    global lives_lost
    #lives_lost += 1
    print(why, "You're dead. \nDo you wanna try again?")
    choice = input("Yes or no?>> ")
    if choice in yes:
        print("go")
        ws_combat1(True)
    else:
        print(f"Thanks for playing, you lost {lives_lost} lives in your journey through Framber's Hut. \nGoodbye!")
        exit(0)

def hut(map_done):
    print("sucess")
    exit(0)


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



#closet_saphire(True)
path_to_gators(True)

