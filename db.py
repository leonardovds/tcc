'''beacon simple database'''

b1 = {"id":"fb:fe:6b:90:92:b4",
        "pos_x": 0,
        "pos_y": 0
        }

b2 = {"id":"eb:fd:db:e0:7a:ad",
        "pos_x": 0,
        "pos_y": 0
        }

b3 = {"id":"ec:2d:ed:68:b7:79",
         "pos_x": 2.3,
         "pos_y": 0
         }

b4 = {"id":"d9:15:36:69:13:d9",
        "pos_x": 2.3,
        "pos_y": 2.7
        }

beacons = [b1, b2, b3, b4]

def beacon_absolute_position(beacon_id):
    global beacons
    for beacon in beacons:
        if beacon['id'] == beacon_id:
            return beacon['pos_x'], beacon['pos_y']


