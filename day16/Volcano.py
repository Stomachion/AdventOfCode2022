import sys
from read_AoCinputs import read_txt_list 
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
import numpy as np
from dataclasses import dataclass

def get_node_dictionary(input_list:list):
    node_names = dict()
    for i in range(len(input_list)):
        line = input_list[i].split()
        node_names[line[1]] = i
    return node_names


def get_flow_rates(input_list:list):
    flow_rates = []
    for i in range(len(input_list)):
        line = input_list[i].split()
        flow_rates.append(int(line[4][5:-1]))
    return flow_rates


def get_neighbour_list(input_list:list):
    neighbours = [[] for i in range(len(input_list))]
    for i in range(len(input_list)):
        line = input_list[i].split()
        for j in range(9,len(line)):
            word = line[j]
            if "," in word:
                neighbours[i].append(word[0:-1])
            else:
                neighbours[i].append(word)

    return neighbours


def create_graph(node_names:list, neighbours:list):
    nr_nodes = len(node_names)
    graph = [[0]*nr_nodes for i in range(nr_nodes)]
    for i in range(nr_nodes):
        for neighbour in neighbours[i]:
            graph[i][node_names[neighbour]] = 1
    return graph


@dataclass
class PressurePath:
    current_node: int
    rest_time: int
    total_pressure: int
    to_open: np.array
    # part 2
    elephant_node: int
    elephant_time: int

def get_pressure(ppath:PressurePath):
    return ppath.total_pressure


class VolcanoSystem:

    def __init__(self, tunnel_file:str):
        volcano_file = str(sys.argv[1])
        volcano_list = read_txt_list(volcano_file)

        self.__node_names = get_node_dictionary(volcano_list)
        self.__flow_rates = get_flow_rates(volcano_list)
        self.__neighbours = get_neighbour_list(volcano_list)

        system_graph = create_graph(self.__node_names, self.__neighbours)
        system_graph = csr_matrix(system_graph)

        self.__dist_matrix = dijkstra(csgraph=system_graph,directed=False)
        self.__working_paths = []
        self.__finished_paths = []


    def compute_paths(self):
        self.init_pressure_pass_search(30,0)
        while len(self.__working_paths)>0:
            path = self.__working_paths.pop()
            self.update_step(path,"you")


    def elephant_helps(self):

        iter = 0
        self.init_pressure_pass_search(26,26)
        while len(self.__working_paths)>0:

            paths = self.__working_paths
            self.__working_paths = []
            while len(paths)>0:
                path = paths.pop()
                self.update_step(path, "you")

            paths = self.__working_paths
            self.__working_paths = []
            while len(paths)>0:
                path = paths.pop()
                self.update_step(path, "elephant")

            # to reduce workload, disregard the lower half of tested path
            # can go wrong if cut of starts to early or cuts of too much. 
            # parmeter are trial by error for now
            self.order_paths()
            iter += 1
            divider = 2
            if iter >1:
                self.__working_paths = self.__working_paths[0:len(self.__working_paths)//divider]


    def order_paths(self):
        self.__working_paths.sort(reverse=True, key=get_pressure)
        self.__finished_paths.sort(reverse=True, key=get_pressure)


    def find_best_path(self):
        max = 0
        idx = 0
        for i,path in enumerate(self.__finished_paths):
            if path.total_pressure > max:
                max = path.total_pressure
                idx = i
        return max, idx

    def init_pressure_pass_search(self, time, eletime):
        self.__working_paths.append(PressurePath(self.__node_names["AA"], \
                                    time, 0, self.__flow_rates, \
                                    self.__node_names["AA"],eletime))


    def update_step(self, path, seeker):
        match seeker:
            case "you":
                paths = self.update_path(path,"you")
                self.sort_path(paths)
            case "elephant":
                elepaths = self.update_path(path,"elephant")
                self.sort_path(elepaths)


    def update_path(self, path: PressurePath, seeker):
        match seeker:
            case "you":
                pressure_time = path.rest_time - 1 - np.array(self.__dist_matrix[path.current_node])
            case "elephant":
                pressure_time = path.elephant_time - 1 - np.array(self.__dist_matrix[path.elephant_node])

        pressure_release = pressure_time * np.array(path.to_open)
        
        non_zero_exist = False
        for i in range(len(pressure_release)): 
            non_zero_exist = non_zero_exist or pressure_release[i] > 0

        next_paths = [] 
        if non_zero_exist:
            for i in range(len(pressure_release)): 
                if pressure_release[i] > 0: 
                    next_open = np.copy(path.to_open)
                    next_open[i] = 0 
                    match seeker:
                        case "you":
                            next_paths.append(PressurePath(i, pressure_time[i], \
                                  path.total_pressure + pressure_release[i], next_open,\
                                    path.elephant_node, path.elephant_time))
                        case "elephant":
                            next_paths.append(PressurePath(path.current_node, path.rest_time, \
                                  path.total_pressure + pressure_release[i], next_open,\
                                    i, pressure_time[i]))
        else:
            match seeker:
                case "you":
                    path.rest_time = 0
                case "elephant":
                    path.elephant_time = 0
            next_paths.append(path)
        
        return next_paths

    def sort_path(self, paths):
        for path in paths:
            if path.rest_time > 0:
                self.__working_paths.append(path)
            elif path.elephant_time > 0:
                self.__working_paths.append(path)
            else:
                self.__finished_paths.append(path)


##################################################################

# Defining main function
def main():
    
    volcano_file = str(sys.argv[1])

    volcano = VolcanoSystem(volcano_file)
    volcano.compute_paths()
    volcano.order_paths()
    max = volcano.find_best_path()
    print("Maximum releasable Pressure is ", max)

    volcano_ele = VolcanoSystem(volcano_file)
    volcano_ele.elephant_helps()
    max = volcano_ele.find_best_path()
    print("Maximum releasable Elephant-Pressure is ", max)

# main
if __name__=="__main__":
    main()