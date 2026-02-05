from fastapi import FastAPI, Depends, HTTPException
from app.auth import validate_api_key
from app.audio_utils import load_audio_from_base64
from app.features import extract_features
from app.model import predict
from app.explain import generate_explanation
from app.config import ALLOWED_LANGUAGES

app = FastAPI()

@app.post("/api/voice-detection")
def detect_voice(data: dict, api_key: str = Depends(validate_api_key)):

    if data["language"] not in ALLOWED_LANGUAGES:
        raise HTTPException(status_code=400, detail="Unsupported language")

    y, sr = load_audio_from_base64(data["audioBase64"])
    features = extract_features(y, sr)

    prediction, confidence = predict(features)

    return {
        "status": "success",
        "language": data["language"],
        "classification": prediction,
        "confidenceScore": round(float(confidence), 2),
        "explanation": generate_explanation(confidence, prediction)
    }
