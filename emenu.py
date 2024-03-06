import tkinter as tk
from PIL import Image, ImageTk

class Menu:
    def __init__(self, master):
        self.master = master
        master.title("eMENU")
        master.geometry("900x800")

        # Charger l'image de fond
        image = Image.open("image/fond-d.jpg")
        self.background_image = ImageTk.PhotoImage(image)

        # Créer un Canvas pour afficher l'image de fond
        self.canvas = tk.Canvas(master, width=900, height=800)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)

        # Affichage des textes en blanc
        self.canvas.create_text(450, 150, text="Bienvenue sur le Channel Discord!", font=("Helvetica", 40), fill="white")

        # Position et texte des boutons
        self.button_texts = ['Messagerie instantanée', 'Voice Chat', 'Déconnexion']

        # Définir les actions des boutons
        self.button_actions = {
            'Messagerie instantanée': self.import_chat,
            'Voice Chat': self.import_vocal,
            'Déconnexion': self.disconnect
        }
        
        # Créer les boutons
        self.create_buttons()

    def create_buttons(self):
        # Créer les boutons et les positionner
        for i, button_text in enumerate(self.button_texts):
            if button_text == 'Déconnexion':
                login_button = tk.Button(self.master, text=button_text, command=self.button_actions[button_text], fg="black", width=10, font=("Helvetica", 12), anchor="center")
                self.canvas.create_window(450, 700, window=login_button)  # Placer le bouton "Déconnexion" plus bas
            else:
                login_button = tk.Button(self.master, text=button_text, command=self.button_actions[button_text], bg="blue", fg="white", width=20, font=("Helvetica", 15), anchor="center")
                self.canvas.create_window(450, 300 + 100 * i, window=login_button)

    def import_chat(self):
        import chat

    def import_vocal(self):
        import pythonclient

    def disconnect(self):
        self.master.destroy()


root = tk.Tk()
menu = Menu(root)
root.mainloop()
