class TsValue:

    def __init__(self, ts: int, value: float):
        self.__ts = ts
        self.__value = value

    def get_ts(self):
        return self.__ts

    def get_value(self):
        return self.__value


class StatsData:
    __cpu_perc: TsValue
    __ram_perc: TsValue
    __cpu_temp: TsValue

    def __init__(self, cpu_perc: TsValue, ram_perc: TsValue, cpu_temp: TsValue):
        self.__cpu_perc = cpu_perc
        self.__ram_perc = ram_perc
        self.__cpu_temp = cpu_temp

    def get_cpu_perc(self):
        return self.__cpu_perc

    def set_cpu_perc(self, cpu_perc):
        self.__cpu_perc = cpu_perc

    def get_cpu_temp(self):
        return self.__cpu_temp

    def set_cpu_temp(self, cpu_temp):
        self.__cpu_temp = cpu_temp

    def get_ram_perc(self):
        return self.__ram_perc

    def set_ram_perc(self, ram_perc):
        self.__ram_perc = ram_perc
