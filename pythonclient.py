import tkinter as tk
import pyaudio
import wave
from pydub import AudioSegment

class EnregistreurAudio:
    def __init__(self, format_audio=pyaudio.paInt16, canaux=2, frequence_echantillonnage=44100, chunk=1024):
        self.format_audio = format_audio
        self.canaux = canaux
        self.frequence_echantillonnage = frequence_echantillonnage
        self.chunk = chunk

    def enregistrer_audio(self, nom_fichier, duree_seconde):
        enregistreur_audio = pyaudio.PyAudio()

        stream = enregistreur_audio.open(format=self.format_audio,
                                          channels=self.canaux,
                                          rate=self.frequence_echantillonnage,
                                          input=True,
                                          frames_per_buffer=self.chunk)

        print("Enregistrement en cours...")

        frames = []

        for i in range(int(self.frequence_echantillonnage / self.chunk * duree_seconde)):
            donnees_audio = stream.read(self.chunk)
            frames.append(donnees_audio)

        print("Enregistrement terminé.")

        stream.stop_stream()
        stream.close()
        enregistreur_audio.terminate()

        wave_writer = wave.open(nom_fichier, 'wb')
        wave_writer.setnchannels(self.canaux)
        wave_writer.setsampwidth(enregistreur_audio.get_sample_size(self.format_audio))
        wave_writer.setframerate(self.frequence_echantillonnage)
        wave_writer.writeframes(b''.join(frames))
        wave_writer.close()

def convertir_wav_mp3(nom_fichier_wav, nom_fichier_mp3):
    audio = AudioSegment.from_wav(nom_fichier_wav)
    audio.export(nom_fichier_mp3, format="mp3")

def enregistrer_et_convertir():
    duree_seconde = int(duree_entry.get())
    enregistreur = EnregistreurAudio()
    nom_fichier_wav = "enregistrement.wav"
    nom_fichier_mp3 = "enregistrement.mp3"
    enregistreur.enregistrer_audio(nom_fichier_wav, duree_seconde)
    convertir_wav_mp3(nom_fichier_wav, nom_fichier_mp3)
    print("Enregistrement terminé et converti en MP3.")

# Interface graphique Tkinter
root = tk.Tk()
root.title("Enregistrement Audio")

label = tk.Label(root, text="Durée de l'enregistrement (en secondes):")
label.pack()

duree_entry = tk.Entry(root)
duree_entry.pack()

enregistrer_button = tk.Button(root, text="Enregistrer et Convertir en MP3", command=enregistrer_et_convertir)
enregistrer_button.pack()

root.mainloop()
