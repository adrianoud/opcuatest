import sys
import time
from opcua import ua, Server

sys.path.insert(0, "..")
if __name__ == "__main__":

    # setup our server
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    # setup our own namespace, not really necessary but should as spec
    uri = "grundfos.com"
    idx = server.register_namespace(uri)
    print (idx)

    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()
    print(objects)

    # populating our address space
    myobj = objects.add_object(idx, "MyObject")
    myobj2 = objects.add_object(idx, "MyObject2")
    print(myobj,myobj2)
    myvar = myobj.add_variable(idx, "MyVariable", 6.7)
    myvar1 = myobj.add_variable(idx, "MyVariable1", 6.7)
    myvar.set_writable()    # Set MyVariable to be writable by clients

    # starting!
    server.start()

    try:
        count = 0
        while True:
            time.sleep(1)
            count += 0.1
            myvar.set_value(count)
            # print(count)
    finally:
        #close connection, remove subcsriptions, etc
        server.stop()