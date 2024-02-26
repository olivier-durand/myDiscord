import socket
import threading

# Fonction pour gérer les connexions des clients
def handle_client(client_socket, client_address):
    print(f"Connexion acceptée depuis {client_address}")

    while True:
        # Recevoir les données du client
        data = client_socket.recv(1024)
        if not data:
            break

        # Afficher le message reçu
        print(f"Message de {client_address}: {data.decode()}")

        # Envoyer le message à tous les autres clients
        for client in clients:
            if client != client_socket:
                client.send(data)

    # Fermer la connexion avec le client
    print(f"Connexion avec {client_address} fermée.")
    client_socket.close()

# Adresse et port du serveur
host = '10.10.93.165'
port = 9090

# Créer un socket pour le serveur
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

print(f"Serveur en écoute sur {host}:{port}")

# Liste pour stocker les connexions des clients
clients = []

while True:
    # Accepter les connexions entrantes
    client_socket, client_address = server.accept()
    clients.append(client_socket)

    # Démarrer un thread pour gérer la connexion du client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()


