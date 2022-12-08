import numpy as np

def read_txt_list(txt_file_name):
    txt_file = open(txt_file_name, "r")
    
    txt_list = []
    for line in txt_file:
        txt_list.append(line.rstrip())
    
    txt_file.close()
    return txt_list 


def read_txt_matrix(txt_file_name):
    
    trees_list = read_txt_list(txt_file_name)
    nr_lines = len(trees_list)
    nr_columns = len(trees_list[0])

    trees_prematrix = []
    for i in range(0,nr_lines):
        line = []
        for j in range(0, nr_columns):
            line.append(int(trees_list[i][j]))
        trees_prematrix.append(line)
    
    return np.array(trees_prematrix)


