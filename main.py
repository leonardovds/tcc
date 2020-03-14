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
        beacons = [] #lista que armazena todos os beacons
        possible_relative_posx = [] #lista com posicoes possiveis no eixo x
        possible_relative_posy = [] #lista com posicoes possiveis no eixo y
        relative_pos_beacon_xy = [] #lista que armazena posicoes possiveis na forma [x,y]
        beacon_posx = [] #posicao x do beacon encontrado
        beacon_posy = [] #posicao y do beacon encontrado
        possible_absolute_position = [] #lista que armazena as possiveis posicoes absolutas do objeto
        beacon = Beacon() #instancia do objeto da classe beacon
        beacon.scanner.start() #metodo que inicia o scanner do beacon
        while True:
            '''
            Aguarda 5 segundos para fazer a leitura do beacon
            '''
            print('lendo beacon')
            time.sleep(5)
            beacon_data = beacon.signal()
            '''
            apos fazer a leitura dos beacons, sao armazenados cada um em um
            indice de uma lista na var beacons
            '''         
            beacon_filter = beacon.return_beacon(beacon_data)
            
            for one_beacon in beacon_filter:
                beacons.append(one_beacon)

            print('leitura realizada')

            '''
            caso nao encontre ao menos 3 beacons, executa a funcao novamente
            '''
            if len(beacons) < 3:
                scan_beacon()
                
            '''
            transforma o sinal rssi em distancia
            '''
            
            for i in range(len(beacons)):
                beacons[i] = beacon.convert_rssi_to_distance(beacons[i])

            beacon.sort_beacon(beacons)
            #beacon.print_beacons(beacons)

            #print('========================================')

            '''
            encontra as posicoes possiveis de cada sinal
            '''
            for one_beacon in beacons:
                beacon_id = one_beacon[0]
                beacon_positionx = beacon.possible_positions('x', one_beacon[1])
                beacon_positiony = beacon.possible_positions('y', one_beacon[1])
                aux = [beacon_id, beacon_positionx]
                possible_relative_posx.append(aux)
                aux = [beacon_id, beacon_positiony]
                possible_relative_posy.append(aux)

            #print(possible_relative_posx)
            #print('========================================')
            #print(possible_relative_posy)
            #print('========================================')
            '''
            transforma as posicoes para uma forma de trabalho mais simples, em uma
            lista no formato [x,y]
            '''
            for i in range(3):
                beacon_id = possible_relative_posx[i][0]
                position = beacon.positions(possible_relative_posx[i][1], possible_relative_posy[i][1])
                aux = [beacon_id, position]
                relative_pos_beacon_xy.append(aux)
            
            #print(relative_pos_beacon_xy)
            #print('========================================')
            '''
            retorna a posicao fixa de cada beacon que foi lido
            '''
            for i in range(3):
                posx, posy = beacons_database.beacon_absolute_position(relative_pos_beacon_xy[i][0])
                beacon_posx.append(posx)
                beacon_posy.append(posy)

            #print(beacon_posx)
            #print('========================================')
            #print(beacon_posy)
            #print('========================================')

            '''
            transforma a lista de posicoes relativas do robo em relacao ao beacon
            em uma lista de posicoes absolutas no ambiente
            '''
            for i in range(3):
                possible_absolute_position.append(beacon.transform_positions(relative_pos_beacon_xy[i][1], beacon_posx[i], beacon_posy[i]))

            #print(possible_absolute_position)
            #print('========================================')
            '''
            encontra a posicao final com base nas posicoes absolutas encontradas
            '''
            initial_position = beacon.find_positions(possible_absolute_position[0], possible_absolute_position[1])
            #print(initial_position)
            #print('========================================')
            final_position = beacon.final_position(initial_position, possible_absolute_position[2])
            #print(final_position)
            #print('========================================')
            beacon.clear_signal()
             
    except Exception as err:
        print(err)

    finally:
        beacon.scanner.stop()
'''
testa multiplas threads
def testa_thread():
    while True:
        print('a')
        time.sleep(1)

functions = [scan_beacon, testa_thread]'''

functions = [scan_beacon]
threads = list()

for index in range(len(functions)):
    t = Thread(target=functions[index])
    threads.append(t)
    t.start()

'''
funcao que 

for thread in threads:
    thread.join()
'''


    
    
    
