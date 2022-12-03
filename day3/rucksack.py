import sys

def read_txt_list(txt_file_name):
    txt_file = open(txt_file_name, "r")
    
    txt_list = []
    for line in txt_file:
        txt_list.append(line.rstrip())
    
    txt_file.close()
    return txt_list 

def split_rucksack(rucksack):
    ruck_size = len(rucksack)
    comp_size = ruck_size // 2
    return rucksack[0:comp_size], rucksack[comp_size:ruck_size]

def find_a_common_item(compartment1, compartment2):
    return set(compartment1).intersection(compartment2).pop()


def prioritize_item(item:str):
    if item.isupper():
        return ord(item)-38
    else:
        return ord(item)-96


def sum_priorities(rucksack_list):
    sum = int(0)
    for sack in rucksack_list:
        comp1, comp2 = split_rucksack(sack)
        common_item = find_a_common_item(comp1, comp2)
        sum += prioritize_item(common_item)
    return sum

# Defining main function
def main():
    
    rucksack_file = str(sys.argv[1])
    rucksack_list = read_txt_list(rucksack_file)

    summed_priorites = sum_priorities(rucksack_list)
    print("The priority sum is ", summed_priorites)


# main
if __name__=="__main__":
    main()