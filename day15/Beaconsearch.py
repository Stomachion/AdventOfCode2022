import sys
from read_AoCinputs import read_txt_list 

def get_sensors_beacons(sensor_list:list):
    sensors = []
    beacons = []
    for line in sensor_list:
        line = line.split()
        x = extrakt_coordinate(line[2])
        y = extrakt_coordinate(line[3])
        sensors.append((x,y))
        x = extrakt_coordinate(line[8])
        y = extrakt_coordinate(line[9])
        beacons.append((x,y))

    return sensors, beacons


def extrakt_coordinate(coord_string:str):
    if "," in coord_string or ":" in coord_string:
        return int(coord_string[2:-1])
    else:
        return int(coord_string[2:])


def compute_manhatten_distance(x:tuple, y:tuple):
    distance = 0
    for i in range(len(x)):
        distance += abs(x[i]-y[i])
    return distance


class Sensorrange:
    
    def __init__(self,sensor_position:tuple, range:int):
        self.__senor_position = sensor_position
        self.__range = range

    def is_x_in_range(self, x:tuple):
        if compute_manhatten_distance(x, self.__senor_position) <= self.__range:
            return True
        else: 
            return False

    def compute_distance_to_sensor(self, x:tuple):
        return abs(x[0]-self.__senor_position[0]) + abs(x[1]-self.__senor_position[1])

    def is_line_in_range(self, line:int):
        ymin = self.__senor_position[1] - self.__range
        ymax = self.__senor_position[1] + self.__range

        if ymin <= line and line <= ymax:
            return True
        else:
            return False

    # assumes line is in range
    def get_line_range(self, line):
        line_range = self.__range - abs(line - self.__senor_position[1])
        return (self.__senor_position[0]-line_range, self.__senor_position[0]+line_range)

    def get_surroundig(self):
        surrounding = []
        r = self.__range+1
        for i in range(0,r):
            surrounding.append((self.__senor_position[0]+i, self.__senor_position[1]+r-i))
            surrounding.append((self.__senor_position[0]+i, self.__senor_position[1]-r+i))
            surrounding.append((self.__senor_position[0]+r-i, self.__senor_position[1]+i))
            surrounding.append((self.__senor_position[0]+r-i, self.__senor_position[1]-i))
        return surrounding



def count_denied_positions(sensors:list, beacons:list, line):
    
    line_coverage = set()
    for i in range(len(sensors)):
        srange = compute_manhatten_distance(sensors[i], beacons[i])
        sensorrange = Sensorrange(sensors[i], srange)
        if sensorrange.is_line_in_range(line):
            line_range = sensorrange.get_line_range(line)
            for x in range(line_range[0],line_range[1]+1):
                line_coverage.add(x)

    # we have to remove beacon positions
    line_coverage = line_coverage - get_devices_x_on_line(beacons, line)
    line_coverage = line_coverage - get_devices_x_on_line(sensors, line)

    return len(line_coverage)


def get_devices_x_on_line(devices:list, line:int):
    device_x = set()
    for device in devices:
        if device[1] == line:
            device_x.add(device[0])
    return device_x


########## Part 2, try 1 --- Works for test, but too slow for real tast   ###########

def find_beacon(sensor_list, xmin, xmax):
    sensors, beacons = get_sensors_beacons(sensor_list)
    for i in range(xmin, xmax):
        xpos = beacon_in_line(sensors, beacons, i, xmin, xmax)
        if len(xpos) == 1:
            return (xpos.pop(),i)
    # beacon not found, error
    return (xmin-1, xmin-1)
 

def beacon_in_line(sensors:list, beacons:list, line, xmin:int, xmax:int):
    xpositions = set(range(xmin,xmax+1))
    for i in range(len(sensors)):
        srange = compute_manhatten_distance(sensors[i], beacons[i])
        sensorrange = Sensorrange(sensors[i], srange)
        if sensorrange.is_line_in_range(line):
            line_range = sensorrange.get_line_range(line)

            if line_range[0] < xmin:
                line_range = (xmin,line_range[1]) 
            if line_range[1] > xmax:
                line_range = (line_range[0],xmax)

            for x in range(line_range[0],line_range[1]+1):
                xpositions.discard(x)
    return xpositions 


########## Part 2, try 2 --- ###########

def find_beacon2(sensor_list, xmin, xmax):
    sensors, beacons = get_sensors_beacons(sensor_list)
    sensranges = []
    for i in range(len(sensors)):
        srange = compute_manhatten_distance(sensors[i], beacons[i])
        sensranges.append(Sensorrange(sensors[i], srange))

    for sensrange in sensranges:
        surrounding = sensrange.get_surroundig()
        print(len(surrounding))
        for point in surrounding:
            test_passed = True
            for testrange in sensranges:
                if point[0] < xmin or point[0] > xmax:
                    test_passed = False
                    break
                if point[1] < xmin or point[1] > xmax:
                    test_passed = False
                    break
                if testrange.is_x_in_range(point):
                    test_passed = False
                    break
            if test_passed: 
                return point

    return (xmin-1, xmin-1)
 


##################################################################

# Defining main function
def main():
    
    sensor_file = str(sys.argv[1])
    sensor_list = read_txt_list(sensor_file)
    line = int(sys.argv[2])

    sensors, beacons = get_sensors_beacons(sensor_list)
    denied_count = count_denied_positions(sensors, beacons, line)
    print("There are ", denied_count, " denied position in line ", line)

### Part 2, try 1 --- Works for test, but too slow for real question
    min = int(sys.argv[3])
    max = int(sys.argv[4])
    beacon_pos = find_beacon2(sensor_list, min, max)

    print("Beacon is at ", beacon_pos)
    print("Frequency ", beacon_pos[0]*4000000+beacon_pos[1])


# main
if __name__=="__main__":
    main()