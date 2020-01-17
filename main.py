import time
from beacon import Beacon #class Beacon in beacon py
import db as beacons
import aux_functions
from threading import Thread

def scan_beacon():
    try:
        i = 0 #aux
        all_beacons = []
        beacon = Beacon()
        beacon.scanner.start()
        while i < 6:
            begin = time.time()
            end = time.time()
            while end - begin < 5:
                beacon_data = beacon.signal()
                end = time.time()
            beacon_one = list(filter(lambda x: x[0] == "fb:fe:6b:90:92:b4", beacon_data))
            beacon_two = list(filter(lambda x: x[0] == "eb:fd:db:e0:7a:ad", beacon_data))
            beacon_three = list(filter(lambda x: x[0] == "ec:2d:ed:68:b7:79", beacon_data))
            beacon_four = list(filter(lambda x: x[0] == "d9:15:36:69:13:d9", beacon_data))
            aux_functions.convert_rssi_to_distance(beacon_one, beacon_two, beacon_three, beacon_four)
            aux_functions.print_beacons(beacon_one, beacon_two, beacon_three, beacon_four)        
            i += 1
            beacon.clear_signal()
                
    except Exception as err:
        print(err)

    finally:
        beacon.scanner.stop()
            
t_one = Thread(target=scan_beacon)
t_one.start()

while True:
    if not t_one.is_alive():
        break


    
    
    
