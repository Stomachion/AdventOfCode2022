import sys
from read_AoCinputs import *


def move_snake(snake_moves:list):
    
    head_pos = np.array([0,0])
    tail_pos = np.array([0,0])
    visited = set()
    visited.add(tuple(tail_pos))

    for move in snake_moves:
        move = move.split()
        step = get_step(move[0])
        for i in range(int(move[1])):
            head_pos, tail_pos = update_postions(head_pos, tail_pos, step)    
            visited.add(tuple(tail_pos))

    return visited



def update_postions(head_pos, tail_pos, step:np.array):
    head_pos += step
    diff = head_pos - tail_pos
    match diff:
        case _ if 2 in diff:
            index = np.where(diff==2)
            diff[index] = 1
        case _ if -2 in diff:
            index = np.where(diff==-2)
            diff[index] = -1
        case other:
            diff = np.array([0,0])
    tail_pos += diff
    return head_pos, tail_pos

def get_step(direction: str):
    match direction:
        case "R":
            return np.array([1, 0])
        case "L":
            return np.array([-1, 0])
        case "U":
            return  np.array([0, 1])
        case "D":
            return np.array([0, -1])

# Defining main function
def main():
    
    snake_file = str(sys.argv[1])
    snake_moves = read_txt_list(snake_file)

    visited = move_snake(snake_moves)
    print("Tail visited ", len(visited), "tiles")


# main
if __name__=="__main__":
    main()