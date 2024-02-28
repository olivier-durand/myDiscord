import mysql.connector


class Database_Discord():
    connexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="azerty",
            database="myDiscord"
        )

    curseur = connexion.cursor()