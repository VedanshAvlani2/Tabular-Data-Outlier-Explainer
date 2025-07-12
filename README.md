# Tabular Data Outlier Explainer

## 📌 Overview
This project identifies and visualizes statistical outliers in structured tabular data using Z-score logic. It generates clear terminal outputs and boxplots for numeric columns, helping analysts pinpoint anomalies with ease.

## 🎯 Objective
- Detect outliers in each numeric column using Z-score thresholding.
- Display a concise terminal summary and corresponding boxplots for visual interpretation.
- Avoid saving any files—outputs are rendered directly to the screen.

## 📁 Dataset
The project uses the classic [`insurance.csv`](https://www.kaggle.com/datasets/mirichoi0218/insurance) dataset containing:
- **Age, BMI, Charges, Children** (numeric)
- **Sex, Region, Smoker** (categorical)

## ⚙️ How to Run

### 1. Clone the Repository and Install Dependencies
```bash
pip install pandas numpy matplotlib seaborn
```

### 2. Run the Script
```bash
python Tabular Data Outlier Explainer.py
```

### 🖼 Sample Output
The script will print a list of columns with the number of outliers and show corresponding boxplots (only for those with detected anomalies).

## 📊 Methodology
- **Z-score** calculation for each numeric column
- Threshold > 3 or < -3 to classify as outlier
- **Boxplots** rendered inline using `matplotlib` and `seaborn`

## 🧠 Key Insights
- Boxplots give immediate visual confirmation of distribution shape and outliers.
- Helpful for feature engineering, anomaly detection, and data cleaning pipelines.

## 🔮 Future Enhancements
- Add support for IQR-based detection
- Export flagged rows to CSV if needed
- Streamlit dashboard version for interactivity
