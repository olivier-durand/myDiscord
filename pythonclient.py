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

if __name__ == "__main__":
    enregistreur = EnregistreurAudio()
    nom_fichier_wav = "enregistrement.wav"
    nom_fichier_mp3 = "enregistrement.mp3"
    duree_seconde = 30

    enregistreur.enregistrer_audio(nom_fichier_wav, duree_seconde)
    convertir_wav_mp3(nom_fichier_wav, nom_fichier_mp3)
