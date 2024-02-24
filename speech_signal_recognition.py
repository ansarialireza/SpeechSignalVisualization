import sounddevice as sd
import numpy as np
import pygame
import matplotlib.pyplot as plt

def record_audio(duration, sample_rate=44100):
    print("Recording...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype=np.int16)
    sd.wait()
    print("Recording finished.")
    return audio_data

def play_audio(audio_data, sample_rate=44100):
    pygame.mixer.init(frequency=sample_rate, channels=2)
    sound = pygame.sndarray.make_sound(audio_data)
    print("Playing...")
    sound.play()
    pygame.time.wait(int(audio_data.shape[0] / sample_rate * 1000))
    print("Playing finished.")

def plot_audio_waveform(audio_data, sample_rate=44100):
    time = np.arange(0, len(audio_data)) / sample_rate
    plt.figure(figsize=(10, 4))
    plt.plot(time, audio_data[:, 0], label='Left channel')
    plt.plot(time, audio_data[:, 1], label='Right channel')
    plt.title('Audio Waveform')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    duration = 5  # مدت زمان ضبط صدا به ثانیه
    recorded_audio = record_audio(duration)
    play_audio(recorded_audio)
    plot_audio_waveform(recorded_audio)
