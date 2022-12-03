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
    return [set(rucksack[0:comp_size]), set(rucksack[comp_size:ruck_size])]


def find_a_common_item(bag_list):
    return set.intersection(*bag_list).pop()


def prioritize_item(item:str):
    if item.isupper():
        return ord(item)-38
    else:
        return ord(item)-96


def sum_priorities(rucksack_list):
    sum = int(0)
    for sack in rucksack_list:
        compartments = split_rucksack(sack)
        common_item = find_a_common_item(compartments)
        sum += prioritize_item(common_item)
    return sum


def sum_group_priorities(rucksack_list):
    sum = int(0)
    i = int(0)
    while i < len(rucksack_list):
        bags = [set(rucksack_list[i]), set(rucksack_list[i+1]), set(rucksack_list[i+2]) ]
        common_item = find_a_common_item(bags)
        sum += prioritize_item(common_item)
        i+=3
    return sum


# Defining main function
def main():
    
    rucksack_file = str(sys.argv[1])
    rucksack_list = read_txt_list(rucksack_file)

    summed_priorites = sum_priorities(rucksack_list)
    print("The priority sum is ", summed_priorites)

    summed_group_priorities = sum_group_priorities(rucksack_list)
    print("The Group priority sum is ", summed_group_priorities)


# main
if __name__=="__main__":
    main()