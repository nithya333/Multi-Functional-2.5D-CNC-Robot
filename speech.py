import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import QThread, pyqtSignal
from vosk import Model, KaldiRecognizer
import vosk
import pyaudio
import json
import os

vosk.SetLogLevel(-1)

def list_audio_devices():
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    p.terminate()

list_audio_devices()

my_speech = []

def save_speech_to_file(filename):
    with open(filename, 'w') as f:
        for line in my_speech:
            f.write(f"{line}\n")

class AudioThread(QThread):
    result_signal = pyqtSignal(str)
    
    def __init__(self, input_device_index=None):
        super().__init__()
        self.running = False
        self.model = Model(r"C:\\Users\\krupa\\Documents\\Exp_Learn_3rdSEM\\CNC\\GitClone\\CNC\\vosk-model-small-en-us-0.15")
        self.recognizer = KaldiRecognizer(self.model, 16000)
        self.mic = pyaudio.PyAudio()
        self.stream = None
        self.input_device_index = input_device_index
    
    def run(self):
        try:
            self.stream = self.mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True,
                                        frames_per_buffer=4096, input_device_index=self.input_device_index)
            self.stream.start_stream()
            self.running = True
            while self.running:
                try:
                    data = self.stream.read(4096, exception_on_overflow=False)
                    if self.recognizer.AcceptWaveform(data):
                        text = json.loads(self.recognizer.Result())["text"]
                        self.result_signal.emit(text)
                        if text:
                            my_speech.append(text)
                except OSError as e:
                    print(f"Error during stream read: {e}")
        except Exception as e:
            print(f"Error opening or starting stream: {e}")
    
    def stop(self):
        self.running = False
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
            self.stream = None
        self.mic.terminate()
        # Call this function after stopping the recording

# Replace `None` with the actual index of your input device
input_device_index = None  # Change this to your input device index
audio_thread = AudioThread(input_device_index)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Speech to Text Recorder")
        self.setGeometry(100, 100, 600, 400)
        
        self.label = QLabel("Press 'Start' to begin recording", self)
        self.label.setStyleSheet("font-size: 25px; margin: 20px;")
        self.label.setWordWrap(True)
        
        self.start_button = QPushButton("Start Recording", self)
        self.start_button.setStyleSheet("background-color: grey; color: white; font-size: 25px; padding: 10px;")
        self.start_button.clicked.connect(self.start_recording)
        
        self.stop_button = QPushButton("Stop Recording", self)
        self.stop_button.setStyleSheet("background-color: grey; color: white; font-size: 25px; padding: 10px;")
        self.stop_button.clicked.connect(self.stop_recording)
        self.stop_button.setEnabled(False)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        self.audio_thread = AudioThread()
        self.audio_thread.result_signal.connect(self.update_text)
    
    def start_recording(self):
        self.label.setText("Recording...")
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.audio_thread.start()
    
    def stop_recording(self):
        self.label.setText("Recording stopped. Press 'Start' to record again.")
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.audio_thread.stop()
        self.audio_thread.wait()
    
    def update_text(self, text):
        self.label.setText(f"Recorded Text: {text}")
        with open('temp_output.txt', 'a') as f:
            f.write(f"{text}\n")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
