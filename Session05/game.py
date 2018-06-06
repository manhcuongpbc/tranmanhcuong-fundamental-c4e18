map_sokoban = {
    "size_x": 5,
    "size_y": 5
}

player = {
    "x":4,
    "y":0
}

boxes =[
    {"x":1,"y":1},
    {"x":2,"y":2},
    {"x":3,"y":3}
]

destinations = [
    {"x":2, "y":1},
    {"x":3, "y":2},
    {"x":4, "y":3}
]


playing = True
while playing:

    ########## print map

    for y in range(map_sokoban["size_y"]):
        for x in range(map_sokoban["size_x"]):

            box_is_here = False
            for box in boxes:
                if box["x"] == x and box['y'] == y:
                    # print("B ",end='')
                    box_is_here = True
                    # break

            player_is_here = False
            if x == player["x"] and y == player["y"]:
                # print("P",end='')
                player_is_here = True

            des_is_here = False
            for des in destinations:
                if des["x"] == x and des["y"] == y:
                    des_is_here = True
            if player_is_here:
                print("P ",end='')
            elif box_is_here:            
                print("B ",end='')
            elif des_is_here:
                print("D ",end='')
            else:
                print("- ",end='')
        print()

    #################end of print map

    #check win:
    win = True
    for box in boxes:
        if box not in destinations:
            win = False
    if win:
        print("You win")
        break

    dx = 0
    dy = 0
    move = input("ur move: ").lower()
    if move == "w":
        dy = -1
    elif move == "s":
        dy = 1
    elif move == "a":
        dx = -1
    elif move == "d":
        dx = 1
    else:
        playing = False
    if 0 <= player['x'] + dx < map_sokoban['size_x'] \
    and 0 <= player['y'] + dy < map_sokoban['size_y']:
        player['x'] += dx
        player['y'] += dy


    for box in boxes:
        if box['x'] == player['x'] and box['y'] == player['y']\
        and 0 <= box['x'] + dx < map_sokoban['size_x'] \
        and 0 <= box['y'] + dy < map_sokoban['size_y']:
            print(box["x"],box["y"])
            box['x'] += dx
            box['y'] += dy
            if box['x'] in [0, map_sokoban['x'] - 1] or box['y'] in [0, map_sokoban['x'] - 1]:
                player['x'] -= dx
                player['y'] -= dy

    # for box1 in boxes:
    #     new_boxes = boxes.pop(boxes.index(box1))
    #     print(new_boxes)
        # for box2 in new_boxes:
        #     if box1["x"] == box2["x"] and box1["y"] == box2["y"]:
        #         player['x'] -= dx
        #         player['y'] -= dy



