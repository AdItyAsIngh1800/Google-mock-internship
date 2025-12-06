# **Google Mock Internship Task — Data Pipeline & ML**

## **Task 1 — Data Pipeline & Analysis**

### **Problem Statement**

I analysed a Spotify songs dataset to explore patterns in musical attributes such as tempo, danceability, energy, and genre distribution. The objective was to design a reproducible end-to-end data pipeline that loads raw data, cleans and preprocesses the dataset, and produces meaningful insights. The pipeline also generates basic visualizations to highlight trends in genres and audio features.

----------

## **Dataset**

-   **Name:**  Spotify Songs Dataset
    
-   **Source:**  Public dataset 
    
-   **Size:**  ~114000 rows
    
-   **Key Columns:**
    
    -   `track_name`,  `track_genre`,  `duration_ms`
        
    -   `tempo`,  `danceability`,  `energy`
        
    -   `artist_name`, etc.
        

----------

## **Steps Taken**

### **1. Loaded Raw Dataset**

-   Loaded the CSV file from  `data/raw/Spotify_songs.csv`.
    

### **2. Cleaned the Dataset**

Cleaning performed inside  `clean_data()`:

-   Standardized column names to  **lowercase + snake_case**.
    
-   Removed duplicate rows.
    
-   Handled missing values:
    
    -   **Median**  for numerical columns
        
    -   **Mode**  for categorical columns
        
-   Removed invalid entries where  `duration_ms <= 0`.
    

### **3. Saved Cleaned Dataset**

-   Stored the cleaned file at:  
    `data/processed/Spotify_songs_cleaned.csv`
    

### **4. Ran Exploratory Data Analysis (EDA)**

Performed in the insights script:

-   Calculated statistical summaries.
    
-   Checked distributions (danceability histogram).
    
-   Identified correlations (danceability ↔ energy).
    
-   Grouped data by genre for deeper insights.
    

### **5. Generated Visualizations (matplotlib only)**

Created and saved plots inside the  `/reports/`  folder:

-   `top_genres.png`  → Bar chart of top 5 genres
    
-   `danceability_hist.png`  → Histogram of danceability distribution
    

----------

## **Tools Used**

-   **Python**
    
-   **pandas**,  **numpy**
    
-   **matplotlib**  (no seaborn)
    
-   **os**  for path handling
    
-   **scikit-learn**  (used later for Task 2 but imported in project)
    
-   **Git & GitHub**  for version control
    

----------

## **Key Findings (Insights)**

Based on the executed analysis:

-   **Average song tempo**  is approximately  **122.15 bpm**  (derived from dataset).
    
-   **Top 5 genres**  appear most frequently in the dataset, led by genres such as acoustic , afrobeat  , psych-rock , progressive-house , power-pop      
    
-   **Danceability and energy show a positive correlation**  (~0.134), meaning more energetic songs tend to be more danceable.
    
-   **Genres vary widely by duration**  — the longest average durations are found in the top 5 genres listed.
-- detroit-techno    372012.402
-- minimal-techno    368863.246
-- chicago-house     366853.868
--breakbeat         321762.218
-- iranian           319709.537
    
    
-   Cleaned data shows  **no invalid duration entries**  and  **no missing values**, ensuring consistency for ML tasks.