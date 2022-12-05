import sys
from typing import List
import copy

def read_txt_list(txt_file_name):
    txt_file = open(txt_file_name, "r")
    
    txt_list = []
    for line in txt_file:
        txt_list.append(line.rstrip())
    
    txt_file.close()
    return txt_list 


def get_create_stacks(crane_list: str):
    
    base_line = get_base_line(crane_list)
    nr_stracks = get_stack_number(crane_list[base_line])
    crate_stacks = [[] for i in range(nr_stracks)]

    for i in range(base_line-1,-1, -1):
        crate_line = crane_list[i]
        for stack in range(0,nr_stracks):
            index = 1+4*stack
            if index < len(crate_line):
                crate = crate_line[1+4*stack]
                if crate != " ":
                    crate_stacks[stack].append(crate) 
    
    return crate_stacks


def perform_reordering(crane_list, crate_stacks):
    
    first_line = get_first_command_line(crane_list)
    for line_nr in range(first_line, len(crane_list)):
        command = crane_list[line_nr].split(" ")
        execute_command(command, crate_stacks)



def execute_command(comand_line: List[str], crate_stacks):
    number_creates, origin, destination = extract_command(comand_line)
    for i in range(number_creates):
        crate = crate_stacks[origin].pop()
        crate_stacks[destination].append(crate)


def perform_reordering2(crane_list, crate_stacks):
    
    first_line = get_first_command_line(crane_list)
    for line_nr in range(first_line, len(crane_list)):
        command = crane_list[line_nr].split(" ")
        execute_command2(command, crate_stacks)


def execute_command2(comand_line: List[str], crate_stacks):
    number_creates, origin, destination = extract_command(comand_line)
    crates = crate_stacks[origin][-number_creates:]
    del crate_stacks[origin][-number_creates:]
    crate_stacks[destination] +=  crates

def extract_command(comand_line: List[str]):
    number_creates = int(comand_line[1])
    origin = int(comand_line[3])-1
    destination = int(comand_line[5])-1

    return number_creates, origin, destination

def get_top_crates(crate_stacks):
    top_crates = str()
    for i in range(len(crate_stacks)):
        top_crates += crate_stacks[i][-1]
    return top_crates


def get_base_line(crane_list: str):
    
    for i in range(len(crane_list)):
        if crane_list[i].startswith(" 1"):
            return i
    # Error: Exception Handeling in python
    return -1


def get_first_command_line(crane_list: str):
    return get_base_line(crane_list)+2


def get_stack_number(crate_base: str):
    crate_base = crate_base.strip()
    return int(crate_base[-1])



# Defining main function
def main():
    
    crane_file = str(sys.argv[1])
    crane_list = read_txt_list(crane_file)

    crate_stacks = get_create_stacks(crane_list)
    crate_stacks2 = copy.deepcopy(crate_stacks)

    perform_reordering(crane_list, crate_stacks)
    print("Top crates after reordering")
    print(get_top_crates(crate_stacks)) 

    perform_reordering2(crane_list, crate_stacks2)
    print("Top crates after reordering")
    print(get_top_crates(crate_stacks2))

# main
if __name__=="__main__":
    main()