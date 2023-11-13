import xmlrpc.client
from xmlrpc.client import Fault

with xmlrpc.client.ServerProxy('http://localhost:8000/fidia-rpc', verbose=False) as s:
    try:
        print(s.pow(2, 'asd'))  # Returns 2**3 = 8
    except Fault as error:
        print(error.faultCode)
        print(error.faultString)

    try:
        print(s.ginopino(2, 'asd'))  # Returns 2**3 = 8
    except xmlrpc.client.Fault as error:
        print(error)
    print(s.add(2, 3, 4, 5, 6, 7, 8, 9, 9))  # Returns 5
    # print(s.mul(5, 2))  # Returns 5*2 = 10
    #
    print(s.system.listMethods())
    #
    # for i in [n for n in s.system.listMethods() if 'system' not in n]:
    #     print(i, s.system.methodSignature(i), s.system.methodHelp(i))
