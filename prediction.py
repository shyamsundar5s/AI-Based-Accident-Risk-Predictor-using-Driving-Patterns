import numpy as np
from tensorflow.keras.models import load_model
from data_processing.feature_extraction import extract_features

# Load pre-trained model
model = load_model('model/saved_models/model_v1.h5')

def predict_risk(data):
    """
    Predict accident risk based on driving data.
    :param data: Fused driving data
    :return: Risk prediction (0-1)
    """
    features = extract_features(data)
    features_array = np.array(list(features.values())).reshape(1, -1)  # Reshape for input
    risk = model.predict(features_array)[0][0]
    return {"risk": risk}
