import gevent
import gevent.pywsgi
import gevent.queue
import base64

from tinyrpc.server.gevent import RPCServerGreenlets
from tinyrpc.dispatch import RPCDispatcher
from tinyrpc.protocols.jsonrpc import JSONRPCProtocol
from tinyrpc.transports.wsgi import WsgiServerTransport

dispatcher = RPCDispatcher()
transport = WsgiServerTransport(max_content_length=20 * 1024 * 1024, queue_class=gevent.queue.Queue)

# start wsgi server as a background-greenlet
wsgi_server = gevent.pywsgi.WSGIServer(('127.0.0.1', 8000), transport.handle)
gevent.spawn(wsgi_server.serve_forever)

rpc_server = RPCServerGreenlets(
    transport,
    JSONRPCProtocol(),
    dispatcher
)

@dispatcher.public
def reverse_string(s):
    return s[::-1]

@dispatcher.public
def accept_file(name, content):
    # Decode the base64 content
    binary_data = base64.b64decode(content)
    # Save the binary data to a file
    with open(name, 'wb') as f:
        f.write(binary_data)

# in the main greenlet, run our rpc_server
rpc_server.serve_forever()