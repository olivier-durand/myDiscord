import speech_recognition as sr
import sqlite3

# Fonction pour enregistrer un message vocal et le stocker dans la base de données
def enregistrer_message():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        
        print("Enregistrement du message... Parlez maintenant.")
        audio = recognizer.listen(source)

    try:
        print("Transcription en cours...")
        texte = recognizer.recognize_google(audio, language='fr-FR')
        print("Message transcrit:", texte)

        # Stockage du message dans la base de données
        connexion = sqlite3.connect('messages.db')
        curseur = connexion.cursor()
        curseur.execute("INSERT INTO messages (texte) VALUES (?)", (texte,))
        connexion.commit()
        connexion.close()
        print("Message enregistre avec succes dans la base de donnees.")

    except sr.UnknownValueError:
        print("Impossible de comprendre l'audio.")
    except sr.RequestError as e:
        print("Erreur lors de la requête vers l'API Google Speech Recognition : {0}".format(e))

# Création de la table dans la base de données si elle n'existe pas
def initialiser_base_donnees():
    connexion = sqlite3.connect('messages.db')
    curseur = connexion.cursor()
    curseur.execute('''CREATE TABLE IF NOT EXISTS messages
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      texte TEXT NOT NULL)''')
    connexion.commit()
    connexion.close()

# Fonction principale pour exécuter le programme
def main():
    initialiser_base_donnees()
    enregistrer_message()

if __name__ == "__main__":
    main()
