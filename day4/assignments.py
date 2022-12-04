import sys

def read_txt_list(txt_file_name):
    txt_file = open(txt_file_name, "r")
    
    txt_list = []
    for line in txt_file:
        txt_list.append(line.rstrip())
    
    txt_file.close()
    return txt_list 

def count_contains(assignment_list):
    contained_count = 0
    overlap_count = 0

    for assignment in assignment_list:
        elf1_sections, elf2_sections = create_section_set(assignment)

        if (test_contained(elf1_sections,elf2_sections)):
            contained_count +=1
        
        if(test_overlap(elf1_sections, elf2_sections)):
            overlap_count +=1
    
    return contained_count, overlap_count


def test_contained(set1, set2):
    if set1.issubset(set2):
        return True
    elif set2.issubset(set1):
        return True
    else:
        return False

def test_overlap(set1:set, set2:set):
    return set1.intersection(set2) != set()


def create_section_set(assignments:str):

    assignments = assignments.replace(",", "-")
    bounds = assignments.split("-")

    elf_1_sections = set(range(int(bounds[0]), int(bounds[1])+1))
    elf_2_sections = set(range(int(bounds[2]), int(bounds[3])+1))

    return elf_1_sections, elf_2_sections


# Defining main function
def main():
    
    assignment_file = str(sys.argv[1])
    assignment_list = read_txt_list(assignment_file)

    countain_count, overlap_count = count_contains(assignment_list)
    print("There are ", countain_count, " fully contained chores")
    print("There are ", overlap_count, " overlap sections")


# main
if __name__=="__main__":
    main()