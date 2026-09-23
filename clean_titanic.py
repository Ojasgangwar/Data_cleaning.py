import pandas as pd
import os

df = pd.read_csv("data/raw_titanic.csv")

print("Original shape:", df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_", regex=False)
)

for column in ["age", "fare"]:
    if column in df.columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

if "age" in df.columns:
    df.loc[df["age"] < 0, "age"] = pd.NA

if "fare" in df.columns:
    df.loc[df["fare"] < 0, "fare"] = pd.NA

for column in ["sex", "embarked", "class"]:
    if column in df.columns:
        df[column] = df[column].astype("string").str.strip().str.lower()

if "age" in df.columns:
    df["age"] = df["age"].fillna(df["age"].median())

if "fare" in df.columns:
    df["fare"] = df["fare"].fillna(df["fare"].median())

for column in ["embarked", "sex", "class"]:
    if column in df.columns and df[column].notna().any():
        df[column] = df[column].fillna(df[column].mode()[0])

os.makedirs("data", exist_ok=True)
df.to_csv("data/cleaned_titanic.csv", index=False)

print("\nCleaned shape:", df.shape)
print("\nRemaining missing values:")
print(df.isnull().sum())
print("\nCleaning completed successfully!")
