import sys
from AoCTree import *



def create_file_system(file_system_list: list[str]):
    pass


# Defining main function
def main():
    
    file_system_file = str(sys.argv[1])
    file_system = AoCTree(file_system_file)
    
    
    file_system.print_tree()
    print()

    sum_max_size_dir = file_system.sum_max_size_directories(100000)
    print("Sum Max file dir = ", sum_max_size_dir)
    print()

    disk_space = 70000000
    used_space = file_system.get_size()
    free_space = disk_space - used_space
    print("Free Space ", free_space)
    to_delete = 30000000 - free_space
    print("To be deleted", to_delete)

    file_size_to_delete = file_system.find_min_dir_min_size(to_delete)
    print("Delete ", file_size_to_delete)

# main
if __name__=="__main__":
    main()