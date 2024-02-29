import pyaudio

import wave
from pydub import AudioSegment

def enregistrer_audio(nom_fichier, duree_seconde):
    chunk = 1024  
    format_audio = pyaudio.paInt16
    canaux = 2  
    frequence_echantillonnage = 44100  
    temps_enregistrement = duree_seconde  

    enregistreur_audio = pyaudio.PyAudio()

    stream = enregistreur_audio.open(format=format_audio,
                                      channels=canaux,
                                      rate=frequence_echantillonnage,
                                      input=True,
                                      frames_per_buffer=chunk)

    print("Enregistrement en cours...")

    frames = []

    for i in range(int(frequence_echantillonnage / chunk * temps_enregistrement)):
        donnees_audio = stream.read(chunk)
        frames.append(donnees_audio)

    print("Enregistrement terminé.")

    stream.stop_stream()
    stream.close()
    enregistreur_audio.terminate()

    wave_writer = wave.open(nom_fichier, 'wb')
    wave_writer.setnchannels(canaux)
    wave_writer.setsampwidth(enregistreur_audio.get_sample_size(format_audio))
    wave_writer.setframerate(frequence_echantillonnage)
    wave_writer.writeframes(b''.join(frames))
    wave_writer.close()

def convertir_wav_mp3(nom_fichier_wav, nom_fichier_mp3):
    audio = AudioSegment.from_wav(nom_fichier_wav)
    audio.export(nom_fichier_mp3, format="mp3")

if __name__ == "__main__":
    nom_fichier_wav = "enregistrement.wav"
    nom_fichier_mp3 = "enregistrement.mp3"
    duree_seconde = 30

    enregistrer_audio(nom_fichier_wav, duree_seconde)
    convertir_wav_mp3(nom_fichier_wav, nom_fichier_mp3)