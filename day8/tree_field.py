from dataclasses import dataclass
from read_AoCinputs import *

@dataclass
class Tree:
    hight: int = 0
    highest_up: int = 0
    highest_down: int = 0
    highest_left: int = 0
    highest_right: int = 0
    visible: bool = True

def create_tree_field(tree_file):

    tree_list = read_txt_list(tree_file)
    nr_lines = len(tree_list)
    nr_cols = len(tree_list[0])
    tree_field = [[Tree()]*nr_cols for i in range(nr_lines) ]

    for i in range(0, nr_lines):
        for j in range(0, nr_cols):
            tree_field[i][j].hight=int(tree_list[i][j])

    return tree_field


def compute_visibility(tree_field: list[list[Tree]]):
   
    nr_lines = len(tree_field)
    nr_cols = len(tree_field[0])

    for j in range(1, nr_cols-1):
        highest = int(0)
        for i in range(1, nr_lines-1):
            if highest < tree_field[i-1][j].hight:
                highest = tree_field[i-1][j].hight
            tree_field[i][j].highest_up = highest




