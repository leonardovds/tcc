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
        
    
