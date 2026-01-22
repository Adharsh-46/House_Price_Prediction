#House Price Prediction Project

This project applies Machine Learning to predict house prices based on multiple features such as area, number of bedrooms, location, and amenities. The system integrates a machine learning model with a web application for real-time predictions.


---

Project Structure

House_Price_Dataset.csv – Raw dataset used for training and testing

house_price_model.py – Python script for data preprocessing, model training, and evaluation

house_price_webapp/ – Frontend and backend files for the web application

index.html / style.css / script.js – Frontend interface

app.py – Flask backend (API integration)


price_prediction.ipynb – Jupyter Notebook with exploratory data analysis (EDA)

requirements.txt – Dependencies for running the project

README.md – Project documentation



---

 Tools & Technologies Used

Python: pandas, numpy, scikit-learn, matplotlib, seaborn

Machine Learning: Linear Regression, Decision Trees, Random Forest

Web Development: HTML, CSS, JavaScript, Flask / React (for web app deployment)

Database (Optional): MySQL / SQLite for storing historical predictions

Deployment: GitHub, Streamlit, or Flask



---

Key Analyses Performed

Data cleaning and preprocessing (handling missing values, encoding categorical variables)

Exploratory Data Analysis (EDA):

Price distribution and outlier detection

Correlation between features (area, location, BHK, amenities)

Feature importance analysis


Model training & evaluation using RMSE and R² score

Comparison of different ML algorithms for prediction accuracy



---

Insights

Location and area size are the most influential factors in determining price.

Outliers (luxury homes) significantly skew average pricing.

Linear Regression works well for smaller datasets, while Random Forest provides higher accuracy for large datasets.

Web application enables real-time, user-friendly predictions.



---

 Recommendations

Add more features like infrastructure projects to improve accuracy.

Deploy the model on cloud platforms (AWS, Azure, or GCP) for scalability.

Enable real-time data updates using APIs for dynamic pricing.

Introduce visual dashboards for buyers and sellers to analyze pricing trends.



---

 How to Run

1. Clone the repository or download ZIP

git clone https://github.com/yourusername/house-price-prediction.git
cd house-price-prediction


2. Install required dependencies

pip install -r requirements.txt


3. Run the model training script

python house_price_model.py


4. Launch the web application

python app.py

Open http://127.0.0.1:5000 in your browser to access the web app.




---

Author

Adharsh Kumar


---

License

For academic and demo use only.
