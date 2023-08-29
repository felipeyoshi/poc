import assemblyai as aai
import time

class TranscriberTest:

    def __init__(self, api_key):
        aai.settings.api_key = api_key
        self.language = aai.TranscriptionConfig(language_code="pt")
        self.client = aai.Transcriber(config=self.language)
        
        

    def transcribe_audio(self, file_name):
        print("Starting transcription...")
        transcript = self.client.transcribe(file_name)
        time.sleep(30)
        print("Transcription completed!")
        return transcript.text