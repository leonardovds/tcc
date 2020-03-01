'''
Importacao das bibliotecas a serem utilizadas
no projeto
'''

import math
import time
from beacon import Beacon #classe Beacon que implementa as funcoes do programa
import db as beacons_database #arquivo com informacoes dos beacons
from threading import Thread


'''
funcao que contem o programa principal que sera responsavel
por fazer a leitura dos beacons constantemente
'''
def scan_beacon():
    try:
        beacons = []
        possible_posx = []
        possible_posy = []
        pos_beacon_xy = []
        posx_absolute_beacon = []
        posy_absolute_beacon = []
        beacon_real_position = []
        beacon = Beacon()
        beacon.scanner.start()
        while True:
            begin = time.time()
            end = time.time()
            '''
            primeiro passo e fazer a leitura dos beacons, e isso ocorre
            por 5 segundos, meramente estipulado.
            '''
            while end - begin < 5:
                beacon_data = beacon.signal()
                end = time.time()
            '''
            apos fazer a leitura dos beacons, sao armazenados cada um em um
            indice de uma lista na var beacons
            '''

            beacon_filter = beacon.return_beacon(beacon_data)
            
            for one_beacon in beacon_filter:
                beacons.append(one_beacon)
                
            '''
            transforma o sinal rssi em distancia
            '''
            
            for i in range(len(beacons)):
                beacons[i] = beacon.convert_rssi_to_distance(beacons[i])

            beacon.sort_beacon(beacons)
            beacon.print_beacons(beacons)

            print('========================================')

            '''
            encontra as posicoes possiveis de cada sinal
            '''
            for one_beacon in beacons:
                beacon_id = one_beacon[0]
                beacon_positionx = beacon.possible_positions('x', one_beacon[1])
                beacon_positiony = beacon.possible_positions('y', one_beacon[1])
                aux = [beacon_id, beacon_positionx]
                possible_posx.append(aux)
                aux = [beacon_id, beacon_positiony]
                possible_posy.append(aux)

            print(possible_posx)
            print('========================================')
            print(possible_posy)
            print('========================================')
            '''
            transforma as posicoes para uma forma de trabalho mais simples
            '''
            for i in range(3):
                beacon_id = possible_posx[i][0]
                position = beacon.positions(possible_posx[i][1], possible_posy[i][1])
                aux = [beacon_id, position]
                pos_beacon_xy.append(aux)
            
            print(pos_beacon_xy)
            print('========================================')
            '''
            transforma as posicoes levando em conta os pontos fixos
            dos beacons
            '''
            for i in range(3):
                posx, posy = beacons_database.beacon_absolute_position(pos_beacon_xy[i][0])
                posx_absolute_beacon.append(posx)
                posy_absolute_beacon.append(posy)

            print(posx_absolute_beacon)
            print('========================================')
            print(posy_absolute_beacon)
            print('========================================')
                
            for i in range(3):
                beacon_real_position.append(beacon.transform_positions(pos_beacon_xy[i][1], posx_absolute_beacon[i], posy_absolute_beacon[i]))

            print(beacon_real_position)
            print('========================================')
            '''
            encontra a posicao final
            '''
            initial_position = beacon.find_positions(beacon_real_position[0], beacon_real_position[1])
            print(initial_position)
            print('========================================')
            final_position = beacon.final_position(initial_position, beacon_real_position[2])
            print(final_position)
            print('========================================')
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


    
    
    
