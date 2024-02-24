import sounddevice as sd
import numpy as np
import pygame
import matplotlib.pyplot as plt
import random

class AudioProcessor:
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate

    def record_audio(self, duration):
        print("Recording...")
        audio_data = sd.rec(int(duration * self.sample_rate), samplerate=self.sample_rate, channels=2, dtype=np.int16)
        sd.wait()
        print("Recording finished.")
        return audio_data

    def play_audio(self, audio_data):
        pygame.mixer.init(frequency=self.sample_rate, channels=2)
        sound = pygame.sndarray.make_sound(audio_data)
        print("Playing...")
        sound.play()
        pygame.time.wait(int(audio_data.shape[0] / self.sample_rate * 1000))
        print("Playing finished.")

    def plot_audio_waveform(self, audio_data, save_plot=True, plot_filename='audio_waveform.png'):
        time = np.arange(0, len(audio_data)) / self.sample_rate
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
    audio_processor = AudioProcessor()
    duration = 5
    recorded_audio = audio_processor.record_audio(duration)
    audio_processor.play_audio(recorded_audio)
    audio_processor.plot_audio_waveform(recorded_audio)
