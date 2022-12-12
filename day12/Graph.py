from read_AoCinputs import *


class Graph:

    def __init__(self, graph_file):
            
        self.__nodes = 0    
        self.__start = (0,0)
        self.__finish = (0,0)
        self.__distances = []
        self.__predecessors = [[]]
        self.__Q = dict()


        list = read_txt_list(graph_file)
        nr_lines = len(list)
        nr_columns = len(list[0])

        graph_matrix = []
        for i in range(0,nr_lines):
            line = []
            for j in range(0, nr_columns):
                letter = list[i][j]
                if letter.isupper():
                    if letter == "S":
                        self.__start = (i,j)
                        line.append(1)
                    else: 
                        self.__finish = (i,j)
                        line.append(26)
                else:
                    line.append(ord(letter)-96)
            graph_matrix.append(line)
    
        self.__nodes = np.array(graph_matrix)

    def __init_dijkstra(self):

        nr_lines = self.__nodes.shape[0]
        nr_cols = self.__nodes.shape[1]
        infinite = nr_lines*nr_cols+1
        self.__distances = np.full(self.__nodes.shape, infinite)
        self.__distances[self.__start[0]][self.__start[1]] = 0

        self.__Q = dict()
        for i in range(nr_lines):
            for j in range (nr_cols):
                self.__Q[(i,j)]=self.__distances[i][j]
 
        self.__predecessors = [[]]
        self.__predecessors = [[(0,0)]*nr_cols for i in range(nr_lines)]
        for i in range(nr_lines):
            for j in range (nr_cols):
                self.__predecessors[i][j] = (i,j)

        self.__predecessors[self.__start[0]][self.__start[1]] = None       


    def perform_dijkstra(self):
        self.__init_dijkstra()
        while  len(self.__Q) > 0:

            minval = min(self.__Q.values())
            us = list(filter(lambda x: self.__Q[x]==minval,self.__Q))
            u = us[0]
            del self.__Q[u]

            neighbors = self.__find_neighbor(u)
            for v in neighbors:
                if len(self.__Q) > 0:
                    self.update_distance(u,v)


    def update_distance(self, u, v):
        alternative = self.__distances[u[0],u[1]] + 1
        if alternative < self.__distances[v[0],v[1]]:
            self.__distances[v[0],v[1]] = alternative
            self.__Q[v] = alternative
            self.__predecessors[v[0]][v[1]] = u


    def __find_neighbor(self, node_idx:tuple):
        upper = (node_idx[0]-1, node_idx[1])
        lower = (node_idx[0]+1, node_idx[1])
        left = (node_idx[0], node_idx[1]-1)
        right = (node_idx[0], node_idx[1]+1)
        
        neighbors = []
        self.__add_neighbor(neighbors, node_idx, upper)
        self.__add_neighbor(neighbors, node_idx, lower)
        self.__add_neighbor(neighbors, node_idx, left)
        self.__add_neighbor(neighbors, node_idx, right)
        
        return neighbors


    def __add_neighbor(self, neigbours:list, node, canidate):
        if self.__is_neighbor(node, canidate):
            neigbours.append(canidate)


    def __is_neighbor(self, node, test):
        if self.__in_bounds(test):
            if self.__nodes[test[0]][test[1]] - \
                   self.__nodes[node[0]][node[1]] < 2:
                return True
        return False

    def __in_bounds(self, test_object: tuple):
        return all(element >= 0 for element in test_object) and \
               test_object[0] < self.__distances.shape[0] and \
               test_object[1] < self.__distances.shape[1]  


    def get_path_lengt(self):
        return self.__distances[self.__finish[0]][self.__finish[1]]

    
    
    def print_graph(self):
        print(self.__nodes)
        print()

    def print_distances(self):
        print(self.__distances)
        print()


    def get_nicest_path(self): 
        nr_lines = self.__nodes.shape[0]
        nr_cols = self.__nodes.shape[1]
        start_positions = []    
        for i in range(nr_lines):
            for j in range(nr_cols):
                if self.__nodes[i][j] == 1:
                    start_positions.append((i,j))
        path_lengths = []
        i = 1
        for start in start_positions:

            self.__start = start
            self.perform_dijkstra()
            path_lengths.append(self.get_path_lengt()) 
        return np.min(path_lengths)
        



