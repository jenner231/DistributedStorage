# Weather update client
# Connects SUB socket to tcp://localhost:5556
# Collects weather updates and finds avg temp in zipcode
#
import sys
import zmq
import weatherupdate_message_pb2
# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5556")
# Subscribe to zipcode, default is NYC, 10001
zip_filter = sys.argv[1] if len(sys.argv) > 1 else ""
socket.setsockopt_string(zmq.SUBSCRIBE, zip_filter)
print(f"Collecting updates from weather server of zip code {zip_filter}")
# Process 5 updates
total_temp = 0
for update_nbr in range(5):
    pb_file_recv = weatherupdate_message_pb2.file()
    
    string = socket.recv()
    pb_file_recv.ParseFromString(string)
    # The parsed file has the same attributes as the original did
    zipcode, temperature, relhumidity = pb_file_recv.zipcode, pb_file_recv.temperature, pb_file_recv.relhumidity
    total_temp += int(temperature)
    print(f"Average temperature for zipcode '{zipcode}' was {total_temp / (update_nbr+1)}F")