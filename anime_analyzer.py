import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. Load Dataset
# ==========================================

df = pd.read_csv("anime-dataset-2023.csv")

print("First 5 rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)


# ==========================================
# 2. Check Original Data
# ==========================================

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nSummary Statistics:")
print(df.describe())


# ==========================================
# 3. Explore Important Columns
# ==========================================

columns_to_check = [
    "Name",
    "Genres",
    "Studios",
    "Score",
    "Episodes",
    "Popularity"
]

for column in columns_to_check:
    print(f"\n{column}:")
    print(df[column].head(10))


# ==========================================
# 4. Create Cleaned Dataset
# ==========================================

df_cleaned = df.copy()

# Replace Unknown values with NaN
df_cleaned = df_cleaned.replace(
    ["Unknown", "UNKNOWN"],
    np.nan
)

# Remove duplicate rows
df_cleaned = df_cleaned.drop_duplicates()


# ==========================================
# 5. Convert Numerical Columns
# ==========================================

numeric_columns = [
    "Score",
    "Episodes",
    "Rank",
    "Scored By"
]

for column in numeric_columns:
    df_cleaned[column] = pd.to_numeric(
        df_cleaned[column],
        errors="coerce"
    )


# ==========================================
# 6. Check Cleaned Data
# ==========================================

print("\nMissing Values After Cleaning:")
print(df_cleaned.isnull().sum())

print("\nDuplicate Rows After Cleaning:")
print(df_cleaned.duplicated().sum())

print("\nOriginal Shape:")
print(df.shape)

print("\nCleaned Shape:")
print(df_cleaned.shape)

print("\nData Types After Cleaning:")
print(df_cleaned.dtypes)


# ==========================================
# 7. Top 10 Highest-Rated Anime
# ==========================================

top_anime = df_cleaned.sort_values(
    by="Score",
    ascending=False
)

print("\nTop 10 Highest-Rated Anime:")
print(
    top_anime[["Name", "Score"]].head(10)
)

popularity_anime = df_cleaned.sort_values(
    by="Popularity",
    ascending=False
)

print("\nTop 10 Most Popular Anime:")
print(
    popularity_anime[["Name", "Popularity"]].head(10)
)

Genres_anime = df_cleaned.sort_values(
    by = "Genres",
    ascending = False
)

print(Genres_anime[["Name", "Genres"]].head(10))

Episodes_anime = df_cleaned.sort_values(
    by = "Episodes",
    ascending = True
)

print(Episodes_anime[["Name", "Episodes"]].head(10))

genres = df_cleaned["Genres"].dropna()

print("\nGenres:")
print(genres.head(10))

genre_list = genres.str.split(", ")

genere_exploded = genre_list.explode()

genere_counts = genere_exploded.value_counts()

print("\nExploded Genres:")

type_counts = df_cleaned["Type"].value_counts()

print("\nAnime Types:")
print(type_counts)

plt.figure(figsize=(10, 6))

sns.barplot(
    x=type_counts.index,
    y=type_counts.values
)
plt.xlabel("Anime Type")
plt.ylabel("Count")
plt.title("Distribution of Anime Types")
plt.show()

most_sudios= df_cleaned["Studios"].value_counts().head(10)

print("\nTop 10 Most Popular Studios:")
print(most_sudios)

plt.figure(figsize=(10,6))
sns.barplot(
   x= most_sudios.index,
   y= most_sudios.values
)
plt.xlabel("Anime Studios")
plt.ylabel("Count")
plt.title("Distribution of Anime Studios")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

top_genres = genere_counts.head(10)
print(top_genres)

top_studios = df_cleaned["Studios"].value_counts().head(10)
print(top_studios)

plt.figure(figsize=(10, 6))

sns.histplot(
    df_cleaned["Score"].dropna(),
    bins=20
)

plt.title("Distribution of Anime Scores")
plt.xlabel("Score")
plt.ylabel("Number of Anime")

plt.tight_layout()
plt.show()