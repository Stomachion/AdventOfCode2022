from __future__ import annotations

class AoCNode:
    
    def __init__(self, name: str, 
                 children: list = []):
        self.__data={"name":name}
        self.__children = children
        print(self.__data["name"], len(self.__children))


    def add_child(self, name: str):
        self.__children.append(AoCNode(name))


    def add_data(self, key, value ):
        self.__data[key] = value


    def get_data(self, key = None):
        if key == None:
            return self.__data
        else:
            return self.__data.get(key)

    
    def print_tree(self, depth:int = 0):
        output = depth*" " + "-" + self.__data.get("name")
        print(output)
        print("Number of Children: ", len(self.__children))
        for child in self.__children:
            child.print_tree(depth+1)

