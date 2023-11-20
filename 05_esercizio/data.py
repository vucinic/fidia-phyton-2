from threading import Lock


class TsValue:

    def __init__(self, ts: int, value: float):
        self.__ts = str(ts)
        self.__value = value

    def get_ts(self):
        return self.__ts

    def get_value(self):
        return self.__value

    def __str__(self):
        return f'{self.__ts} - {self.__value}'


class StatsData:
    __cpu_perc: TsValue
    __ram_perc: TsValue
    __cpu_temp: TsValue

    def __init__(self, cpu_perc: TsValue, ram_perc: TsValue, cpu_temp: TsValue):
        self.__cpu_perc = cpu_perc
        self.__ram_perc = ram_perc
        self.__cpu_temp = cpu_temp
        self.__cpu_perc_lock = Lock()
        self.__ram_perc_lock = Lock()
        self.__cpu_temp_lock = Lock()

    def get_cpu_perc(self):
        with self.__cpu_perc_lock:
            return self.__cpu_perc

    def set_cpu_perc(self, cpu_perc: TsValue):
        with self.__cpu_perc_lock:
            self.__cpu_perc = cpu_perc

    def get_cpu_temp(self):
        with self.__cpu_temp_lock:
            return self.__cpu_temp

    def set_cpu_temp(self, cpu_temp: TsValue):
        with self.__cpu_temp_lock:
            self.__cpu_temp = cpu_temp

    def get_ram_perc(self):
        with self.__ram_perc_lock:
            return self.__ram_perc

    def set_ram_perc(self, ram_perc: TsValue):
        with self.__ram_perc_lock:
            self.__ram_perc = ram_perc
