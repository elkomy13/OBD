# Vehicle Telemetry Data Analysis and Classification

## Project Overview
This repository hosts a comprehensive analysis and classification model designed for vehicle telemetry data. The primary objective is to process and analyze telemetry data collected from 19 drivers operating a single vehicle on a specific route. By employing various machine learning techniques, this project aims to extract meaningful insights and predict potential vehicle performance issues based on telemetry parameters.

## Key Features
- **Data Preprocessing**: Robust methods for data cleaning, handling missing values, encoding categorical variables, and normalizing numerical features.
- **Exploratory Data Analysis (EDA)**: Visualizations to understand feature distributions and relationships, aiding in pattern identification and anomaly detection.
- **Dimensionality Reduction**: Implementation of Principal Component Analysis (PCA) to reduce dataset dimensionality while retaining significant variance for improved model performance.
- **Clustering**: Application of K-Means clustering to group similar data points and uncover underlying data structures.
- **Model Training and Evaluation**: Training and evaluating multiple machine learning models, including Random Forest, XGBoost, LightGBM, Support Vector Machines, and Neural Networks, with performance metrics such as accuracy, confusion matrices, and classification reports.
- **Hyperparameter Tuning**: Utilization of grid search for optimizing model parameters, ensuring the best performance.
- **Learning Curves**: Visualization of learning curves to diagnose potential overfitting or underfitting issues as training set sizes vary.

## Dataset
The dataset comprises telemetry data from 19 drivers, capturing various vehicle parameters such as engine load, fuel level, RPM, and more. It has been meticulously processed to extract relevant features and eliminate inconsistencies.

## Installation
To get started, ensure you have the necessary libraries installed:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost lightgbm joblib
```

## Usage
1. Clone the repository:
   ```bash
   git clone <https://github.com/elkomy13/OBD.git>
   ```
2. Place your dataset (e.g., `exp2_19drivers_1car_1route.csv`) in the project directory.
3. Run the Jupyter Notebook or Python script to execute the data analysis and model training.

## Results
The project includes visualizations such as:
- Confusion matrices for each model.
- Bar charts comparing the accuracy of different models.
- Learning curves illustrating model performance over varying training sizes.

## Conclusion
This project serves as a valuable resource for automotive engineers, data scientists, and researchers interested in vehicle dynamics and performance analysis. Insights gained can inform targeted interventions and educational programs for improving driving behaviors.
