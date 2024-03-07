import pygame
import mysql.connector
from mysql.connector import Error
from datetime import datetime
from database import Database_Discord

db = Database_Discord()

class Chat:
    def __init__(self, username):
        self.username = username
        self.messages = []

    def charger_messages(self):
        connection = None
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='myDiscord',
                user='root',
                password='azerty'
            )
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("SELECT username, date_heure, message FROM messages")
                self.messages = cursor.fetchall()
        except Error as e:
            print("Erreur lors de la connexion à la base de données:", e)
        finally:
            if connection is not None and connection.is_connected():
                cursor.close()
                connection.close()

    def parler(self, message):
        now = datetime.now()
        date_heure = now.strftime("%Y-%m-%d %H:%M:%S")
        print(f"{self.username} ({date_heure}): {message}")
        self.messages.append((self.username, date_heure, message))
        self.enregistrer_message(message, date_heure)

    def enregistrer_message(self, message, date_heure):
        connection = None
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='votre_base_de_donnees',
                user='votre_utilisateur',
                password='votre_mot_de_passe'
            )
            if connection.is_connected():
                cursor = connection.cursor()
                query = "INSERT INTO messages (username, date_heure, message) VALUES (%s, %s, %s)"
                cursor.execute(query, (self.username, date_heure, message))
                connection.commit()
        except Error as e:
            print("Erreur lors de la connexion à la base de données:", e)
        finally:
            if connection is not None and connection.is_connected():
                cursor.close()
                connection.close()

# Initialisation de Pygame
pygame.init()
largeur, hauteur = 800, 600
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Chat Pygame")

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Police
police = pygame.font.Font(None, 32)

# Utilisation de la classe Chat
username = discord.utilisateur
mon_chat = Chat(username)
mon_chat.charger_messages()

running = True
message = ""
clock = pygame.time.Clock()

scroll_offset = 0
scroll_speed = 20

while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                mon_chat.parler(message)
                message = ""
            elif event.key == pygame.K_BACKSPACE:
                message = message[:-1]
            else:
                message += event.unicode
    
    # Calcul de la position des messages en fonction du décalage vertical
    y = 10 - scroll_offset
    for msg in mon_chat.messages:
        texte = f"{msg[0]} ({msg[1]}): {msg[2]}"
        surface_texte = police.render(texte, True, NOIR)
        ecran.blit(surface_texte, (10, y))
        y += 40

    # Gestion du défilement avec les touches fléchées
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        scroll_offset += scroll_speed
    if keys[pygame.K_DOWN]:
        scroll_offset -= scroll_speed

    # Limitation de la position du défilement
    max_scroll = len(mon_chat.messages) * 40 - hauteur
    scroll_offset = max(0, min(scroll_offset, max_scroll))

    # Affichage du message en cours de frappe
    zone_texte = police.render(message, True, NOIR)
    ecran.blit(zone_texte, (10, hauteur - 40))

    # Mise à jour de l'affichage
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
