import socket
import threading
import tkinter

# Fonction pour envoyer des messages au serveur
def send_message(event=None):
    message = message_entry.get()
    message_entry.delete(0, tkinter.END)
    client_socket.send(message.encode())

# Fonction pour recevoir des messages du serveur
def receive_message():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            chat_text.insert(tkinter.END, message + '\n')
        except OSError:
            break

# Configuration de la connexion au serveur
host = '127.0.0.1'
port = 55555

# Création de la fenêtre de chat
window = tkinter.Tk()
window.title('Chat en local')

# Zone de texte pour afficher les messages
chat_text = tkinter.Text(window)
chat_text.pack(fill=tkinter.BOTH, expand=True)

# Zone de texte pour saisir les messages
message_entry = tkinter.Entry(window)
message_entry.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True)
message_entry.bind("<Return>", send_message)

# Bouton pour envoyer les messages
send_button = tkinter.Button(window, text="Envoyer", command=send_message)
send_button.pack(fill=tkinter.BOTH, side=tkinter.RIGHT)

# Connexion au serveur
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# Démarrer un thread pour recevoir les messages du serveur
receive_thread = threading.Thread(target=receive_message)
receive_thread.start()

# Démarrer la boucle principale de l'interface graphique
window.mainloop()

# Fermer la connexion avec le serveur
client_socket.close()
