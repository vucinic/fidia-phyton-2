# Create server
from xmlrpc.server import SimpleXMLRPCServer

import data
import stats


class XmlRpcServe:

    def __init__(self, stats: data.StatsData):
        self.stats = stats

    def get_cpu_perc(self):
        return self.stats.get_cpu_perc()

    def get_cpu_temp(self):
        return self.stats.get_cpu_temp()

    def get_ram_perc(self):
        return self.stats.get_ram_perc()



def main():
    with SimpleXMLRPCServer(('localhost', 8000), logRequests=True) as server:
        st = stats.StatsRoutine()

        statsData = st.stats

        server.register_instance(XmlRpcServe(statsData))

        st.run()

        server.serve_forever()


if __name__ == '__main__':
    main()