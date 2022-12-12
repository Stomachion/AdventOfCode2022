import sys
from monkey import *
import numpy



# Defining main function
def main():
    
    monkey_file = str(sys.argv[1])

    # Part One
    monkeys = MonkeyGroup(monkey_file, lambda item: item //3)
    for i in range(20):
        monkeys.play_round()
    
    activity = monkeys.get_activity()
    HVTs = sorted(activity, reverse= True)[:2]
    print("HVTs Bounty = ",numpy.prod(HVTs) )
    print()


    # Part Two
    monkeys = MonkeyGroup(monkey_file, lambda item: item )
    monkeys.activate_supertest()
    for i in range(10000):
        monkeys.play_round()
        
    monkeys.print_activity()
    
    activity = monkeys.get_activity()
    HVTs = sorted(activity, reverse= True)[:2]
    print("HVTs Bounty = ",numpy.prod(HVTs) )
    print()


# main
if __name__=="__main__":
    main()