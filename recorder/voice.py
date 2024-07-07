import pyaudio
import wave
from pydub import AudioSegment

# Settings for recording
FORMAT = pyaudio.paInt16  # Format of sampling 16 bits
CHANNELS = 1              # Number of channels, 1 for mono and 2 for stereo
RATE = 44100              # Sampling rate, how many samples per second
CHUNK = 1024              # How many frames per buffer
WAVE_OUTPUT_FILENAME = "output.wav"  # Name of the output file

audio = pyaudio.PyAudio()

# Start Recording
def start_recording(record_seconds):
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("Recording...")
    frames = []

    for i in range(0, int(RATE / CHUNK * record_seconds)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording.")

    stream.stop_stream()
    stream.close()

    # Save the recorded data as a WAV file
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

# Play Recording
def play_recording():
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'rb')

    stream = audio.open(format=audio.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

    data = wf.readframes(CHUNK)

    while data:
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

# Convert WAV to another format using pydub
def convert_format(output_format):
    audio = AudioSegment.from_wav(WAVE_OUTPUT_FILENAME)
    output_file = f"output.{output_format}"
    audio.export(output_file, format=output_format)
    print(f"Saved as {output_file}")

# Main function to control the application
def main():
    while True:
        print("\nVoice Recorder Application")
        print("1. Record")
        print("2. Play")
        print("3. Convert Format")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                record_seconds = int(input("Enter recording duration in seconds: "))
                start_recording(record_seconds)
            except ValueError:
                print("Invalid input. Please enter a valid number for recording duration.")
        elif choice == '2':
            play_recording()
        elif choice == '3':
            output_format = input("Enter the format to convert to (e.g., mp3, flac, etc.): ")
            convert_format(output_format)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

    audio.terminate()

if __name__ == "__main__":
    main()
