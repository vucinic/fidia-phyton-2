import random
import sys

import psutil


def get_cpu_temperature():
    # for g in psutil.sensors_temperatures(False)['coretemp']:
    #     print(g)
    if sys.platform == 'win32':
        return random.Random().random() * 100
    else:
        cpu = [i[1] for i in psutil.sensors_temperatures(False)['coretemp'] if 'Core' in i[0]]
        cpu_temp = sum(cpu) / len(cpu)
        # print(cpu_temp)
        return cpu_temp


def get_cpu_percent():
    print(psutil.cpu_percent())


def get_mem_percent():
    print(psutil.virtual_memory().percent)

