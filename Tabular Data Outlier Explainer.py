import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------------
# 1. Load Dataset
# -------------------------------
df = pd.read_csv("insurance.csv")

# -------------------------------
# 2. Detect Outliers Function
# -------------------------------
def detect_outliers(df, col, threshold=3):
    mean = df[col].mean()
    std = df[col].std()
    z_scores = (df[col] - mean) / std
    return df[np.abs(z_scores) > threshold]

# -------------------------------
# 3. Outlier Detection & Display
# -------------------------------
numeric_cols = df.select_dtypes(include=[np.number]).columns

print("\n📊 Outlier Summary:\n")
for col in numeric_cols:
    outliers = detect_outliers(df, col)
    count = len(outliers)
    print(f"🔹 {col}: {count} outliers")

    if count > 0:
        print(f"📌 Displaying boxplot for '{col}'...\n")
        plt.figure(figsize=(8, 3))
        sns.boxplot(x=df[col], color="salmon")
        plt.title(f"Boxplot of {col} (outliers may be visible)")
        plt.xlabel(col)
        plt.tight_layout()
        plt.show()
