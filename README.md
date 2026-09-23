# Titanic Dataset Cleaning using Python & Pandas

A simple data-cleaning project that demonstrates how to clean and preprocess a Titanic dataset using **Python** and **Pandas**.

The project handles missing values, duplicate records, inconsistent categorical values, incorrect data types, and impossible numerical values before creating a cleaned dataset.

## 📌 Project Overview

Real-world datasets often contain missing values, duplicate records, inconsistent formatting, and invalid data.

This project demonstrates a basic data-cleaning workflow using the Titanic dataset.

### Key Operations

* Load a raw CSV dataset
* Check missing values
* Detect and remove duplicate records
* Clean column names
* Convert numerical columns to appropriate data types
* Handle missing numerical values
* Handle missing categorical values
* Standardize categorical values
* Remove impossible values such as negative age and fare
* Export the cleaned dataset as a CSV file

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **CSV**
* **Git & GitHub**

## 📂 Project Structure

```text
titanic-data-cleaning/
│
├── data/
│   ├── raw_titanic.csv
│   └── cleaned_titanic.csv
│
├── mypython.py
│
└── README.md
```

## 📊 Dataset

The project uses a Titanic passenger dataset containing information such as:

* Passenger ID
* Survival status
* Passenger class
* Name
* Gender
* Age
* Number of siblings/spouses
* Number of parents/children
* Ticket
* Fare
* Cabin
* Port of embarkation

The raw dataset is stored in:

```text
data/raw_titanic.csv
```

The cleaned dataset is generated as:

```text
data/cleaned_titanic.csv
```

## 🔄 Data Cleaning Process

### 1. Load Dataset

```python
df = pd.read_csv("data/raw_titanic.csv")
```

### 2. Check Missing Values

```python
df.isnull().sum()
```

### 3. Remove Duplicate Records

```python
df = df.drop_duplicates()
```

### 4. Clean Column Names

Column names are converted to lowercase and spaces are replaced with underscores.

For example:

```text
Passenger ID → passenger_id
```

### 5. Handle Numerical Values

The `age` and `fare` columns are converted to numeric data types.

Missing values are replaced using the median.

```python
df["age"] = df["age"].fillna(df["age"].median())
df["fare"] = df["fare"].fillna(df["fare"].median())
```

### 6. Handle Categorical Values

Missing categorical values are filled using the mode.

Columns such as:

```text
sex
embarked
class
```

are also standardized to lowercase.

For example:

```text
Male → male
Female → female
First → first
```

### 7. Remove Impossible Values

Invalid negative values are identified and replaced with missing values before imputation.

```python
df.loc[df["age"] < 0, "age"] = pd.NA
df.loc[df["fare"] < 0, "fare"] = pd.NA
```

### 8. Export Cleaned Dataset

```python
df.to_csv("data/cleaned_titanic.csv", index=False)
```

## ▶️ How to Run

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/titanic-data-cleaning.git
```

### Step 2: Open the Project

```bash
cd titanic-data-cleaning
```

### Step 3: Install Pandas

```bash
pip install pandas
```

If you are using a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Then:

```bash
pip install pandas
```

### Step 4: Run the Program

```bash
python mypython.py
```

## 💻 Expected Output

The program displays:

```text
Original shape: (...)

Missing values:
...

Duplicate rows: ...

Cleaned shape: (...)

Remaining missing values:
...

Cleaning completed successfully!
```

The cleaned dataset will be created automatically inside the `data` folder.

## 🎯 Learning Objectives

This project helps demonstrate:

* Basic Pandas operations
* Data preprocessing
* Missing-value handling
* Duplicate detection
* Data type conversion
* Categorical data standardization
* Data validation
* CSV file handling
* Basic data-cleaning workflow

## 🚀 Future Improvements

Possible improvements include:

* Exploratory Data Analysis (EDA)
* Data visualization using Matplotlib and Seaborn
* Outlier detection
* Feature engineering
* Encoding categorical variables
* Building a machine-learning model to predict Titanic survival

## 👨‍💻 Author

**Ojas Gangwar**

B.Tech Computer Science / Information Technology Student

### Skills

Python • Java • SQL • Pandas • Data Analytics • Data Science • Git & GitHub

---

⭐ If you found this project useful, consider giving the repository a
