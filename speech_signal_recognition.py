import sounddevice as sd
import numpy as np
import pygame
import matplotlib.pyplot as plt
import random

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

def plot_audio_waveform(audio_data, sample_rate=44100, save_plot=True, plot_filename='audio_waveform.png'):
    time = np.arange(0, len(audio_data)) / sample_rate
    plt.figure(figsize=(10, 4))
    
    # Generating random colors
    color_left = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    color_right = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    
    plt.plot(time, audio_data[:, 0], label='Left channel', color=color_left)
    plt.plot(time, audio_data[:, 1], label='Right channel', color=color_right)
    
    plt.title('Audio Waveform')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()
    
    if save_plot:
        plt.savefig(plot_filename)
        print(f"Plot saved as {plot_filename}")
    else:
        plt.show()

if __name__ == "__main__":
    duration = 3
    recorded_audio = record_audio(duration)
    play_audio(recorded_audio)
    plot_audio_waveform(recorded_audio)
