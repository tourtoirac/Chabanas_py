import socket, select, logging
from params import ch_server
import libs.networklib as networklib
import libs.tools as tools

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server_address = (ch_server.HOST, ch_server.PORT)
server.bind(server_address)
logger.info(f"Server connected to {ch_server.HOST}:{ch_server.PORT}")
server.listen()

input_list = [server]
client_list = []

try:
    while True:
        read_ready, _, _ = select.select(input_list, [], [])
        for notified_socket in read_ready:
            # accept connection if server is read-ready
            if notified_socket is server:
                connection, client_address = notified_socket.accept()
                logger.info(f"server received connection: socket {connection.fileno()}")
                input_list.append(connection)
                client_list.append(connection)
            # receive message if a connection is read-ready
            else:
                message = networklib.receive_message(notified_socket)
                if not message:
                    logger.info(f"client {notified_socket} is no longer responding. Closing the connection")
                    input_list.remove(notified_socket)
                    client_list.remove(notified_socket)
                else:
                    response=tools.process_command(message)
                    if response['target_socket'] == 'sender':
                        logger.debug("Target socket = sender")
                        response = networklib.prepare_message(response)
                        notified_socket.send(response)
                    elif response['target_socket'] == 'others':
                        logger.debug("Target socket = everyone but sender")
                        response = networklib.prepare_message(response)
                        for client_socket in client_list:
                            if client_socket != notified_socket:
                                client_socket.send(response)
                    else:
                        logger.debug("Target socket = everyone")
                        response = networklib.prepare_message(response)
                        for client_socket in client_list:
                            client_socket.send(response)
                    logger.debug("Response sent")

except KeyboardInterrupt:
    logger.info("Keyboard interrupt catch. Exiting")
finally:
    server.close()