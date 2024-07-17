def show_instructions():
    print("Text-Based Adventure Game")
    print("Commands:")
    print("  go [direction]")
    print("  get [item]")
    print()

def show_status():
    print("---------------------------")
    print(f"You are in the {current_room}")
    print("Inventory:", inventory)
    print(f"Exits: {', '.join(rooms[current_room].keys())}")
    if "item" in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")
    print("---------------------------")

rooms = {
    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'item': 'key',
    },
    'Kitchen': {
        'north': 'Hall',
        'item': 'monster',
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'item': 'potion',
    },
    'Garden': {
        'north': 'Dining Room'
    }
}

inventory = []
current_room = 'Hall'

show_instructions()

while True:
    show_status()

    move = input(">").lower().split()

    if move[0] == 'go':
        if move[1] in rooms[current_room]:
            current_room = rooms[current_room][move[1]]
        else:
            print("You can't go that way!")

    if move[0] == 'get':
        if "item" in rooms[current_room] and move[1] == rooms[current_room]['item']:
            inventory.append(move[1])
            print(f"{move[1]} got!")
            del rooms[current_room]['item']
        else:
            print(f"Can't get {move[1]}!")

    if 'item' in rooms[current_room] and 'monster' in rooms[current_room]['item']:
        print("A monster has got you... GAME OVER!")
        break

    if current_room == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print("You escaped the house... YOU WIN!")
        break
