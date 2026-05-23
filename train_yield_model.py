import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

df=pd.read_csv(
"data/Crop_recommendation.csv"
)

X=df[

[
"N",
"P",
"K",
"temperature",
"humidity",
"ph",
"rainfall"
]

]

y=df["rainfall"]

model=RandomForestRegressor(
n_estimators=100,
random_state=42
)

model.fit(
X,
y
)

joblib.dump(
model,
"models/yield_model.pkl"
)

print(
"Yield model trained successfully"
)