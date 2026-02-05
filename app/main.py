
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import os

from app.audio_utils import load_audio_from_base64
from app.features import extract_features
from app.model import predict
from app.explain import generate_explanation

# -------------------------------------------------
# Initialize FastAPI app
# -------------------------------------------------
app = FastAPI(
    title="AI Voice Detection API",
    description="Detect AI-generated vs Human voice",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)
# -------------------------------------------------
# Root endpoint (IMPORTANT for Render & health check)
# -------------------------------------------------
@app.get("/")
def root():
    return {"status": "AI Voice Detection API is running"}

# -------------------------------------------------
# Request schema
# -------------------------------------------------
class VoiceRequest(BaseModel):
    language: str
    audioFormat: str
    audioBase64: str

# -------------------------------------------------
# Main detection endpoint
# -------------------------------------------------
@app.post("/api/voice-detection")
def voice_detection(
    request: VoiceRequest,
    x_api_key: str = Header(None)
):
    # -----------------------------
    # API KEY validation
    # -----------------------------
    server_api_key = os.getenv("API_KEY")

    if server_api_key is None:
        raise HTTPException(status_code=500, detail="API key not configured on server")

    if x_api_key != server_api_key:
        raise HTTPException(status_code=401, detail="Invalid API key")

    # -----------------------------
    # Validate audio format
    # -----------------------------
    if request.audioFormat.lower() != "mp3":
        raise HTTPException(status_code=400, detail="Only mp3 format is supported")

    # -----------------------------
    # Load audio from Base64
    # -----------------------------
    try:
        audio_signal, sample_rate = load_audio_from_base64(request.audioBase64)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid or corrupted audioBase64")

    # -----------------------------
    # Feature extraction
    # -----------------------------
    features = extract_features(audio_signal, sample_rate)

    # -----------------------------
    # Model prediction
    # -----------------------------
    classification, confidence = predict(features)

    # -----------------------------
    # Explanation generation
    # -----------------------------
    explanation = generate_explanation(classification, confidence)

    # -----------------------------
    # Final response
    # -----------------------------
    return {
        "status": "success",
        "language": request.language,
        "classification": classification,
        "confidenceScore": round(float(confidence), 2),
        "explanation": explanation
    }
