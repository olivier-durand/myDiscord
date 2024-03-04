import tkinter as tk

class Menu:
    def __init__(self):
        pygame.init()

        
root = tk.tk()
root.title("eMenu")
root.geometry("900x800")
        # Charger l'image de fond
image = Image.open("image/fond-d.jpg")

background_image = ImageTk.phtoImage(image)
       

        # Couleurs
        
        # Position et texte des boutons
        self.button_positions = {
            'Chat textuelle': (50, 50),
            'Chat vocal': (50, 100),
        }

        # Définir les actions des boutons
        self.button_actions = {
            'Chat textuelle': self.Nouvelle_partie,
            'Chat vocal': self.Choisir_pokemon,
            
        }

    

    def Chat_texte(self):
        from texte import texte
        texte = texte()
        

    def Chat_vocal(self):
        from vocal import vocal
        vocal = vocal()
       
             
if __name__ == "__main__":
    menu = Menu()
    menu.run()