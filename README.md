# AI-Based-Accident-Risk-Predictor-using-Driving-Patterns
The AI-Based Accident Risk Predictor uses sensor data (GPS + accelerometer) to predict accident risks in real-time. It includes a mobile app for data collection and visualization, a backend for processing, and a deep learning model for predictions.

## Key Components
1. **Data Processing**: Sensor data fusion and feature extraction.
2. **Deep Learning Model**: LSTM-based model for time-series analysis.
3. **Mobile App**: Flutter app for user interaction and monitoring.
4. **Backend**: Flask-based API for predictions and alert notifications.

## Workflow
1. Mobile app collects GPS and accelerometer data.
2. Data is preprocessed and sent to the backend.
3. Backend extracts features and uses the model for prediction.
4. If risk is high, alerts are sent to emergency contacts.
