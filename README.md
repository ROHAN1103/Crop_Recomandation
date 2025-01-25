# Crop_Recomandation

**Project Overview**

This project predicts the most suitable crop to cultivate on a given piece of land based on environmental and soil conditions. The goal is to assist farmers in making informed decisions to maximize productivity and efficiency.

![image](https://github.com/user-attachments/assets/82dc91d4-70b9-4864-848d-bd5c4ca6bd10)


**Dataset**

* *Source:*
The dataset (Crop_recommendation.csv) contains information about various crops and their corresponding environmental conditions.

* *Attributes:*

  1. **Soil nutrients:** Nitrogen (N), Phosphorus (P), Potassium (K)

  2. **Climate factors:** Temperature, Humidity, pH, Rainfall

  3. **Target:** Crop label (e.g., rice, maize, banana, coffee, etc.)

  4. **Dataset Size:** Include details such as the number of rows and columns.

**Data Preprocessing**

* *Exploratory Data Analysis (EDA):*
Examined dataset structure using .info(), .describe(), and .value_counts().
Analyzed distribution of crops and nutrient levels.

* *Feature Scaling:*
Normalized soil nutrients (N, P, K) and environmental features (temperature, humidity, pH, and rainfall) using MinMaxScaler.

* *Encoding:*
Encoded crop labels into numerical values using LabelEncoder.

**Data Analysis**

* Observed relationships between features (e.g., nutrient levels vs. crop suitability).
* Identified trends and patterns, such as which crops require high nitrogen or grow in specific pH ranges.

**Machine Learning Models**

*Models Used:*
  1. Random Forest
  2. Decision Tree
  3. Logistic Regression
  4. Linear Regression
  5. Adaboost Regression
  6. Gradient Boosting Regression
     
*Training and Testing:*

* Split dataset into training and testing sets (e.g., 80/20 split).
*Evaluation:*

* Metrics: MAE, R-Square

**Visualizations**

*Graphs and plots:*

* Distribution of crops in the dataset.
* Correlation heatmap between features.
* Feature importance from ML models.
* Tools Used: Matplotlib, Seaborn.

**Streamlit Web Application**

The project includes a user-friendly Streamlit-based web application that allows users to input soil and environmental parameters and receive crop recommendations in real-time.

*Features:*

1. Interactive Inputs:

  - Users can provide values for the following features:
  * Nitrogen (N): 0–140
  * Phosphorus (P): 0–145
  * Potassium (K): 0–210
  * Temperature: 0–45°C
  * Humidity: 0–100%
  * pH: 0–10
  * Rainfall: 0–300 mm
Inputs are dynamically adjustable using sliders or numeric fields.

2. Backend Model:

  - The application loads a pre-trained machine learning model (model.pkl) and a scaler object (scaler.pkl) using joblib.
  - The features provided by the user are scaled and normalized before making predictions.

3.Crop Recommendation:

  * After processing the input features, the model predicts the most suitable crop from a predefined list, including crops like rice, maize, banana, mango, etc.
  * The predicted crop is displayed on the interface.

4. Code Efficiency:

  * The app caches the model and scaler using @st.cache_resource for faster loading and improved efficiency.
