import math
import time
from beacontools import BeaconScanner, IBeaconFilter


class Beacon():

    #atributos da classe
    
    beacon_data = []
    tolerance = 1
    pi = math.pi
    step = pi/50

    @staticmethod
    def average(beacon):
        average_sum = 0
        for value in beacon:
            average_sum += value[1]
        return average_sum/len(beacon)

    @staticmethod
    def sort_beacon_key(beacon):
        return beacon[1]
    
    def callback(self, bt_addr, rssi, packet, additional_info):
            beacon_data = [bt_addr, rssi]#atributo do objeto
            Beacon.beacon_data.append(beacon_data)#atributo da classe            
            
    def __init__(self):
        self.initial_time = time.time()
        self.scanner = BeaconScanner(self.callback, 
            device_filter=IBeaconFilter(uuid="fda50693-a4e2-4fb1-afcf-c6eb07647825")
        )
        
    def signal(self):
        return Beacon.beacon_data#atributo da classe

    def clear_signal(self):
        Beacon.beacon_data.clear()

    def convert_rssi_to_distance(self, beacon):
        beacon_average = Beacon.average(beacon)
        beacon_distance = abs((abs(beacon_average) - 45)/10)
        return [beacon[0][0], beacon_distance]

    def print_beacons(self, beacon):
        for value in beacon:
            print (value)
        print('=' * 25)

    def possible_positions(self, axis, distance):
        step = Beacon.step
        pi = Beacon.pi
        positions = []
        i = 0
        if axis == 'y':
            while i < 100:
                aux = math.sin(step) * distance
                positions.append(aux)
                step += pi/50
                i += 1
        else:
            while i < 100:
                aux = math.cos(step) * distance
                positions.append(aux)
                step += pi/50
                i += 1
        return positions            
                
    def transform_positions(self, pos_list, pos_x, pos_y):
        positions = []
        for valores in pos_list:
            new_pos_x = round(abs(pos_x - valores[0]),5) 
            new_pos_y = round(abs(pos_y - valores[1]),5)
            aux = [new_pos_x, new_pos_y]
            positions.append(aux)
        return positions
            
    def avrg_pos(self, positions):
        total = 0
        for position in positions:
            total += position[0] #valores da posicao x
        avrg_x = total/len(positions)
        total = 0
        for position in positions:
            total += position[1] #valores da posicao y
        avrg_y = total/len(positions)
        return avrg_x, avrg_y

    def find_positions(self, beacon_one, beacon_two):
        tolerance = Beacon.tolerance
        i = 0
        positions = []
        while i < len(beacon_one):
            if beacon_one[i][0] >= beacon_two[i][0] - tolerance and beacon_one[i][0] <= beacon_two[i][0] + tolerance and beacon_one[i][1] >= beacon_two[i][1] - tolerance and beacon_one[i][1] <= beacon_two[i][1] + tolerance:
                aux = [beacon_one[i][0], beacon_one[i][1]]
                positions.append(aux)
            i += 1
        return positions
        
    def final_position(self, positions, beacon):
        tolerance = Beacon.tolerance
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

    def positions(self, possible_positions_x, possible_positions_y):
        pos_possible = []
        for pos in range(len(possible_positions_x)):
            aux = [possible_positions_x[pos], possible_positions_y[pos]]
            pos_possible.append(aux)
        return pos_possible

    def return_beacon(self, beacon_data):
        beacon = list(filter(lambda x: x[0] == "fb:fe:6b:90:92:b4", beacon_data))
        if len(beacon) > 0:
            yield beacon
        beacon = list(filter(lambda x: x[0] == "eb:fd:db:e0:7a:ad", beacon_data))
        if len(beacon) > 0:
            yield beacon
        beacon = list(filter(lambda x: x[0] == "ec:2d:ed:68:b7:79", beacon_data))
        if len(beacon) > 0:
            yield beacon
        beacon = list(filter(lambda x: x[0] == "d9:15:36:69:13:d9", beacon_data))
        if len(beacon) > 0:
            yield beacon


    def sort_beacon(self, beacons):
        beacons.sort(key=Beacon.sort_beacon_key)

