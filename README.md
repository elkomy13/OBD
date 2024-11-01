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

# EDA
![image](https://github.com/user-attachments/assets/62800bc2-b0ba-4abc-8d7d-edc17375ad25)
![image](https://github.com/user-attachments/assets/6727c073-57ea-4e32-b8ab-5313bd9a23d1)

## Dataset
The dataset comprises telemetry data from 19 drivers, capturing various vehicle parameters such as engine load, fuel level, RPM, and more. It has been meticulously processed to extract relevant features and eliminate inconsistencies.

# PCA
![image](https://github.com/user-attachments/assets/2279280b-67bd-49f0-a5be-2834e2c4ced7)
![image](https://github.com/user-attachments/assets/28731155-fcbc-4627-a510-a73f4fba9829)

#K-Means
![image](https://github.com/user-attachments/assets/9b829792-8c9a-4bba-ac7c-e0e5591d41cc)
![image](https://github.com/user-attachments/assets/410c53c6-8320-45b0-a07a-57b68d3a7608)




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
- ![image](https://github.com/user-attachments/assets/c6a2aa0e-0aed-4fe0-91c8-62f906104ea3)
- ![image](https://github.com/user-attachments/assets/d80fe4fc-27dd-44a1-98ad-20b7912052bf)
- ![image](https://github.com/user-attachments/assets/c6c2863d-59ec-42e8-aca0-a4d157972600)
- ![image](https://github.com/user-attachments/assets/3a82a8e0-ab8f-469e-a64d-a89a83b58dc9)
- ![image](https://github.com/user-attachments/assets/72a4dcc6-df1b-4f0f-9951-dc0a504bebc9)
- ![image](https://github.com/user-attachments/assets/93728126-1e8d-49fc-b103-fedaf58b0a4a)
- ![image](https://github.com/user-attachments/assets/0bd844d2-9270-4ae2-b786-af4ac97b68e9)
- ![image](https://github.com/user-attachments/assets/718797d0-3ddf-49a8-a6a0-8e2eb27d1059)
- Bar charts comparing the accuracy of different models.
- ![image](https://github.com/user-attachments/assets/149bb05c-38ad-4cb4-b378-f41f5d9872ba)
- Learning curves illustrating model performance over varying training sizes.
- ![image](https://github.com/user-attachments/assets/8357a88b-093d-4f92-8e87-303bc801c485)


## Conclusion
This project serves as a valuable resource for automotive engineers, data scientists, and researchers interested in vehicle dynamics and performance analysis. Insights gained can inform targeted interventions and educational programs for improving driving behaviors.
