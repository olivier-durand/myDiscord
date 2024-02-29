import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog

# Adresse et port du serveur
host = '10.10.98.182'
port = 9090

class Client:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        
        # Demande le surnom du client
        self.msg = tkinter.Tk()
        self.msg.withdraw()
        self.surnom = simpledialog.askstring("Surnom", "Entrez votre surnom s'il vous plaît", parent=self.msg)
        
        self.gui_done = False
        self.running = True

        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread = threading.Thread(target=self.receive)

        gui_thread.start()
        receive_thread.start()

    def gui_loop(self):
        self.win = tkinter.Tk()
        self.win.config(bg='cyan')

        self.chat_label = tkinter.Label(self.win, text="Chat", bg="cyan")
        self.chat_label.configure(font="arial 12")
        self.chat_label.pack(padx=20, pady=5)

        self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
        self.text_area.pack(padx=20, pady=5)
        self.text_area.config(state="disabled")

        self.msg_label = tkinter.Label(self.win, text="Message", bg="cyan")
        self.msg_label.config(font="arial 12")  
        self.msg_label.pack(padx=20, pady=5)

        self.saisie = tkinter.Text(self.win, height=3)
        self.saisie.pack(padx=20, pady=5)

        self.btn_envoie = tkinter.Button(self.win, text="Envoyer", command=self.ecrire)
        self.btn_envoie.configure(font="arial 12")
        self.btn_envoie.pack(padx=20, pady=5)

        self.gui_done = True

        self.win.protocol("WM_DELETE_WINDOW", self.stop)

        self.win.mainloop()

    def ecrire(self):
        message = f"{self.surnom} : {self.saisie.get('1.0', 'end')}"
        self.sock.send(message.encode('utf-8'))
        self.saisie.delete('1.0', 'end')

    def stop(self):
        self.running = False
        self.win.destroy()
        self.sock.close()

    def receive(self):
        while self.running:
            try:
                message = self.sock.recv(1024)
                if not message:  # Si le message est vide, la connexion est fermée
                    self.stop()
                    break
                if message == b'surnom':
                    self.sock.send(self.surnom.encode("utf-8"))
                else:
                    if self.gui_done:
                        self.text_area.config(state="normal")
                        self.text_area.insert("end", message.decode())
                        self.text_area.yview("end")
                        self.text_area.config(state="disabled")
            except ConnectionAbortedError:
                break
            except Exception as e:
                print("Erreur:", e)
                self.stop()
                break

    def enregistrer_message(self, message):
        # Mettez ici votre logique pour enregistrer le message
        pass

    # Méthode pour afficher la liste des utilisateurs dans une fenêtre séparée
    def show_user_list(self, cursor):
        user_list_window = tkinter.Toplevel()
        user_list_window.title("Liste des utilisateurs")
        user_list_window.geometry("300x300")  # Définir les dimensions de la fenêtre de la liste des utilisateurs

        # Récupérer la liste des utilisateurs depuis la base de données
        cursor.execute("SELECT username FROM user")
        users = cursor.fetchall()

        # Afficher les utilisateurs dans un tableau
        for i, user in enumerate(users, start=1):
            if user[0] != self.surnom:  # Ne pas afficher l'utilisateur connecté lui-même
                user_label = tkinter.Label(user_list_window, text=user[0])
                user_label.grid(row=i, column=0, padx=10, pady=5)

    # Méthodes pour ouvrir les fenêtres des différentes fonctionnalités
    def open_users_window(self):
        pass  # Remplir cette méthode pour afficher la fenêtre des utilisateurs
    
    def open_option_window(self):
        pass  # Remplir cette méthode pour afficher la fenêtre des options
    
    def open_info_window(self):
        pass  # Remplir cette méthode pour afficher la fenêtre d'informations

    def logout(self):
        pass  # Remplir cette méthode pour gérer la déconnexion

if __name__ == "__main__":
    # Initialisation du client
    client = Client(host, port)
