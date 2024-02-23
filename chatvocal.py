from vidstream import AudioSender
from vidstream import AudioReceiver
import threading
import socket
import sys

# Configuration des adresses IP et des ports
RECEIVER_IP = '127.0.0.1'
RECEIVER_PORT = 9999
SENDER_IP = '127.0.0.1'
SENDER_PORT = 5555

# Création du récepteur et de l'expéditeur audio
receiver = AudioReceiver(RECEIVER_IP, RECEIVER_PORT)
sender = AudioSender(SENDER_IP, SENDER_PORT)

# Fonctions pour démarrer le serveur et le flux audio
def start_receiver():
    receiver.start_server()

def start_sender():
    sender.start_stream()

# Création des threads pour démarrer le serveur et le flux audio
receiver_thread = threading.Thread(target=start_receiver)
sender_thread = threading.Thread(target=start_sender)

# Démarrage des threads
receiver_thread.start()
sender_thread.start()

# Attente de la fin des threads avant de quitter le programme
try:
    while threading.active_count() > 0:
        pass
except KeyboardInterrupt:
    receiver.stop_server()
    sender.stop_stream()
    sys.exit(0)


