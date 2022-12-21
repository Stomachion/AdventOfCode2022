import sys
from read_AoCinputs import read_txt_list 
from dataclasses import dataclass


@dataclass
class Monkey:
    name:str
    type:str
    number: int
    predecessor1:str
    predecessor2:str

def read_monkey_band(monkey_file):
    monkey_list = read_txt_list(monkey_file)
    monkey_band = []
    monkey = "dummy initialize"
    for line in monkey_list:
        line = line.split()
        # Number monkey
        if len(line) == 2:
            monkey = Monkey(line[0][0:-1], "number", \
                int(line[1]), "", "")
        # Number monkey
        else:
            monkey = Monkey(line[0][0:-1], line[2], \
                0, line[1], line[3])
        monkey_band.append(monkey)

    return monkey_band


def let_monkeys_shout(monkeys:list[Monkey]):
    yelled_monkeys = dict()
    rest_monkeys = []

    for monkey in monkeys:
        if monkey.type == "number":
            yelled_monkeys[monkey.name] = monkey.number
        else:
            rest_monkeys.append(monkey)


    while len(rest_monkeys) > 0:
        monkeys = rest_monkeys
        rest_monkeys = []
        for monkey in monkeys:
            m1 = monkey.predecessor1
            m2 = monkey.predecessor2 
            if m1 in yelled_monkeys and m2 in yelled_monkeys:
                m1 = yelled_monkeys[m1]
                m2 = yelled_monkeys[m2]
                yell = eval("m1" + monkey.type + "m2")
                yelled_monkeys[monkey.name] = yell
            else:
                rest_monkeys.append(monkey)

    return yelled_monkeys

##################################################################

# Defining main function
def main():
    
    monkey_code_file = str(sys.argv[1])
    monkeys = read_monkey_band(monkey_code_file)

    
    yelled_monkes = let_monkeys_shout(monkeys)

    print("root yells ", yelled_monkes["root"])
    

# main
if __name__=="__main__":
    main()