import numpy as np
import pandas as pd
import os

RAW_DATA_PATH = os.path.join("data/raw/Spotify_songs.csv" )
PROCESSED_DATA_PATH = os.path.join("data/processed/Spotify_songs_cleaned.csv")

def load_data(path:str)->pd.DataFrame:
    df = pd.read_csv(path)
    return df

def explore_data(df: pd.DataFrame)->None:
    print(df.head(10))
    print(df.info())
    print(df.describe())

def clean_data(df:pd.DataFrame)->pd.DataFrame:
    df=df.copy()
    df.columns = [col.strip().lower().replace(" ","_") for col in df.columns]

    df = df.drop_duplicates()

    numeric_cols = df.select_dtypes(include = ['int64' , 'float64']).columns 

    categorical_cols = df.select_dtypes(include=['object']).columns

    for col in numeric_cols:
        median_value = df[col].median()
        df[col] = df[col].fillna(median_value)
    
    for col in categorical_cols:
        mode_value= df[col].mode()[0]
        df[col] = df[col].fillna(mode_value)

    if "duration_ms" in df.columns:
        df = df[df["duration_ms"] > 0]
    
    df["is_popular"] = (df["popularity"] > 70).astype(int)


    return df

   


def save_data(df:pd.DataFrame , path:str)->None:
    df.to_csv(path , index=False)


def run_pipeline():
    df_raw = load_data(RAW_DATA_PATH)
    df_clean = clean_data(df_raw)
    save_data(df_clean, PROCESSED_DATA_PATH)
    print("Saved cleaned data to: " ,  PROCESSED_DATA_PATH)

if __name__ == "__main__":
    run_pipeline()


