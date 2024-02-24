# Audio Recorder and Player

This Python script facilitates audio recording, playback, and waveform visualization using sounddevice, pygame, and matplotlib.

## Dependencies

- Python 3.x
- sounddevice
- numpy
- pygame
- matplotlib

Install the dependencies using:

```bash
pip install sounddevice numpy pygame matplotlib
```

## Usage

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

2. **Run the script:**

```bash
python audio_recorder_player.py
```

Adjust the `duration` variable in the script to change the recording length.

## Functions

### 1. Record Audio

```python
def record_audio(duration, sample_rate=44100):
    # ...
```

Records audio for the specified duration.

### 2. Play Audio

```python
def play_audio(audio_data, sample_rate=44100):
    # ...
```

Plays back the recorded audio using pygame.

### 3. Plot Audio Waveform

```python
def plot_audio_waveform(audio_data, sample_rate=44100, save_plot=True, plot_filename='audio_waveform.png'):
    # ...
```

Plots and optionally saves the audio waveform using matplotlib.

## Example

```python
if __name__ == "__main__":
    duration = 3
    recorded_audio = record_audio(duration)
    play_audio(recorded_audio)
    plot_audio_waveform(recorded_audio)
```

This script records audio for 3 seconds, plays it back, and plots the waveform.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.