import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


PROCESSED_DATA_PATH = os.path.join("data", "processed", "spotify_songs_cleaned.csv")

def load_clean_data():
    return pd.read_csv(PROCESSED_DATA_PATH)

def prepare_features(df: pd.DataFrame):
    feature_cols = ["danceability", "energy", "tempo", "loudness", "duration_ms"]
    target_col = "is_popular"

    df_model = df.dropna(subset=feature_cols + [target_col])
    X = df_model[feature_cols]
    y = df_model[target_col]
    return X, y

def split_data(X, y, test_size=0.2, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    return X_train, X_test, y_train, y_test

def build_logistic_regression_model():
    model = Pipeline(steps=[
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(max_iter=1000))
    ])
    return model

def train_and_evaluate(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    print("Accuracy:", acc)
    print("F1-score:", f1)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    
    return acc, f1

def run_model():
    df = load_clean_data()
    X, y = prepare_features(df)
    X_train, X_test, y_train, y_test = split_data(X, y)
    
    model = build_logistic_regression_model()

    acc, f1 = train_and_evaluate(model, X_train, X_test, y_train, y_test)
    print(f"Final Accuracy: {acc:.4f}")
    print(f"Final F1-score: {f1:.4f}")

if __name__ == "__main__":
    run_model()

