from fastapi import FastAPI

app = FastAPI(
    title="AI Voice Detection API",
    description="Detect AI-generated vs Human voice",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

@app.get("/")
def root():
    return {"message": "FastAPI is running on Render"}

@app.get("/health")
def health():
    return {"status": "ok"}

