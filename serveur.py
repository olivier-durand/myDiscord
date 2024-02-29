import socket
import threading

# Adresse et port du serveur
host = '10.10.98.182'
port = 9090

# Créer un socket pour le serveur
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Liste pour stocker les connexions des clients et leurs surnoms
clients = []
surnoms = []

# Fonction pour diffuser un message à tous les clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Fonction pour gérer les connexions des clients
def handle(client):
    while True:
        try:
            # Recevoir les données du client
            message = client.recv(1024)
            print(f"Surnom {surnoms[clients.index(client)]}: {message.decode('utf-8')}")
            broadcast(message)
        except:
            # Gérer les erreurs de connexion
            index = clients.index(client)
            clients.remove(client)
            client.close()
            surnom = surnoms[index]
            surnoms.remove(surnom)
            break

# Fonction pour recevoir les connexions entrantes des clients
def recevoir():
    while True:
        # Accepter une connexion entrante
        client, adress = server.accept()
        print(f"Connecté avec {str(adress)}")
        
        # Envoyer un message demandant le surnom
        client.send("SURNOM".encode("utf-8"))
        surnom = client.recv(1024).decode("utf-8")

        # Ajouter le client et son surnom à la liste
        surnoms.append(surnom)
        clients.append(client)

        # Afficher le surnom du client
        print(f"Surnom du client : {surnom}")

        # Diffuser un message informant de la connexion du client
        broadcast(f"{surnom} connecté au serveur\n".encode("utf-8"))

        # Envoyer un message de confirmation au client
        client.send("Connecté au serveur\n".encode("utf-8"))

        # Démarrer un thread pour gérer le client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

# Lancement du serveur
print("Attente de connexion...")
recevoir()
