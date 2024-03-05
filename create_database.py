import pygame
import sqlite3

def creer_base_donnees():
    # Connexion à la base de données (créera un nouveau fichier messages.db si inexistant)
    connexion = sqlite3.connect('messages.db')

    # Création d'un curseur pour exécuter des requêtes SQL
    curseur = connexion.cursor()

    # Création de la table messages si elle n'existe pas déjà
    curseur.execute('''CREATE TABLE IF NOT EXISTS messages
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      texte TEXT NOT NULL)''')

    # Valider les changements et fermer la connexion
    connexion.commit()
    connexion.close()

# Appel de la fonction pour créer la base de données
creer_base_donnees()