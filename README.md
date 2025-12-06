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

----------

# **Task 2 — Basic ML Model**

### **Model Used**

-   **Model:**  Logistic Regression (with StandardScaler + Pipeline)
    
-   **Features Used:**
    
    -   `danceability`
        
    -   `energy`
        
    -   `tempo`
        
    -   `loudness`
        
    -   `duration_ms`
        
-   **Target Variable:**
    
    -   `is_popular`  → 1 if popularity > 70, else 0
        

----------

### **Why This Model?**

#### **Logistic Regression**

-   Baseline model for binary classification.
    
-   Fast to train and easy to interpret.
    
-   Produces probability outputs for popularity prediction.
    
-   Works well with standardized numeric features (handled via  `StandardScaler`  in the pipeline).
    

_(Decision Tree was not used, but is often a common baseline alternative.)_

----------

### **Evaluation Setup**

-   **Train/Test Split:**  80% train, 20% test
    
-   **Stratification:**  Ensures the proportion of popular vs. non-popular songs remains consistent.
    
-   **Metrics Evaluated:**
    
    -   Accuracy
        
    -   F1-score
        
    -   Precision & Recall via classification report
        

----------

### **Results (Actual Output)**

Metric

Value

**Accuracy**

**0.9575**

**F1-score**

**0.0000**

#### **Classification Report Summary**

Class

Precision

Recall

F1-score

Support

**0 (not popular)**

0.96

1.00

0.98

21,831

**1 (popular)**

0.00

0.00

0.00

969

**Overall Accuracy**

**95.75%**

22,800

----------

### **Why Is Accuracy High But F1-score = 0?**

This happens because of  **severe class imbalance**:

-   Class  **0 (not popular)**  →  **21,831 samples**
    
-   Class  **1 (popular)**  →  **only 969 samples**
    

The model learned to  **predict nearly everything as class 0**, because class 0 dominates the dataset.

So:

-   Accuracy becomes high (because most data is class 0).
    
-   F1-score for class 1 becomes  **0**, since the model predicts  **zero popular songs correctly**.
    

This is a classic imbalance problem in classification.

----------

### **Strengths**

-   Captures basic linear relationships between audio features and popularity.
    
-   Very high accuracy on the majority class.
    
-   Simple baseline pipeline to extend with more models.
    
-   Code structure is clean, modular, and easy to build upon.
    

----------

### **Limitations**

-   **Strong class imbalance**: Popular songs are <5% of dataset → model fails to learn minority class.
    
-   **F1-score = 0**  indicates the model is  _not_  actually detecting popularity.
    
-   **No resampling applied**  (SMOTE/oversampling/undersampling).
    
-   **Limited features**  — real-world popularity depends on:
    
    -   Artist popularity
        
    -   Playlist placement
        
    -   Release year
        
    -   Marketing, virality, social media trends
        
-   **No hyperparameter tuning**  was performed.

----------

----------

# **Task 3 — SQL Database & Analytical Queries**

## **Overview**

This task involves designing a relational database for an e-commerce scenario and writing SQL queries to analyze user behaviour, product performance, and revenue patterns. The task demonstrates understanding of  **schema creation, JOINs, aggregations, subqueries, and window functions**.

----------

## **Database Schema**

Three relational tables were created with proper primary keys and foreign key constraints:

### **1.  `users`**

Stores customer details.

-   `user_id`  (PK)
    
-   `user_name`
    
-   `email`
    
-   `country`
    
-   `created_at`
    

### **2.  `products`**

Stores product catalog information.

-   `product_id`  (PK)
    
-   `product_name`
    
-   `category`
    
-   `price`
    

### **3.  `transactions`**

Stores purchase activity.

-   `transaction_id`  (PK)
    
-   `user_id`  (FK → users.user_id)
    
-   `product_id`  (FK → products.product_id)
    
-   `quantity`
    
-   `transaction_date`
    
-   `payment_method`
    
-   `status`
    

----------

## **Objectives of the Task**

-   Create normalized tables with proper constraints.
    
-   Write SQL queries to analyze transactions, revenue, and customer spending.
    
-   Demonstrate use of  **JOINs**,  **GROUP BY**,  **aggregations**,  **subqueries**, and  **window functions**.
    

----------

## **Queries Implemented**

### **Q1 — Basic JOIN**

Return transaction details along with user name and country.

### **Q2 — Transaction Amount Calculation**

Combine users, products, and transactions and compute  
`total_amount = quantity × price`.

### **Q3 — Country-wise Revenue**

SUM of revenue grouped by user country.

### **Q4 — High-Value Users**

Find users who spent  **more than 1000**  using a subquery.

### **Q5 — Ranking Transactions**

Use  `ROW_NUMBER()`  window function to rank each user’s transactions by date (latest first).

### **Q6 — Filtered Transactions**

Retrieve only  **successful Credit Card transactions**  after  `2024-01-01`.

### **Q7 — Top 3 Best-Selling Products**

Order products by total revenue and return top 3.

### **Q8 — Average Order Value (AOV) per User**

Compute average revenue per transaction for each user.

----------

## **Skills Demonstrated**

 SQL table creation  
Primary key & foreign key relationships  
JOINs (INNER JOIN)  
Aggregations (SUM, AVG)  
GROUP BY & HAVING  
Filtering with WHERE  
Subqueries  
Window functions (ROW_NUMBER)  
Revenue calculations

----------

## **Summary**

Task 3 successfully models an e-commerce database and performs analytical SQL queries that are commonly required in real-world data engineering and BI analyst roles. The task highlights clean schema design, relational integrity, and strong SQL querying capability.