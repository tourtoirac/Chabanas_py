import socket, logging, random, select, datetime
from params import ch_server, ch_user
import networklib

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

user_nickame=f"{ch_user.nickname}_{random.randint(1,100000)}"

tourtoirac = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tourtoirac.setblocking(False)


try:
    while True:
        read_ready, _, _ = select.select(input_list, [], [])
        for s in read_ready:
            response = networklib.receive_message(s)
            received_data = response['data'].decode('UTF-8')
            logger.info(f"tourtoirac redirected message: {received_data}")
        if last_message_sent+datetime.timedelta(seconds=random.randint(5, 15)/10) < datetime.datetime.now():
            message=networklib.prepare_message(f"{user_nickame} - new value: {random.randint(1,100000)}")
            tourtoirac.send (message)
except KeyboardInterrupt:
    logging.info("{user_nickame}. Keyboard interrupt detected. Exiting")
finally:
    tourtoirac.close()