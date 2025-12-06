import pandas as pd 
import numpy as np
import os 

PROCESSED_DATA_PATH = os.path.join("/Users/adityasingh/Google-mock-internship/data/processed/Spotify_songs_cleaned.csv")

def load_clean_data():
    return pd.read_csv(PROCESSED_DATA_PATH)

def insight_average_tempo(df):
    avg_tempo= df['tempo'].mean()
    print(f'1. average tempo of songs : {avg_tempo:.2f}')

def insight_top_genres(df):
    top_genres=df['track_genre'].value_counts().head(5)
    print(f'2. top 5 genres :')
    print(top_genres)

def insight_danceability_energy_corr(df):
    corr = df['danceability'].corr(df['energy'])
    print(f'3. the correlation between danceablitity and energy : {corr:.3f}')

def insight_avg_duration_by_genre(df):
    result = df.groupby('track_genre')['duration_ms'].mean().sort_values(ascending=False).head(5)
    print('4. genres with highest average song duration(top 5): ')
    print(result)




def run_insights():
    df = load_clean_data()
    print(df.columns)
    insight_average_tempo(df)
    insight_top_genres(df)
    insight_danceability_energy_corr(df)
    insight_avg_duration_by_genre(df)

    
if __name__ == '__main__':
    run_insights()

