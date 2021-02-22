import os
import sys
import pygame
import socket
import select
import datetime
import random
import logging
import time

import libs.networklib as networklib

from params import ch_user, ch_server

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

tourtoirac = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tourtoirac.connect((ch_server.HOST,ch_server.PORT))
logger.info(f"Connected to {ch_server.HOST}:{ch_server.PORT}")
input_list = [tourtoirac]

if __name__ == "__main__":
    while True:
        read_ready, _, _ = select.select(input_list, [], [])
        for s in read_ready:
            response=networklib.receive_message(s)
            received_data = response['data'].decode('UTF-8')
            logger.info(f"Received data : {received_data}")