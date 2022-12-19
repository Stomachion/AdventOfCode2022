import sys
from read_AoCinputs import read_txt_list 


# Defining main function
def main():
    
    rock_file = str(sys.argv[1])
    rocks = read_txt_list(rock_file)


# main
if __name__=="__main__":
    main()