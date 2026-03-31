from room import Room
from item import Item
from character import Character
from character import Enemy

Ball = Item("Ball")
Ball.set_description("An air filled, spherical object that can roll and be kicked")

kitchen = Room("Kitchen")
kitchen.set_description("A dark room with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A well lit room with a fine wooden rectangular table in the middle.")

ballroom = Room("Ballroom")
ballroom.set_description("A large and luxurious room with high ceiling.")


kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Grrrrrr...")
dave.set_weakness("Cheese")

print("\n")
dining_hall.get_details()

current_room = kitchen
while True:
    print("\n")
    current_room.get_details
    command = input("> ").lower()
    current_room = current_room.move(command)
    print('Player is now in room:', current_room.name)



