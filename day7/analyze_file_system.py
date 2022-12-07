import sys
from AoCNode import AoCNode

def read_txt_list(txt_file_name):
    txt_file = open(txt_file_name, "r")
    
    txt_list = []
    for line in txt_file:
        txt_list.append(line.rstrip())
    
    txt_file.close()
    return txt_list 

def create_file_system(file_system_list: list[str]):
    pass


# Defining main function
def main():
    
    file_system_file = str(sys.argv[1])
    file_system_list = read_txt_list(file_system_file)

    file_system = AoCNode("/")
    file_system.add_child("a")

    file_system.print_tree()

# main
if __name__=="__main__":
    main()