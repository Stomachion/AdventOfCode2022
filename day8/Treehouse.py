import sys
from read_AoCinputs import *


def print_LOL(list_of_list:list[list]):
    print()
    for i in range(len(list_of_list)):
        for j in range(len(list_of_list[i])):
            print(list_of_list[i][j], " ", end='')
        print()  


def test_tree_visibility(trees:list[list], i: int, j: int):
    #up 
    highest = -1
    for k in range(i-1, -1, -1):
        if trees[k][j] > highest:
            highest = trees[k][j]

    if trees[i][j] > highest: 
        return True 

    #down 
    highest = -1
    for k in range(i+1, len(trees),):
        if trees[k][j] > highest:
            highest = trees[k][j]

    if trees[i][j] > highest: 
        return True 

    #right
    highest = -1
    for k in range(j+1, len(trees[i])):
        if trees[i][k] > highest:
            highest = trees[i][k]

    if trees[i][j] > highest: 
        return True 

    #left
    highest = -1
    for k in range(j-1, -1, -1):
        if trees[i][k] > highest:
            highest = trees[i][k]

    if trees[i][j] > highest: 
        return True

    return False


def compute_scenic_score(trees:list[list], i: int, j: int):
    scenic_score = 1

    #up 
    nr_trees = 0
    for k in range(i-1, -1, -1):
        nr_trees += 1
        if trees[i][j] <= trees[k][j]:
            break
    scenic_score *= nr_trees 

    #down
    nr_trees = 0
    for k in range(i+1, len(trees)):
        nr_trees += 1
        if trees[i][j] <= trees[k][j]:
            break
    scenic_score *= nr_trees 

    #left 
    nr_trees = 0
    for k in range(j-1, -1, -1):
        nr_trees += 1
        if trees[i][j] <= trees[i][k]:
            break
    scenic_score *= nr_trees 

    #right
    nr_trees = 0
    for k in range(j+1, len(trees)):
        nr_trees += 1
        if trees[i][j] <= trees[i][k]:
            break
    scenic_score *= nr_trees 
    return scenic_score


def compute_max_scenic_score(trees:list[list]):
    max_score = 0
    scenic_score = 0
    for i in range(len(trees)):
        for j in range(len(trees[i])):
            scenic_score = compute_scenic_score(trees, i, j)
            if scenic_score > max_score:
                max_score = scenic_score
    return max_score


def test_visibility(trees:list[list]):

    nr_lines = trees.shape[0]
    nr_cols = trees.shape[1]
    visible_trees = [[False]*nr_cols for i in range(nr_lines) ]

    for i in range(nr_lines):
        for j in range(nr_cols):
            visible_trees[i][j] = test_tree_visibility(trees,i,j)
    return visible_trees


def count_visible_trees(visible_trees):
    count = 0
    for i in range(len(visible_trees)):
        for j in range(len(visible_trees[i])):
            if visible_trees[i][j]:
                count += 1
    return count

# Defining main function
def main():
    
    tree_file = str(sys.argv[1])
    trees = read_txt_matrix(tree_file)
    #print_LOL(trees)

    visible_trees = test_visibility(trees)
    nr_visible_trees = count_visible_trees(visible_trees)

    print("There are ", nr_visible_trees, " trees visible.")

    max_scenic_score = compute_max_scenic_score(trees)
    print("Maximum Scenic Score is ", max_scenic_score)

    print()


# main
if __name__=="__main__":
    main()