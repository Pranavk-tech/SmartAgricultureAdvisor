import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Read dataset
df = pd.read_csv("data/Crop_recommendation.csv")

print("Dataset loaded successfully")


# Input columns
X = df.drop("label", axis=1)

# Output column
y = df["label"]


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# Train model
model.fit(
    X_train,
    y_train
)


# Test prediction
predictions = model.predict(
    X_test
)


# Calculate accuracy
accuracy = accuracy_score(
    y_test,
    predictions
)

print("Accuracy:", accuracy)


# Save model
joblib.dump(
    model,
    "models/crop_model.pkl"
)

print("Model saved successfully")