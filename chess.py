from array import *

basic_chess = [[1,1,2,1,0], [1,1,1,0,1], [1,0,0,1,1], [0,1,0,1,1],[1,1,1,0,0]]

def move(direction, chess):
    index = 0
    pos1 = 0
    pos2 = 0
    for array in chess:
        try:
            pos2 = array.index(2)
            pos1 = index
        except:
            index += 1
    match direction:
        case "left":
            if(basic_chess[pos1][pos2] == 2):
                chess[pos1][pos2] = "S"
            else:
                chess[pos1][pos2] = basic_chess[pos1][pos2]
            chess[pos1][pos2 - 1] = 2
            return chess
        case "right":
            if(basic_chess[pos1][pos2] == 2):
                chess[pos1][pos2] = "S"
            else:
                chess[pos1][pos2] = basic_chess[pos1][pos2]
            chess[pos1][pos2 + 1] = 2
            return chess
        case "down":
            if(basic_chess[pos1][pos2] == 2):
                chess[pos1][pos2] = "S"
            else:
                chess[pos1][pos2] = basic_chess[pos1][pos2]
            chess[pos1 + 1][pos2] = 2
            return chess
        case "top":
            if(basic_chess[pos1][pos2] == 2):
                chess[pos1][pos2] = "S"
            else:
                chess[pos1][pos2] = basic_chess[pos1][pos2]
            chess[pos1 - 1][pos2] = 2
            return chess

def get_symbole(chess):
    index = 0
    pos1 = 0
    pos2 = 0
    for array in chess:
        try:
            pos2 = array.index(2)
            pos1 = index
        except:
            index += 1
    return basic_chess[pos1][pos2]

def print_chess(chess):
    for r in chess:
            for c in r:
                print(c,end = " ")
            print("")

if __name__ == '__main__':
    move_chess = [[1,1,2,1,0], [1,1,1,0,1], [1,0,0,1,1], [0,1,0,1,1],[1,1,1,0,0]]
    i=0

    move_chess = move("left", move_chess)
    move_chess = move("right", move_chess)
    move_chess = move("right", move_chess)

    while(i < 6):
        if get_symbole(move_chess) == 0:
            move_chess = move("top", move_chess)
        else:
            move_chess = move("down", move_chess)
        i+=1
     
    print_chess(move_chess)