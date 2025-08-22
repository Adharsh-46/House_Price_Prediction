import sklearn
import pandas as pd
import streamlit as st
import joblib
import sklearn.compose._column_transformer as ct

# Patch: fake _RemainderColsList if missing
if not hasattr(ct, "_RemainderColsList"):
    class _RemainderColsList(list):
        pass
    ct._RemainderColsList = _RemainderColsList

model = joblib.load("house_price_model.joblib","rb")

st.header("Hyderabad House Price Predictor")
# Load your dataset for unique values
data = pd.read_csv(r"cleaned_data.csv")

# Collect inputs
tit= st.selectbox("Choose the type", data['title'].unique())
loc= st.selectbox("Choose the location", data['location'].unique())
ratesqft = st.number_input("Enter rate per sqft")
areasqft = st.number_input("Enter area in sqft")
buildsta = st.selectbox("Enter building status",data['building_status'].unique())

example_input = pd.DataFrame([{
    "title": tit,
    "location": loc,
    "rate_persqft": ratesqft,
    "area_insqft": areasqft,
    "building_status": buildsta
}])

predicted_price = model.predict(example_input)
print(model.named_steps['preprocessor'].transformers_)

example_input = example_input[["title", "location", "rate_persqft", "area_insqft", "building_status"]]

if st.button("Predict"):
    st.write("Input to model:", example_input)
    predicted_price = model.predict(example_input)
    st.success(f"Predicted price: {predicted_price[0]:.2f} Lakhs")

