import os
import librosa
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

DATA_DIR = "data"

print("🔍 Starting training script...")
print("📂 Looking for data directory:", DATA_DIR)

def extract_features(file_path):
    y, sr = librosa.load(file_path, sr=None)

    features = []

    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    features.extend(np.mean(mfcc, axis=1))

    zcr = librosa.feature.zero_crossing_rate(y)
    features.append(np.mean(zcr))

    centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
    features.append(np.mean(centroid))

    rms = librosa.feature.rms(y=y)
    features.append(np.mean(rms))

    return features

X = []
y = []

for label, class_name in enumerate(["human", "ai"]):
    class_dir = os.path.join(DATA_DIR, class_name)
    print(f"➡️ Checking folder: {class_dir}")

    if not os.path.exists(class_dir):
        print(f"❌ Folder not found: {class_dir}")
        continue

    for lang in os.listdir(class_dir):
        lang_dir = os.path.join(class_dir, lang)
        print(f"   🔹 Language folder: {lang_dir}")

        for file in os.listdir(lang_dir):
            if file.endswith(".mp3"):
                file_path = os.path.join(lang_dir, file)
                print(f"      🎵 Processing file: {file_path}")

                try:
                    features = extract_features(file_path)
                    X.append(features)
                    y.append(label)
                except Exception as e:
                    print(f"      ❌ Error processing {file}: {e}")

print("📊 Total samples collected:", len(X))

if len(X) == 0:
    print("❌ NO AUDIO FILES FOUND. TRAINING CANNOT CONTINUE.")
    exit()

X = np.array(X)
y = np.array(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("🧠 Training RandomForest model...")

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print(f"✅ Model accuracy: {acc:.2f}")

joblib.dump(model, "model/voice_detector.pkl")
print("💾 Model saved to model/voice_detector.pkl")
