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


def find_n_most_calrories_elves(elves_calories, n):
    return (-elves_calories).argsort()[:n]


def sum_special_elves_calories(elves_calories, special_elves_list):
    sum = int(0)
    for elves in special_elves_list:
        sum += elves_calories[elves]
    return sum


def compute_top3_total_calories(elves_calories):
    top3 = find_n_most_calrories_elves(elves_calories, 3)
    return sum_special_elves_calories(elves_calories, top3)


# Defining main function
def main():
    
    elves_food_list_file = str(sys.argv[1])
    elves_food_list = read_txt_list(elves_food_list_file)
    
    elves_calories = compute_elves_calories(elves_food_list)
    
    max_calory_elf, max_calories = find_elf_with_most_calories(elves_calories)
    print("Elf number ", max_calory_elf, "with ", max_calories, " calories")
    
    top3_total_calories = compute_top3_total_calories(elves_calories)
    print("Top 3 elves total calories: ", top3_total_calories) 

    

# main
if __name__=="__main__":
    main()