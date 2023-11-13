import datetime
import xmlrpc.client
from xmlrpc.server import SimpleXMLRPCRequestHandler
from xmlrpc.server import SimpleXMLRPCServer


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/fidia-rpc',)


def adder_function(*args):
    return sum(args)


class MyFuncs:
    def mul(self, x, y):
        return x * y


def today():
    """
    This method return the current date
    :return:
    """
    now = datetime.datetime.today()
    print(now)
    return xmlrpc.client.DateTime(now)


def python_logo():
    with open("python_logo.jpg", "rb") as handle:
        return xmlrpc.client.Binary(handle.read())



# Create server
with SimpleXMLRPCServer(
        ('localhost', 8000),
        requestHandler=RequestHandler,
        logRequests=True) as server:
    server.register_introspection_functions()

    print(today())


    # Register pow() function; this will use the value of
    # pow.__name__ as the name, which is just 'pow'.
    server.register_function(pow)

    server.register_function(adder_function, 'add')
    server.register_function(today, 'today')
    server.register_function(python_logo, 'logo')

    # Register an instance; all the methods of the instance are
    # published as XML-RPC methods (in this case, just 'mul').

    server.register_instance(MyFuncs())

    # Run the server's main loop
    server.serve_forever()
