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
        print("This is book")



    


living_room(True)