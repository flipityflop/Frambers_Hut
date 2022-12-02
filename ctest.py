yes = 'Yes' 'yes' 'Y' 'y' 'ya' 'Ya'
no = 'No' 'no' 'n' 'N' 'na' 'Na'
a = 'a' 'A' 
b = 'b' 'B'
c = 'c' 'C'
#delete line on import
map_done = True

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
