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


def find_start_marker(signal: str, length: int):
    for i in range(length,len(signal)+1):
        sequence = set(signal[i-length:i])   
        if len(sequence) == length: 
            return i  
    # error
    return -1

# Defining main function
def main():
    
    signal_file = str(sys.argv[1])
    signal = read_txt_list(signal_file)

    first_marker = find_start_marker(signal[0], 14)
    print("First marker after character ", first_marker)

# main
if __name__=="__main__":
    main()