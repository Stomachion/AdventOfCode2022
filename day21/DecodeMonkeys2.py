import sys
from read_AoCinputs import read_txt_list 

def read_monkey_band(monkey_file):
    monkey_list = read_txt_list(monkey_file)
    monkey_band = dict()

    for line in monkey_list:
        splited = line.split()
        name = line[0:4]
        operation = ""
        if len(splited) == 2:
            operation = line[6:]
        else: 
           operation = line[6:]
        monkey_band[name] = operation

    return monkey_band

def get_command(monkeys:dict, command:str):
    keep_going = True
    while keep_going:
        splitted_command = command.split()
        command = ""
        count_finished = 0
        for word in splitted_command: 
            if len(word) == 4:
                command += "( " + monkeys[word] + " ) "
            else:
                command += word + " "
                count_finished += 1
        if count_finished == len(splitted_command):
            keep_going = False
    
    return command

def get_command2(monkeys:dict, command:str):
    keep_going = True
    while keep_going:
        splitted_command = command.split()
        command = ""
        count_finished = 0
        for word in splitted_command: 
            if word == "humn":
                command += word + " "
                count_finished += 1
            elif len(word) == 4:
                command += "( " + monkeys[word] + " ) "
            else:
                command += word + " "
                count_finished += 1
        if count_finished == len(splitted_command):
            keep_going = False
    
    return command


def let_monkeys_shout(monkeys:dict):
    command = monkeys["root"]
    return get_command(monkeys, command)


def real_talk(monkeys:dict):
    command = monkeys["root"]
    splitted_commad = command.split()
    command1 = splitted_commad[0]
    command2 = splitted_commad[2]

    command1 = get_command2(monkeys, command1)
    command2 = get_command2(monkeys, command2)

    return command1, command2

def is_human(command:str):
    if command.find("humn") == -1:
        return False
    else:
        return True

def eval_monkey_command(command:str):
    if is_human(command):
        return command
    else:
        return eval(command)

def get_inverse_operation(operation:str):
    match operation:
        case "+":
            return "-"
        case "-":
            return "+"
        case "*":
            return "/"
        case "/":
            return "*"

def is_operation(command: str):
    if command == "+" or command == "-":
        return True
    elif command == "*" or command == "/":
        return True
    else:
        return False

def strip_parentisis(expression:str):
    return expression[2:-2]

def split_math_expr(expression:str):
    count_opened = 0
    for i in range(len(expression)):
        if expression[i] == "(":
            count_opened += 1
        elif expression[i] == ")":
            count_opened -= 1
        if count_opened == 0 and is_operation(expression[i]):
            left = expression[0:i]
            operation = expression[i]
            right = expression[i+1:]
            return left, operation, right

def solve_human_eqation(lhs:str , rhs:int):
    while lhs.find("(") > -1:
        lhs = strip_parentisis(lhs)
        left, op, right = split_math_expr(lhs)
        #print(left)
        #print(op)
        #print(right)
    
        if is_human(left):
            rhs = eval(str(rhs) + get_inverse_operation(op) + right)
            lhs = left
        # hier falsch
        else:
            lhs = right
            left = eval(left)
            match op:
                case "+":
                    rhs = rhs - left
                case "*":
                    rhs = rhs / left
                case "-":
                    rhs = left - rhs
                case "/":
                    rhs = left / rhs 
    return rhs
    

##################################################################

# Defining main function
def main():
    
    monkey_code_file = str(sys.argv[1])
    monkeys = read_monkey_band(monkey_code_file)
    #print(monkeys)

    yell = let_monkeys_shout(monkeys)
    print("root yells ", eval(yell))

    command1, command2 = real_talk(monkeys)
    command1 = eval_monkey_command(command1)
    command2 = eval_monkey_command(command2)

    value = 0
    math_expr = " "
    if type(command1) == int:
        value = command1
        math_expr = command2
    else:
        value = command2
        math_expr = command1

    humn = solve_human_eqation(math_expr, value)
    print("humn = ", humn)


# main
if __name__=="__main__":
    main()