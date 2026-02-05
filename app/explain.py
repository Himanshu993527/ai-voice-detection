def generate_explanation(confidence, prediction):
    if prediction == "AI_GENERATED":
        return "Unnatural pitch consistency and overly smooth spectral patterns detected"
    else:
        return "Natural vocal variations and human-like speech patterns detected"
