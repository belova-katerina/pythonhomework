from time import sleep
from itertools import cycle

class TrafficLight:
    __color = ['Красный', 'Жёлтый', 'Зелёный', 'Жёлтый']

    def running(self):
        c = 0
        for el in cycle(TrafficLight.__color):
            i = 0
            while i < 4:
                print(f'Светофор переключается: \n '
                        f'{TrafficLight.__color[i]}')
                if i == 0:
                    sleep(7)
                elif i == 1:
                    sleep(2)
                elif i == 2:
                    sleep(5)
                elif i == 3:
                    sleep(2)
                i += 1
        c += 1


TrafficLight = TrafficLight()
TrafficLight.running()