from google.cloud import speech

def transcribe(audio_bytes):
    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(content=audio_bytes)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.WEBM_OPUS,
        language_code="hi-IN",  # or kn-IN, ta-IN
    )

    response = client.recognize(config=config, audio=audio)
    return " ".join(r.alternatives[0].transcript for r in response.results)

def transcribe_audio(audio_bytes):
    return "transcription will come here"
