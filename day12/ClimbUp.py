import sys
import numpy
from Graph import Graph



# Defining main function
def main():
    
    mountain_file = str(sys.argv[1])
    mountains = Graph(mountain_file)

    mountains.perform_dijkstra()
    path_length  = mountains.get_path_lengt()

    print("The path is ", path_length, " long")

    nice = mountains.get_nicest_path()
    print("Nicest path is ", nice, " long")
   
  
# main
if __name__=="__main__":
    main()