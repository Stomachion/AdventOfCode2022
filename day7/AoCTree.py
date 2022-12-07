from read_AoCinputs import read_txt_list

class AoCNode:

    def __init__(self, name: str, parent = None, size: int = 0 ):
        self.__name = name
        self.__parent = parent
        self.__size = size
        self.__children = []

    def add_child(self, name: str, parent, size: int = 0):
        self.__children.append(AoCNode(name, parent, size))

    def get_child(self, name: str):
        for child in self.__children:
            if child.__name == name:
                return child
        return None
    
    def get_parent(self):
        return self.__parent

    def print_tree(self, depth:int = 0):
        output = depth*" " + "-" + self.__name  \
                 + " size=" + str(self.__size)
        print(output)
        for child in self.__children:
            child.print_tree(depth+1)

    def compute_size(self):
        for child in self.__children:
            child.compute_size()
            self.__size += child.__size
            
    def get_size(self):
        return self.__size

    def sum_max_size_directories(self, max_size: int):
        sum = 0
        if 0 < len(self.__children):
            if self.__size <= max_size:
                sum += self.__size
            for child in self.__children:
                sum += child.sum_max_size_directories(max_size)
        return sum

    def find_all_dir_min_size(self, min_size: int, dir_sizes: list):
        if 0 < len(self.__children):
            if self.__size >= min_size:
                dir_sizes.append(self.__size)
            for child in self.__children:
                child.find_all_dir_min_size(min_size, dir_sizes)

class AoCTree:

    def __init__(self, input_file:list):

        file_system_list = read_txt_list(input_file)
        line_number = int(0)
        line = file_system_list[line_number].split()

        self.__root = AoCNode(line[2])
        current_node = self.__root
        line_number += 1

        while line_number < len(file_system_list):
            line = file_system_list[line_number].split()
            match line:
                case _ if "cd" in line and not ".." in line :
                    current_node = current_node.get_child(line[2])
                case _ if "cd" in line and ".." in line :
                    current_node = current_node.get_parent()
                case _ if not "$" in line:
                    if "dir" in line:
                        current_node.add_child(line[1], current_node)
                    else:
                        current_node.add_child(line[1], current_node, int(line[0]))
            line_number += 1 

        self.__root.compute_size()  
    
    def print_tree(self):
        self.__root.print_tree()

    def sum_max_size_directories(self, max_size: int):
        return self.__root.sum_max_size_directories(max_size)

    def find_min_dir_min_size(self, min_size):
        dir_sizes = []
        self.__root.find_all_dir_min_size(min_size, dir_sizes)
        return min(dir_sizes)

    def get_size(self):
        return self.__root.get_size()
