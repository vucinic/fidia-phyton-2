import xmlrpc.client

with xmlrpc.client.ServerProxy('http://localhost:8000', verbose=False) as s:

    print(s.get_cpu_perc())
    print(s.get_cpu_temp())
    print(s.get_ram_perc())