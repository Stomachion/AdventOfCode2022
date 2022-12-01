import numpy 
import sys

def read_txt_list(txt_file_name):
    txt_file = open(txt_file_name, "r")
    
    txt_list = []
    for line in txt_file:
        txt_list.append(line.rstrip())
    
    txt_file.close()
    return txt_list 


def compute_elves_calories(food_list):

    elves_calories = []
    current_calories = int(0)
    
    for food_calrories in food_list:
        if food_calrories == '':
            elves_calories.append(current_calories)
            current_calories = 0
        else:
            current_calories += int(food_calrories)
    # add last elfs calories
    elves_calories.append(current_calories)

    return numpy.asarray(elves_calories)


def find_elf_with_most_calories(elves_calories):
    elf = numpy.argmax(elves_calories)
    return elf, elves_calories[elf]

# Defining main function
def main():
    elves_food_list_file = str(sys.argv[1])
    elves_food_list = read_txt_list(elves_food_list_file)
    elves_calories = compute_elves_calories(elves_food_list)
    max_calory_elf, max_calories = find_elf_with_most_calories(elves_calories)
    print("Elf number ", max_calory_elf, "with ", max_calories, " calories")
    

# main
if __name__=="__main__":
    main()