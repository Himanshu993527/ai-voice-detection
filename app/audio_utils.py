import base64
import io
import librosa

def load_audio_from_base64(audio_base64):
    audio_bytes = base64.b64decode(audio_base64)
    audio_stream = io.BytesIO(audio_bytes)
    y, sr = librosa.load(audio_stream, sr=None)
    return y, sr
