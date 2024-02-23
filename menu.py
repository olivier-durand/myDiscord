import tkinter as tk    
from tkinter import messagebox
from PIL import Image, ImageTk

def toggle_password_visibility():
    global show_password, motdepasse_entry, confirmermotdepasse_entry, eye_open_image, eye_closed_image
    
    if show_password:
        motdepasse_entry.config(show="*")
        confirmermotdepasse_entry.config(show="*")
        show_hide_button.config(image=eye_closed_image)
    else:
        motdepasse_entry.config(show="")
        confirmermotdepasse_entry.config(show="")
        show_hide_button.config(image=eye_open_image)
        
    show_password = not show_password

def submit_form():
    # Fonction pour soumettre le formulaire
    pass

root = tk.Tk()  # Correction 1
root.title("page d'inscription Discord")  # Correction 2
root.geometry("800x700")

image = Image.open("image/fond-d.jpg")
background_image = ImageTk.PhotoImage(image)  # Correction de la variable typo

canvas = tk.Canvas(root, width=800, height=700)  # Correction 3
canvas.pack()

canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

# Afficher des textes en blanc
canvas.create_text(450, 150, text="Bienvenue sur Discord", font=("helvetica", 24), fill="black")  # Correction 4
canvas.create_text(450, 200, text="Nom :", fill="white")  # Correction 4
canvas.create_text(450, 260, text="Prénom :", fill="white")  # Correction 4
canvas.create_text(450, 310, text="Adresse mail :", fill="white")  # Correction 4
canvas.create_text(450, 360, text="Mot de passe :", fill="white")  # Correction 4
canvas.create_text(450, 410, text="Confirmer votre mot de passe :", fill="white")

# création des champs pour saisie
nom_entry = tk.Entry()
canvas.create_window(450, 230, window=nom_entry)
prenom_entry = tk.Entry()
canvas.create_window(450, 280, window=prenom_entry)
email_entry = tk.Entry()
canvas.create_window(450, 330, window=email_entry)  # Correction de la méthode
motdepasse_entry = tk.Entry(root, show="*")
canvas.create_window(450, 380, window=motdepasse_entry)
confirmermotdepasse_entry = tk.Entry(root, show="*")
canvas.create_window(450, 430, window=confirmermotdepasse_entry)
# image de l'oeil
eye_open_image = Image.open("image/eye_open.jpeg")
eye_closed_image = Image.open("image/eye_closed.jpeg")

# redimensionnement de l'image
eye_open_image = eye_open_image.resize((20, 20))
eye_closed_image = eye_closed_image.resize((20, 20))

# conversion de l'image redimensionnée
eye_open_image = ImageTk.PhotoImage(eye_open_image)
eye_closed_image = ImageTk.PhotoImage(eye_closed_image)

# bouton pour afficher ou masquer le mot de passe 
show_password = False
show_hide_button = tk.Button(root, image=eye_closed_image, command=toggle_password_visibility, bg="black")
canvas.create_window(450, 480, window=show_hide_button)

# bouton d'inscription
login_button = tk.Button(root, text="S'inscrire", command=submit_form, bg="blue", fg="white")  # Correction de la typo
canvas.create_window(450, 580, window=login_button)

root.mainloop()
