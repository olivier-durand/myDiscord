import mysql.connector

def enregistrer_audio_db(nom_fichier_audio, chemin_audio):
    # Se connecter à la base de données MySQL
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Poussin13",
        database="myDiscord"
    )

    curseur = connexion.cursor()

# Lire les données audio depuis le fichier
with open(chemin_audio, "rb") as fichier_audio:
    donnees_audio = fichier_audio.read()

    # Insérer les données audio dans la base de données
    requete = "INSERT INTO MessagesAudio (nom_fichier, audio) VALUES (%s, %s)"
    valeurs = (nom_fichier_audio, donnees_audio)
    curseur.execute(requete, valeurs)

    # Valider la transaction
    connexion.commit()

    # Fermer la connexion
    curseur.close()
    connexion.close()

# Utilisation de la fonction pour enregistrer un message audio dans la base de données
enregistrer_audio_db("message_audio.mp3", "chemin/vers/votre/message_audio.mp3")
