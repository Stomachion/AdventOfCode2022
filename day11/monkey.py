from read_AoCinputs import *

class Monkey:

    def __init__(self, number:int, start: int, input_list:list):
        self.__number = number
        self.__items = []
        self.__operation = None
        self.__test = 0
        self.__test_true = 0
        self.__test_false = 0
        self.__counter = 0

        item_line = input_list[start+1].replace(",","")
        item_line = item_line.split()
        for i in range(2,len(item_line)):
            self.__items.append(int(item_line[i]))

        op_line = input_list[start+2].split()
        match op_line:
            case _ if "*" in op_line:
                if op_line[-1] == "old":
                    self.__operation = lambda old: old * old
                else:
                    self.__operation = lambda old: old * int(op_line[-1])
            case _ if "+" in op_line:
                if op_line[-1] == "old":
                    self.__operation = lambda old: old + old
                else:
                    self.__operation = lambda old: old + int(op_line[-1])
        
        test_line = input_list[start+3].split()
        self.__test = int(test_line[-1])

        test_line = input_list[start+4].split()
        self.__test_true = int(test_line[-1])

        test_line = input_list[start+5].split()
        self.__test_false = int(test_line[-1])

    def add_item(self, item):
        self.__items.append(item)


    def do_operation(self, old):
        return self.__operation(old)

    def do_test(self, worry_level):
        if worry_level % self.__test == 0:
            return self.__test_true
        else:
            return self.__test_false

    def print_items(self):
        print("Monkey", self.__number, ":", end=" ")
        for item in self.__items:
            print(item, end=" ")
        print()

    def throw_item(self, function):
        if len(self.__items) == 0:
            return None, None
        item = self.__items.pop(0)
        self.__counter += 1
        item = self.do_operation(item)
        item = function(item)
        destination = self.do_test(item)
        return item, destination

    def print_nr_inspects(self):
        print("Monkey", self.__number, " inspcted",self.__counter , " items ")

    def get_nr_inspects(self):
        return self.__counter
        
    def set_test(self, test):
        self.__test = test

    def get_test(self):
        return self.__test

class MonkeyGroup:

    def __init__(self, monkey_file, function):
        self.__monkeys = []
        self.__function = function

        monkey_list = read_txt_list(monkey_file)
        for i in range(0,len(monkey_list),+7):
           self.__monkeys.append(Monkey(i//7,i, monkey_list))

    def print_monkey_items(self):
        for monkey in self.__monkeys:
            monkey.print_items()
        print()

    def play_round(self):
        for monkey in self.__monkeys:
            value, destination = monkey.throw_item(self.__function)
            while destination != None:
                 self.__monkeys[destination].add_item(value)
                 value, destination = monkey.throw_item(self.__function)

    def print_activity(self):
        for monkey in self.__monkeys:
            monkey.print_nr_inspects()
    
    def get_activity(self):
        activity = []
        for monkey in self.__monkeys:
            activity.append(monkey.get_nr_inspects())
        return activity

    def activate_supertest(self):
        supertest = 1
        for monkey in self.__monkeys:
            supertest *= monkey.get_test()
        self.__function = lambda x: x % supertest

        



                 
        