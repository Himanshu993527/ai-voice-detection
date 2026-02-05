from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI is running on Render"}

@app.get("/test")
def test():
    return {"status": "OK"}
