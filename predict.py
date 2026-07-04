import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/ai_model.pkl")

# Example traffic
traffic = pd.DataFrame([{
    "Source": 0,
    "Destination": 2,
    "Protocol": 1,
    "Packets": 300,
    "Bytes": 42000,
    "Duration": 9
}])

prediction = model.predict(traffic)

if prediction[0] == 0:
    print("Prediction : ATTACK")
else:
    print("Prediction : NORMAL")
