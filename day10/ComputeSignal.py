import sys
from read_AoCinputs import *
import numpy as np

def analyse_signal(signal: list):
    cycle = 1
    x = 1
    s_cycle = 20
    output = []

    for instruction in signal:
        instruction = instruction.split()

        match instruction:
            case _ if "noop" in instruction:
                s_cycle = do_special(cycle, s_cycle, output, x)
                cycle += 1
                pixel_pos = [cycle // 40, cycle % 40]
            case _ if "addx" in instruction:
                s_cycle = do_special(cycle, s_cycle, output, x)
                cycle += 1
                s_cycle = do_special(cycle, s_cycle, output, x)
                cycle += 1
                x += int(instruction[1])
    
    return np.sum(output)


def do_special(cycle:int, special:int, output:list, x):
    if cycle == special:
        output.append(x*cycle)
        special += 40
    return special


def set_pixel(signal: list):
    cycle = 1
    x = 1
    sprite = [0,1,2]
    pixel_pos = [0,0]
    screen = [["."]*40 for i in range(6)]

    for instruction in signal:
        instruction = instruction.split()

        match instruction:
            case _ if "noop" in instruction:
                pixel_pos = get_pixel_pos(cycle)
                print_pixel(pixel_pos, sprite, screen)
                cycle += 1
            case _ if "addx" in instruction:

                pixel_pos = get_pixel_pos(cycle)
                print_pixel(pixel_pos, sprite, screen)
                cycle += 1

                pixel_pos = get_pixel_pos(cycle)
                print_pixel(pixel_pos, sprite, screen)
                cycle += 1

                x += int(instruction[1])
                sprite = [x-1, x, x+1]
    return screen


def get_pixel_pos(cycle):
    col = (cycle -1) % 40
    line = (cycle -1) // 40
    return [line,col]


def print_pixel(pixel_pos:list, sprite:list, screen:list):
    if sprite[0] <= pixel_pos[1] and sprite[2] >= pixel_pos[1]:
        screen[pixel_pos[0]][ pixel_pos[1]] = "#"


def print_screen(screen:list):
    print()
    for i in range(len(screen)):
        for j in range(len(screen[i])):
            print(screen[i][j], end = "")
        print()


# Defining main function
def main():
    
    signal_file = str(sys.argv[1])
    signal = read_txt_list(signal_file)

    result = analyse_signal(signal)
    print("Result is ", result)

    screen = set_pixel(signal)
    print_screen(screen)


    


# main
if __name__=="__main__":
    main()