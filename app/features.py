import numpy as np
import librosa

def extract_features(y, sr):
    features = []

    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    features.extend(np.mean(mfcc, axis=1))

    zcr = librosa.feature.zero_crossing_rate(y)
    features.append(np.mean(zcr))

    spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
    features.append(np.mean(spectral_centroid))

    rms = librosa.feature.rms(y=y)
    features.append(np.mean(rms))

    return np.array(features).reshape(1, -1)
