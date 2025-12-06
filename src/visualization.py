import matplotlib.pyplot as plt
import os
from spotify_analysis import load_clean_data

os.makedirs("reports", exist_ok=True)

def plot_top_genres(df):
    if 'track_genre' not in df.columns:
        return
    
    top_genres = df['track_genre'].value_counts().head(5)

    plt.figure()
    plt.bar(top_genres.index,top_genres.values)
    plt.xlabel('Genre')
    plt.ylabel('No of songs')
    plt.title('Top 5 genres')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('reports/top_genres.png')
    plt.close()

def plot_danceability_hist(df):
    if "danceability" not in df.columns:
        return
    
    plt.figure()
    plt.hist(df["danceability"], bins=20)
    plt.xlabel("Danceability")
    plt.ylabel("Frequency")
    plt.title("Distribution of Danceability")
    plt.tight_layout()
    plt.savefig("reports/danceability_hist.png")
    plt.close()


def run_plots():
    df = load_clean_data()
    plot_top_genres(df)
    plot_danceability_hist(df)

if __name__ == '__main__':
    run_plots()