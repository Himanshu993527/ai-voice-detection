import joblib

model = joblib.load("model/voice_detector.pkl")

def predict(features):
    pred = model.predict(features)[0]
    proba = model.predict_proba(features)[0]

    if pred == 1:
        return "AI_GENERATED", float(proba[1])
    else:
        return "HUMAN", float(proba[0])
