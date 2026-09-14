# Anime Data Analyzer 🎌

## 📌 Project Overview

Anime Data Analyzer is a Python-based data analysis project that explores an anime dataset containing information about anime ratings, genres, studios, popularity, episodes, anime types, and other details.

The main goal of this project is to clean the dataset, analyze important information, and create visualizations to understand different patterns in anime data.

## 🎯 Objectives

* Analyze anime ratings
* Find the highest-rated anime
* Find the most popular anime
* Analyze the most common genres
* Analyze different anime types
* Find studios with the most anime
* Understand the distribution of anime scores
* Practice real-world data cleaning and visualization

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

## 📊 Dataset

The project uses the **Anime Dataset 2023**, which contains information about anime titles, ratings, genres, studios, popularity, episodes, and other attributes.

## 🧹 Data Cleaning

The following data-cleaning steps were performed:

* Checked the dataset shape and columns
* Checked missing values
* Checked duplicate rows
* Replaced `Unknown` and `UNKNOWN` values with `NaN`
* Removed duplicate rows
* Converted numerical columns into appropriate data types
* Handled invalid numerical values using `errors="coerce"`

## 🔍 Analysis Performed

### 1. Top 10 Highest-Rated Anime

Analyzed the anime with the highest scores.

### 2. Top 10 Most Popular Anime

Analyzed anime popularity using the `Popularity` ranking.

> Lower popularity rank means higher popularity.

### 3. Genre Analysis

Analyzed the most common anime genres using:

* `split()`
* `explode()`
* `value_counts()`

### 4. Anime Type Analysis

Compared different anime types such as:

* TV
* Movie
* OVA
* ONA
* Special
* Music

### 5. Studio Analysis

Analyzed the studios that have produced the highest number of anime entries.

### 6. Score Distribution

Created a histogram to understand how anime scores are distributed across the dataset.

## 💡 Key Insights

* Identified the highest-rated anime in the dataset.
* Identified the most popular anime using popularity rankings.
* Found the most common anime genres.
* Compared different anime types.
* Identified studios with the highest number of anime entries.
* Studied the distribution of anime scores.

## 📈 Visualizations

### Top Genres

![Top Genres](images/top_genres.png)

### Anime Types

![Anime Types](images/anime_types.png)

### Top Studios

![Top Studios](images/top_studios.png)

### Score Distribution

![Score Distribution](images/score_distribution.png)

## 🚀 How to Run the Project

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### Step 2: Open the project folder

```bash
cd anime-data-analyzer
```

### Step 3: Install required libraries

```bash
pip install pandas numpy matplotlib seaborn
```

### Step 4: Make sure the dataset is in the project folder

The file should be:

```text
anime-dataset-2023.csv
```

### Step 5: Run the Python program

```bash
python anime_analyzer.py
```

## 📁 Project Structure

```text
Anime-Data-Analyzer/
│
├── anime_analyzer.py
├── anime-dataset-2023.csv
├── README.md
│
└── images/
    ├── top_genres.png
    ├── anime_types.png
    ├── top_studios.png
    └── score_distribution.png
```

## 🎓 What I Learned

Through this project, I practiced:

* Python programming
* Pandas data manipulation
* NumPy
* Data cleaning
* Handling missing values
* Removing duplicates
* Data type conversion
* Sorting data
* `value_counts()`
* `split()`
* `explode()`
* Exploratory Data Analysis (EDA)
* Data visualization
* Matplotlib
* Seaborn

## 👨‍💻 Author

**BB.Abhishek**

---

⭐ If you find this project useful, feel free to explore the repository.
