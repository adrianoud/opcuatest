import sys
from opcua import Client

sys.path.insert(0, "..")


if __name__ == "__main__":

    client = Client("opc.tcp://localhost:4840/freeopcua/server/")
    # client = Client("opc.tcp://admin@localhost:4840/freeopcua/server/") #connect using a user
    try:
        client.connect()
        # Client has a few methods to get proxy to UA nodes that should always be in address space such as Root or Objects
        root = client.get_root_node()
        objs = client.get_objects_node()
        print("root node is: ", root)  # 整型节点  root i=84 objects i=85  另外还有字符型节点id s = xxx
        print("objects node is", objs)

        # Node objects have methods to read and write node attributes as well as browse or populate address space
        print("Children of root are: ", root.get_children())
        print("Children of objects are: ", objs.get_children())
        # get a specific node knowing its node id
        #var = client.get_node(ua.NodeId(1002, 2))
        #var = client.get_node("ns=3;i=2002")
        #print(var)
        #var.get_data_value() # get value of node as a DataValue object
        #var.get_value() # get value of node as a python builtin
        #var.set_value(ua.Variant([23], ua.VariantType.Int64)) #set node value using explicit data type
        #var.set_value(3.9) # set node value using implicit data type

        # Now getting a variable node using its browse path
        objss = root.get_child(["0:Objects"])
        obj = root.get_child(["0:Objects", "2:MyObject"])
        myvar = root.get_child(
            ["0:Objects", "2:MyObject", "2:MyVariable"])  # 2 为namespace   root -> objects -> myobj -> myvar

        value = myvar.get_value()
        print("objects", objss)
        print("myobj is: ", obj)
        print("myvar is: ", myvar)


        print(value)

        # Stacked myvar access
        # print("myvar is: ", root.get_children()[0].get_children()[1].get_variables()[0].get_value())

    finally:
        client.disconnect()