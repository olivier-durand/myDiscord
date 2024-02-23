import threading
import queue
import sounddevice as sd
import numpy as np
import socket

# Variables globales
RECORD_BLOCK_SIZE = 1024
PLAY_BLOCK_SIZE = 1024
RECORD_DEVICE = None
PLAY_DEVICE = None
RECORD_CHANNELS = 1
PLAY_CHANNELS = 1
RECORD_STREAM = None
PLAY_STREAM = None
RECORD_QUEUE = queue.Queue()
PLAY_QUEUE = queue.Queue()

def record_callback(indata, frames, time, status):
    RECORD_QUEUE.put(indata.copy())

def play_callback(outdata, frames, time, status):
    if not PLAY_QUEUE.empty():
        outdata[:] = PLAY_QUEUE.get().astype(np.float32)
    else:
        outdata.fill(0)

def record_transmit():
    global RECORD_STREAM
    with sd.InputStream(device=RECORD_DEVICE, channels=RECORD_CHANNELS, callback=record_callback, blocksize=RECORD_BLOCK_SIZE):
        while True:
            data = RECORD_QUEUE.get()

                client.send(data)

def receive_play(socket):
    global PLAY_STREAM
    with sd.OutputStream(device=PLAY_DEVICE, channels=PLAY_CHANNELS, callback=play_callback, blocksize=PLAY_BLOCK_SIZE):
        while True:
            data = socket.recv(PLAY_BLOCK_SIZE)
            PLAY_QUEUE.put(np.frombuffer(data, dtype=np.float32))

if __name__ == "__main__":
    SERVER_IP = "10.10.87.136"
    SERVER_PORT = 9001
    CLIENT_ID = input("Enter your user ID: ")

    # Connect to server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((SERVER_IP, SERVER_PORT))
    server_socket.send(CLIENT_ID.encode())

    # Specify recipient
    recipient_id = input("Enter recipient ID: ")
    server_socket.send(recipient_id.encode())

    # Threads for record-transmit and receive-play
    record_transmit_thread = threading.Thread(target=record_transmit)
    receive_play_thread = threading.Thread(target=receive_play, args=(server_socket,))
    record_transmit_thread.start()
    receive_play_thread.start() 