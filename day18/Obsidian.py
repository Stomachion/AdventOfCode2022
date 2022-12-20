import sys
from read_AoCinputs import read_txt_list 

def get_cubes(scan:list):
    cubes = []
    for line in scan:
        line = line.split(",")
        x = int(line[0])
        y = int(line[1])
        z = int(line[2])
        cubes.append((x,y,z))
    return cubes

def count_surface_sides(cube_list: list):
    surface_sides = 0
    for cube in cube_list:
        surface_sides += count_free_sides(cube, cube_list)
    return surface_sides

def count_free_sides(cube:tuple, cube_list:list):
    free_sides = 6

    spot = (cube[0]+1, cube[1], cube[2]) 
    if is_cube_in_list(spot, cube_list):
        free_sides -=1
    spot = (cube[0]-1, cube[1], cube[2]) 
    if is_cube_in_list(spot, cube_list):
        free_sides -=1

    spot = (cube[0], cube[1]+1, cube[2]) 
    if is_cube_in_list(spot, cube_list):
        free_sides -=1
    spot = (cube[0], cube[1]-1, cube[2]) 
    if is_cube_in_list(spot, cube_list):
        free_sides -=1

    spot = (cube[0], cube[1], cube[2]+1) 
    if is_cube_in_list(spot, cube_list):
        free_sides -=1
    spot = (cube[0], cube[1], cube[2]-1) 
    if is_cube_in_list(spot, cube_list):
        free_sides -=1

    return free_sides

def is_cube_in_list(cube:tuple, cube_list: list):
    if cube_list.count(cube) > 0:
        return True
    else:
        return False

##################################################################

# Defining main function
def main():
    
    scan_file = str(sys.argv[1])
    scan_list = read_txt_list(scan_file)

    cubes = get_cubes(scan_list)
    surface_sides = count_surface_sides(cubes)

    print("There are ", surface_sides, " surfacesides")


# main
if __name__=="__main__":
    main()