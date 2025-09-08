import sqlite3
import os
import joblib
import pandas as pd
import database_utils
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Tränar, utvärderar och sparar modellen som kan klassificera heltal som udda eller jämna.

MODEL_DIR = "model_registry"
os.makedirs(MODEL_DIR, exist_ok=True)

def train_and_save_model(version):
    """
    Tränar modell och tar fram dess träffsäkerhet. Sparar sedan modellen i model registry.7
    Tar emot modellens versionsnummer.
    Returnerar accuracyscore.
    """
    df = pd.read_sql("SELECT * FROM training_data", database_utils.conn)
    X = df[["number"]]
    y = df["label"]

    X_train, X_test, y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LogisticRegression()
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    acc = accuracy_score(X_test, preds)

    model_path = os.path.join(MODEL_DIR, f"model_v{version}.pkl")
    joblib.dump(model, model_path)

    print(f"Tränad och sparad modell v{version} med accuracy {acc:.2f}")
    return acc    