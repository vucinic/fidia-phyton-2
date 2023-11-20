import random
import sys
import time
from threading import Thread

import psutil

import data


class StatsRoutine:

    def __init__(self, log_enabled=False):
        super().__init__()
        self.log_enabled = log_enabled
        self.__is_running = False
        self.stats = data.StatsData(
            data.TsValue(int(time.time_ns() / 1_000_000), 0.0),
            data.TsValue(int(time.time_ns() / 1_000_000), 0.0),
            data.TsValue(int(time.time_ns() / 1_000_000), 0.0),
        )

        self.__th_c_temp = Thread(target=self.__get_cpu_temperature)
        self.__th_c_perc = Thread(target=self.__get_cpu_percent)
        self.__th_m_perc = Thread(target=self.__get_mem_percent)

    def run(self):
        self.__is_running = True
        self.__th_c_temp.start()
        self.__th_c_perc.start()
        self.__th_m_perc.start()

    def stop(self):
        self.__is_running = False
        self.__th_c_temp.join()
        self.__th_c_perc.join()
        self.__th_m_perc.join()

    def __get_cpu_temperature(self):
        # for g in psutil.sensors_temperatures(False)['coretemp']:
        #     print(g)

        while self.__is_running:
            temp = 0
            if sys.platform == 'win32':
                temp = random.Random().random() * 100
            else:
                cpu = [i[1] for i in psutil.sensors_temperatures(False)['coretemp'] if 'Core' in i[0]]
                cpu_temp = sum(cpu) / len(cpu)
                temp = cpu_temp

            v = data.TsValue(int(time.time_ns() / 1_000_000), temp)

            if self.log_enabled:
                print('cpu_temp', v)

            self.stats.set_cpu_temp(v)
            time.sleep(0.125)

    def __get_cpu_percent(self):
        while self.__is_running:
            v = data.TsValue(int(time.time_ns() / 1_000_000), psutil.cpu_percent())
            if self.log_enabled:
                print('cpu_temp', v)
            self.stats.set_cpu_perc(v)
            time.sleep(0.125)

    def __get_mem_percent(self):
        while self.__is_running:
            v = data.TsValue(int(time.time_ns() / 1_000_000), psutil.virtual_memory().percent)
            if self.log_enabled:
                print('ram_perc', v)
            self.stats.set_ram_perc(v)
            time.sleep(0.125)
