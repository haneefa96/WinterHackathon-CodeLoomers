from google.cloud import speech


def transcribe(audio_bytes):
    try:
        client = speech.SpeechClient()
        
        # Detect audio encoding if possible or try default
        # Streamlit often sends bytes that might be WAV or weird wrappers depending on the recorder component
        # We will try to recognize it as LINEAR16 or WEBM_OPUS which are common web formats
        
        audio = speech.RecognitionAudio(content=audio_bytes)
        
        # Configure for automatic language detection or specific Indian English/Hindi
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16, # Try WAV/Linear16 first
            # sample_rate_hertz=44100, # Let it auto-detect if possible
            language_code="hi-IN",
            alternative_language_codes=["en-IN", "ta-IN", "kn-IN"],
            enable_automatic_punctuation=True,
        )

        response = client.recognize(config=config, audio=audio)
        
        if not response.results:
            return "Could not transcribe audio. Please try again or type directly."

        transcript = " ".join(result.alternatives[0].transcript for result in response.results)
        return transcript

    except Exception as e:
        print(f"Speech API Error: {e}")
        # Build logic: if error is about content, return safe error
        return f"Error processing audio: {str(e)[:50]}..."

def transcribe_audio(audio_bytes):
    return transcribe(audio_bytes)
