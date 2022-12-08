yes = 'Yes' 'yes' 'Y' 'y' 'ya' 'Ya'
no = 'No' 'no' 'n' 'N' 'na' 'Na'
a = 'a' 'A' 
b = 'b' 'B'
c = 'c' 'C'
#delete line on import
map_done = True

def living_room(map_done):
    print("""
    You walk inside the house.
    Everything is covered in a thick layer of dust.
    The sunlight wriggles through the windows, tinted green by the mildew.
    *cough* *cough*
    Before you lies a table. To your right, along the wall, a shelf stands. 
    The room recedes in to the deeper shadows, but at the far end, just beyond two saggy chairs,
    the faint outline of a door is visible.
    To your left, there is another door, old and wooden.
     """)
    living_room_choice1(map_done, False, False, 0)



def living_room_choice1(map_done, table_done, shelf_done, tries):
    print("What do you want to do?")
    choice = input(">> ")
    choice = choice.strip(); choice = choice.casefold()
    #table = 'table', 'check table', 'check the table', 'see table', 'see the table'
    #shelf = 'shelf', 'check'
    if 'table' in choice and table_done == False:
        print("You walk towards the table.")
        print("""
    The table is made of a dark walnut wood, full of deep grooves and cuts.
    There's piles of open books and 2 or 3 empty glasses.
    A pair of bronze spectacles lies upon a yellowed parchment, as though someone had just taken them off.
    There's a silver tipped pen, lying in a little puddle of ink upon the parchment.
    Something is lying underneath it all.""")
        living_room_table(map_done, False, False, False, False)
    elif 'table' in choice and table_done == True:
        print("You already checked out the table, see what else you can find.")
        living_room_choice1(map_done, table_done, shelf_done)
    elif 'shelf' in choice and shelf_done == False:
        print("You head to the shelf to see if there's anything cool.")
        print("There's nothing but a dusty old jar, and a book entitled: 'How to Maintain your Personal Gorbel'")
        print("You consider what a 'Gorbel' is, and turn back around to see what else there is in the room.")
        living_room_choice1(map_done, table_done, shelf_done)
    elif 'shelf' in choice and shelf_done == True:
        print("There's nothing more to see on the shelf.")
        living_room_choice1(map_done, table_done, shelf_done)
    elif tries <= 2:
        print("That's not something you can do. Try to pick something else.")
        tries += 1
        living_room_choice1(map_done, table_done, shelf_done, tries)
    else:
        print("That's not something you can do. Try to pick something else.")
        print("HINT: try 'table', 'shelf', 'left door' or 'straight'.")
        living_room_choice1(map_done, table_done, shelf_done, tries)


def living_room_table(map_done, book_done, spectacle_done, parchment_done, sword_done):

    choice = input("\nWhat do you want to examine?\n>> ")
    choice = choice.strip(); choice = choice.casefold()
    if 'book' in choice and book_done == False:
        print("These books all seem to be written in a different language.")
        print("One book has a picture of a majestic castle on the cover.")
        print("Another is deep green with brass fittings on the corners.")
        print("There's nothing useful to get from these books.")
        book_done = True
        living_room_table(map_done, book_done, spectacle_done, parchment_done, sword_done)
    elif 'spectacle' in choice and spectacle_done == False:
        print("""
        You pick up the spectacles to examine them more closely.
        They have thickly scratched lenses and the wire frames are a deeply bronze and bent.
        You try them on, and now everything looks dusty and tinged by yellow.
        They seem useful.
        """)
        choice_s = input("Do you want to keep them?\n>> ")
        if yes in choice:
            global have_spectacles
            have_spectacles = True
            spectacle_done = True
            living_room_table(map_done, book_done, spectacle_done, parchment_done, sword_done)
        else:
            print("You put the spectacles back on the table and look at the other things on the table.")
            spectacle_done = True
            living_room_table(map_done, book_done, spectacle_done, parchment_done, sword_done)
    elif 'parchment' in choice and parchment_done == False:
        print("""
        You gently lift the parchment from the table to get a better look...
        ..........................
        The parchment is quite old and begins to crumble in your hand...
        You make out some words, names perhaps?
        There's a 'Jesse'...
        and maybe a 'Arthur'?
        The parchment is gone now, part of the dust.
        """)
        parchment_done = True
        living_room_table(map_done, book_done, spectacle_done, parchment_done, sword_done)
    elif 'underneath' in choice or 'table' in choice and sword_done == False:
        print("You clear everything off, and underneath is a sweet sword.")
        choice_s = input("Examine?\n>> ")
        if choice_s in yes:
            global frambers_sword
            print("""
            You look more closely at the blade.
            It is made of a deep grey metal, perhaps a burnt steel.
            There's a wicked swirling pattern etched into the blade, fine as a shimmering star.
            The handle is round, and wrapped in a carefully polished leather strap.
            There's an engraving on the handle, inlaid with a reddish gold. It says "Framber's Aqua".
            This sword is in exceptional condition.
            """)
            choice_s = input("Do you want to keep the sword?\n>> ")
            if choice in yes:
                frambers_sword = True
                sword_done = True
                living_room_table(map_done, book_done, spectacle_done, parchment_done, sword_done)
            else:
                print("Alright, you put this really cool sword back on the table.")    
                frambers_sword = False
                sword_done = True
                living_room_table(map_done, book_done, spectacle_done, parchment_done, sword_done)
        else:
            choice_s = input("Do you want to keep the sword?\n>> ")
            if choice in yes:
                frambers_sword = True
                sword_done = True
                living_room_table(map_done, book_done, spectacle_done, parchment_done, sword_done)
            else:
                print("Alright, you put this really cool sword back on the table.")    
                frambers_sword = False
                sword_done = True
                living_room_table(map_done, book_done, spectacle_done, parchment_done, sword_done)
    

    else:
        exit(0)



    


living_room(True)