import math

tolerance = 1

def write_file(*args):
    beacon_storage = open('beacons.txt', 'w')
    for beacon in args:
        beacon_average = average(beacon)
        beacon_storage.write('=' * 25)
        beacon_storage.write('\n')
        

def convert_rssi_to_distance(*args):
    for beacon in args:
        for value in beacon:
            value[1] = abs((abs(value[1]) - 38)/10)

def print_beacons(*args):
    for beacon in args:
        for value in beacon:
            print (value)
        print('=' * 25)
            
def average(beacon):
    average_sum = 0
    for value in beacon:
        average_sum += value[1]
    return average_sum/len(beacon)

def possible_positions(axis, step, pi, distance):
    positions = []
    i = 0
    if axis == 'y':
        while i < 25:
            aux = math.sin(step) * distance
            positions.append(aux)
            step += pi/50
            i += 1
    else:
        while i < 25:
            aux = math.cos(step) * distance
            positions.append(aux)
            step += pi/50
            i += 1
    return positions            
            
def transform_positions(pos_list, pos_x, pos_y):
    positions = []
    for valores in pos_list:
        new_pos_x = round(abs(pos_x - valores[0]),5) 
        new_pos_y = round(abs(pos_y - valores[1]),5)
        aux = [new_pos_x, new_pos_y]
        positions.append(aux)
    return positions
        
def avrg_pos(positions):
    total = 0
    for position in positions:
        total += position[0] #valores da posicao x
    avrg_x = total/len(positions)
    total = 0
    for position in positions:
        total += position[1] #valores da posicao y
    avrg_y = total/len(positions)
    return avrg_x, avrg_y

def find_positions(beacon_one, beacon_two):
    global tolerance
    i = 0
    positions = []
    while i < len(beacon_one):
        if beacon_one[i][0] >= beacon_two[i][0] - tolerance and beacon_one[i][0] <= beacon_two[i][0] + tolerance and beacon_one[i][1] >= beacon_two[i][1] - tolerance and beacon_one[i][1] <= beacon_two[i][1] + tolerance:
            aux = [beacon_one[i][0], beacon_one[i][1]]
            positions.append(aux)
        i += 1
    return positions
    
def final_position(positions, beacon):
    global tolerance
    i = 0
    pos_final = []
    while i < len(positions):
        j = 0
        while j < len(beacon):
            if positions[i][0] >= beacon[j][0] - tolerance and positions[i][0] <= beacon[j][0] + tolerance and positions[i][1] >= beacon[j][1] - tolerance and positions[i][1] <= beacon[j][1] + tolerance:
                aux = [positions[i][0], positions[i][1]]
                pos_final.append(aux)
                break
            j += 1
        i += 1
    return pos_final

        
    
