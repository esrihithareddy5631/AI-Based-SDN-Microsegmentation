import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

# Load dataset
df = pd.read_csv("data/sdn_dataset.csv")

# Encode categorical columns
le_source = LabelEncoder()
le_destination = LabelEncoder()
le_protocol = LabelEncoder()
le_label = LabelEncoder()

df["Source"] = le_source.fit_transform(df["Source"])
df["Destination"] = le_destination.fit_transform(df["Destination"])
df["Protocol"] = le_protocol.fit_transform(df["Protocol"])
df["Label"] = le_label.fit_transform(df["Label"])

# Features
X = df[["Source","Destination","Protocol","Packets","Bytes","Duration"]]

# Target
y = df["Label"]

# Split dataset
X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Random Forest
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train,y_train)

# Predictions
y_pred = model.predict(X_test)

print("\nAccuracy:")
print(accuracy_score(y_test,y_pred))

print("\nClassification Report:")
print(classification_report(y_test,y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test,y_pred))

# Save model
joblib.dump(model,"models/ai_model.pkl")

print("\nModel saved successfully!")
