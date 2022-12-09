import sys
from read_AoCinputs import *


def move_snake(snake_moves:list, snake_length: int):
    
    snake = []
    for i in range(snake_length):
        snake.append(np.array([0,0]))

    visited = set()
    visited.add(tuple(snake[snake_length-1]))
   
    for move in snake_moves:
        move = move.split()
        step = get_step(move[0])
        for i in range(int(move[1])):
            snake[0] += step
            for j in range(1,len(snake)):
                snake[j] = update_positions(snake[j-1], snake[j])    
            visited.add(tuple(snake[snake_length-1]))

    """             for i in range(len(snake)):
                print(snake[i])
            print()  """

    return visited


def update_positions(lead_seq, follow_seq):
    diff = lead_seq - follow_seq
    if np.all(np.abs(diff) < 2 ):
        return follow_seq
    else:
        update = np.where(abs(diff)==2, np.sign(diff), diff)
        follow_seq += update
        return  follow_seq
        
    """         update = np.where(abs(diff)<2, diff, np.sign(diff))
        print("update", update)
         """
    """     match diff:
        case _ if 2 in diff:
            index = np.where(diff==2)
            diff[index] = 1
        case _ if -2 in diff:
            index = np.where(diff==-2)
            diff[index] = -1
        case other:
            diff = np.array([0,0]) 
    follow_seq += diff
    return follow_seq """


def get_step(direction: str):
    match direction:
        case "R":
            return np.array([1, 0])
        case "L":
            return np.array([-1, 0])
        case "U":
            return np.array([0, 1])
        case "D":
            return np.array([0, -1])


# Defining main function
def main():
    
    snake_file = str(sys.argv[1])
    snake_moves = read_txt_list(snake_file)

    visited = move_snake(snake_moves, 2)
    print("2-Snake's Tail visited ", len(visited), "tiles")

    visited = move_snake(snake_moves, 10)
    print("10-Snake's Tail visited ", len(visited), "tiles")


# main
if __name__=="__main__":
    main()