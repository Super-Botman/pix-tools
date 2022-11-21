from array import *

basic_chess = [[0,0,0,1,2], ['P',1,2,3,2], [0,3,4,0,0], [0,0,1,2,0],[0,0,4,4,0]]

def move(direction, chess):
    index = 0
    pos1 = 0
    pos2 = 0
    for array in chess:
        try:
            pos2 = array.index('P')
            pos1 = index
        except:
            index += 1
    match direction:
        case "left":
            if(basic_chess[pos1][pos2] == 'P'):
                chess[pos1][pos2] = 'S'
            else:
                chess[pos1][pos2] = basic_chess[pos1][pos2]
            chess[pos1][pos2 - 1] = 'P'
            return chess
        case "right":
            if(basic_chess[pos1][pos2] == 'P'):
                chess[pos1][pos2] = 'S'
            else:
                chess[pos1][pos2] = basic_chess[pos1][pos2]
            chess[pos1][pos2 + 1] = 'P'
            return chess
        case "down":
            if(basic_chess[pos1][pos2] == 'P'):
                chess[pos1][pos2] = "S"
            else:
                chess[pos1][pos2] = basic_chess[pos1][pos2]
            pos1 = pos1 == 5 if -1 else pos1
            chess[pos1 + 1][pos2] = 'P'
            return chess
        case "top":
            if(basic_chess[pos1][pos2] == 'P'):
                chess[pos1][pos2] = "S"
            else:
                chess[pos1][pos2] = basic_chess[pos1][pos2]
            chess[pos1][pos2] = 'P'
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
    move_chess = [[0,0,0,1,2], ['P',1,2,3,2], [0,3,4,0,0], [0,0,1,2,0],[0,0,4,4,0]]
    
    i=0
    move_chess = move("right", move_chess)

    while(i < 247):
        if get_symbole(move_chess) == 3 :
            move_chess = move("top", move_chess)
        elif get_symbole(move_chess) == 3 :
            move_chess = move("right", move_chess)
        elif get_symbole(move_chess) == 2 :
            move_chess = move("down", move_chess)
        elif get_symbole(move_chess) == 4 :
            move_chess = move("left", move_chess)
        i+=1
    move_chess = move("top", move_chess)
    move_chess = move("right", move_chess)
    move_chess = move("top", move_chess)

    print_chess(move_chess)