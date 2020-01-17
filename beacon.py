import time
from beacontools import BeaconScanner, IBeaconFilter


class Beacon():
    beacon_data = []
    
    def callback(self, bt_addr, rssi, packet, additional_info):
            beacon_data = [bt_addr, rssi, time.time() - self.initial_time]
            Beacon.beacon_data.append(beacon_data)            
            
    def __init__(self):
        self.initial_time = time.time()
        self.scanner = BeaconScanner(self.callback, 
            device_filter=IBeaconFilter(uuid="fda50693-a4e2-4fb1-afcf-c6eb07647825")
        )
        
    def signal(self):
        return Beacon.beacon_data

    def clear_signal(self):
        Beacon.beacon_data.clear()
