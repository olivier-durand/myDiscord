import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
import os


def submit_form():
    email = email_entry.get()
    password = password_entry.get()
    # Remplacez cette logique par votre propre vérification d'authentification
    if email == "laplateforme.io" and password == "password":
        messagebox.showinfo("Connexion réussie", "Connexion réussie !")
    else:
        messagebox.showerror("Erreur de connexion", "Adresse email ou mot de passe incorrect.")

def create_account():
    # Ajoutez ici la logique pour créer un nouveau compte
    messagebox.showinfo("Créer un compte", "Créer un compte")

def toggle_password_visibility():
    global show_password
    show_password = not show_password
    if show_password:
        show_hide_button.config(image=eye_open_image)
        password_entry.config(show="")
    else:
        show_hide_button.config(image=eye_closed_image)
        password_entry.config(show="*")

def forgot_password():
    # Demander à l'utilisateur son adresse e-mail
    email = simpledialog.askstring("Mot de passe oublié", "Veuillez entrer votre adresse e-mail de récupération:")
    if email:
        messagebox.showinfo("Réinitialisation du mot de passe", f"Un lien de réinitialisation a été envoyé à {email}. Veuillez vérifier votre boîte de réception.")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Page d'accueil Discord")
root.geometry("800x700")  # Définition de la taille de la fenêtre à 900x800 pixels

# Ouverture de l'image avec PIL
image = Image.open("image/fond-d.jpg")
# Conversion de l'image en format compatible avec Tkinter
background_image = ImageTk.PhotoImage(image)

# Création de la zone de canevas pour afficher l'image de fond et les éléments d'interface utilisateur
canvas = tk.Canvas(root, width=800, height=700)
canvas.pack()

# Affichage de l'image de fond
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

# Affichage des textes en blanc
canvas.create_text(450, 150, text="Bienvenue sur Discord", font=("Helvetica", 24), fill="white")
canvas.create_text(450, 200, text="Adresse mail ou numéro de téléphone :", fill="white")
canvas.create_text(450, 280, text="Mot de passe :", fill="white")
#canvas.create_text(450, 500, text="Mot de passe oublié ?", fill="white")

# Création des champs de saisie
email_entry = tk.Entry(root)
canvas.create_window(450, 230, window=email_entry)

password_entry = tk.Entry(root, show="*")
canvas.create_window(450, 310, window=password_entry)

# Chargement de l'image de l'œil
eye_open_image = Image.open("image/eye_open.jpeg")
eye_closed_image = Image.open("image/eye_closed.jpeg")

# Redimensionnement de l'image de l'œil ouvert
eye_open_image = eye_open_image.resize((30, 30))

# Redimensionnement de l'image de l'œil fermé
eye_closed_image = eye_closed_image.resize((30, 30))

# Conversion de l'image redimensionnée en format compatible avec Tkinter
eye_open_image = ImageTk.PhotoImage(eye_open_image)
eye_closed_image = ImageTk.PhotoImage(eye_closed_image)

# Bouton pour afficher ou masquer le mot de passe
show_password = False
show_hide_button = tk.Button(root, image=eye_closed_image, command=toggle_password_visibility, bg="black")
canvas.create_window(450, 380, window=show_hide_button)

# Création des boutons
login_button = tk.Button(root, text="Se connecter", command=submit_form, bg="blue", fg="white")
canvas.create_window(450, 450, window=login_button)

create_account_button = tk.Button(root, text="Créer un compte",  command=lambda: [root.destroy(), os.system("python menu.py")], bg="blue", fg="white")
canvas.create_window(450, 580, window=create_account_button)


forgot_password_button = tk.Button(root, text="Mot de passe oublié ?", command=forgot_password, bg="white", fg="black")
canvas.create_window(450, 530, window=forgot_password_button)

# Lancement de la boucle principale de l'interface utilisateur
root.mainloop()