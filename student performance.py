import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Raki\Downloads\student (1)\student-mat.csv", sep=";")

print("Dataset Loaded Successfully")

print("\nFirst 5 Rows:")
print(df.head())

print("\nShape of Dataset:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove Duplicates
df = df.drop_duplicates()

print("\nDataset Shape After Removing Duplicates:")
print(df.shape)

# --------------------------
# Analysis Questions
# --------------------------

# Average Final Grade
avg_grade = df['G3'].mean()
print("\nAverage Final Grade:", avg_grade)

# Students scoring above 15
above_15 = df[df['G3'] > 15].shape[0]
print("Students scoring above 15:", above_15)

# Correlation between studytime and G3
corr = df['studytime'].corr(df['G3'])
print("Correlation between Study Time and Grade:", corr)

# Gender Performance
gender_avg = df.groupby('sex')['G3'].mean()

print("\nAverage Grade by Gender:")
print(gender_avg)

# --------------------------
# Visualization 1
# Histogram
# --------------------------

plt.figure(figsize=(6,4))
plt.hist(df['G3'], bins=10, edgecolor='black')
plt.title("Distribution of Final Grades")
plt.xlabel("Grade")
plt.ylabel("Frequency")
plt.show()

# --------------------------
# Visualization 2
# Scatter Plot
# --------------------------

plt.figure(figsize=(6,4))
plt.scatter(df['studytime'], df['G3'])
plt.title("Study Time vs Final Grade")
plt.xlabel("Study Time")
plt.ylabel("Final Grade")
plt.show()

# --------------------------
# Visualization 3
# Bar Chart
# --------------------------

gender_avg.plot(kind='bar')

plt.title("Male vs Female Average Score")
plt.xlabel("Gender")
plt.ylabel("Average Grade")
plt.show()
