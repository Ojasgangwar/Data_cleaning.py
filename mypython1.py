import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/cleaned_titanic.csv")

print("Dataset Shape:", df.shape)


print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nSurvival Count:")
print(df["survived"].value_counts())

print("\nSurvival Percentage:")
print(df["survived"].value_counts(normalize=True) * 100)

print("\nSurvival by Gender:")
print(pd.crosstab(df["sex"], df["survived"]))

print("\nSurvival Rate by Gender:")
print(df.groupby("sex")["survived"].mean() * 100)


print("\nSurvival by Class:")
print(pd.crosstab(df["class"], df["survived"]))

print("\nSurvival Rate by Class:")
print(df.groupby("class")["survived"].mean() * 100)


print("\nAge Statistics:")
print("Average age:", df["age"].mean())
print("Minimum age:", df["age"].min())
print("Maximum age:", df["age"].max())


print("\nFare Statistics:")
print("Average fare:", df["fare"].mean())
print("Minimum fare:", df["fare"].min())
print("Maximum fare:", df["fare"].max())


print("\nSurvival by Embarkation Port:")
print(df.groupby("embarked")["survived"].mean() * 100)


plt.figure(figsize=(6, 4))

df["survived"].value_counts().sort_index().plot(
    kind="bar"
)

plt.title("Titanic Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Number of Passengers")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

survival_gender = pd.crosstab(
    df["sex"],
    df["survived"]
)

survival_gender.plot(
    kind="bar",
    figsize=(7, 4)
)

plt.title("Survival by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Passengers")
plt.xticks(rotation=0)
plt.legend(["Not Survived", "Survived"])
plt.tight_layout()
plt.show()


survival_class = pd.crosstab(
    df["class"],
    df["survived"]
)

survival_class.plot(
    kind="bar",
    figsize=(7, 4)
)

plt.title("Survival by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")
plt.xticks(rotation=0)
plt.legend(["Not Survived", "Survived"])
plt.tight_layout()
plt.show()


plt.figure(figsize=(7, 4))

df["age"].plot(
    kind="hist",
    bins=10
)

plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 4))

df["fare"].plot(
    kind="hist",
    bins=10
)

plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.show()


print("\n========== KEY INSIGHTS ==========")

overall_survival = df["survived"].mean() * 100
female_survival = df[df["sex"] == "female"]["survived"].mean() * 100
male_survival = df[df["sex"] == "male"]["survived"].mean() * 100

print(f"1. Overall survival rate was approximately {overall_survival:.2f}%.")

print(
    f"2. Female passengers had a survival rate of "
    f"{female_survival:.2f}%, compared with "
    f"{male_survival:.2f}% for male passengers."
)

class_survival = df.groupby("class")["survived"].mean() * 100

for passenger_class, rate in class_survival.items():
    print(
        f"3. Passengers in {passenger_class} class "
        f"had a survival rate of {rate:.2f}%."
    )

print(
    f"4. The average passenger age was "
    f"{df['age'].mean():.2f} years."
)

print(
    f"5. The average ticket fare was "
    f"{df['fare'].mean():.2f}."
)

print(
    "6. The age distribution shows that the dataset "
    "contains passengers across different age groups."
)

print(
    "7. Fare values vary considerably, indicating differences "
    "in ticket pricing among passengers."
)

print("\nEDA completed successfully!")