# 🎙️ AI-Generated Voice Detection API  
**(Tamil | English | Hindi | Malayalam | Telugu)**

---

## 📌 Project Overview

This project provides a **secure REST API** that detects whether a given voice sample is **AI-generated** or **spoken by a real human**.

The system supports **five languages** and processes **Base64-encoded MP3 audio** files.  
It is built specifically for **AI voice forensics, misuse detection, and hackathon evaluation**.

---

## 🚀 Features

- 🎧 Accepts **one MP3 audio file per request**
- 🔐 Secured using **API Key authentication**
- 🌍 Supports **5 languages**:
  - **Tamil**
  - **English**
  - **Hindi**
  - **Malayalam**
  - **Telugu**
- 🧠 Uses **machine learning** for classification
- 📊 Returns **confidence score**
- 🧾 Provides a **short explanation**
- 📦 JSON-based request & response

---

## 🏗️ Project Structure

AI-Voice-Detection/
├── app/
│ ├── main.py # FastAPI entry point
│ ├── auth.py # API key validation
│ ├── config.py # Constants & allowed languages
│ ├── audio_utils.py # Base64 → audio loader
│ ├── features.py # Feature extraction
│ ├── model.py # ML model loader & prediction
│ └── explain.py # Explanation generator
│
├── model/
│ └── voice_detector.pkl # Trained ML model
│
├── training/
│ ├── train_model.py # Training script
│ └── dataset_info.md
│
├── requirements.txt
├── render.yaml
└── README.md


---

## 🔐 API Authentication

All API requests require an **API Key** sent in request headers.


Requests without a valid API key are **rejected**.

---

## 📥 API Endpoint

### **POST** `/api/voice-detection`

---

### 🔹 Request Headers


---

### 🔹 Request Body

```json
{
  "language": "English",
  "audioFormat": "mp3",
  "audioBase64": "BASE64_ENCODED_MP3_AUDIO"
}
```
### Response Example
{
  "status": "success",
  "language": "English",
  "classification": "HUMAN",
  "confidenceScore": 0.97,
  "explanation": "Natural vocal variations and human-like speech patterns detected"
}
---

### 🧠 Classification Labels
Label	Description
HUMAN	Voice spoken by a real human
AI_GENERATED	Voice generated using AI or synthetic systems

---
---

## 🙌 About the Developer

This project was **designed and developed by**:

### **👨‍💻 Himanshu Singh**  
**B.Tech Student | AI & Backend Development Enthusiast**

- Passionate about **Artificial Intelligence**, **Machine Learning**, and **Backend APIs**
- Interested in solving **real-world problems** using technology
- Actively participating in **hackathons** and technical competitions

---

## ⭐ Support This Project

If you found this project **useful, interesting, or inspiring**:

👉 **Please give this repository a ⭐ star on GitHub!**

Your support motivates me to:
- Build more impactful projects  
- Improve this system further  
- Share open-source work with the community  

---

## 🤝 Contributions

Contributions, suggestions, and improvements are **welcome**!

- Fork the repository
- Create a new branch
- Submit a pull request

---

## 📬 Contact

For queries, collaboration, or feedback:

- **GitHub:** https://github.com/Himanshu993527

---

### 🙏 Thank you for checking out this project!


