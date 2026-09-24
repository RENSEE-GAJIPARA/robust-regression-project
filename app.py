"""
Robust Regression Engine - House Price Predictor Streamlit app that loads the best model trained in
the notebook (Models/best_model.pkl) and lets a user predict a house price from property attributes.
"""

import pickle
import pandas as pd 
import streamlit as st

st.set_page_config(page_title="House Price Predictor", page_icon="🏠", layout="centered")

@st.cache_resource
def load_model():
    with open("Models/best_model.pkl", "rb") as file:
        return pickle.load(file)
    
bundle = load_model()
model = bundle["model"]
scaler = bundle["scaler"]
feature_order = bundle["features"]
model_name = bundle["model_name"]

st.title("🏠 Robust Regression Engine")
st.caption(f"Predicting house prices with a tuned **{model_name}** model")

st.markdown(
    "Fill in the property details below and the model will estimate the "
    "market price (in INR). This app uses the same regression pipeline "
    "built and validated in the accompanying Jupyter notebook — "
    "regularization, cross-validation, tree ensembles and SVR were all "
    "compared, and this model came out on top on held-out test data."
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    area_sqft = st.number_input("Area (sq. ft.)", min_value=200, max_value=10000, value=1700, step=50)
    bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3, step=1)
    bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2, step=1)
    location_score = st.slider("Location score (1 = worst, 10 = best)", 1.0, 10.0, 6.5, 0.1)
    property_age = st.number_input("Property age (years)", min_value=0, max_value=100, value=20, step=1)

with col2:
    distance_city_km = st.number_input("Distance to city center (km)", min_value=0.0, max_value=100.0, value=13.0, step=0.5)
    crime_rate_index = st.slider("Crime rate index (0 = safest)", 0.0, 10.0, 4.2, 0.1)
    near_school = st.selectbox("Near a school?", ["No", "Yes"]) == "Yes"
    near_metro = st.selectbox("Near a metro station?", ["No", "Yes"]) == "Yes"

st.divider()

if st.button("Predict House Price", type="primary", use_container_width=True):
    input_row = pd.DataFrame([{
        "area_sqft": area_sqft,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "location_score": location_score,
        "property_age": property_age,
        "distance_city_km": distance_city_km,
        "near_school": int(near_school),
        "near_metro": int(near_metro),
        "crime_rate_index": crime_rate_index,
    }])[feature_order]

    if scaler is not None:
        input_processed = scaler.transform(input_row)
    else:
        input_processed = input_row

    prediction = model.predict(input_processed)[0]

    st.success(f"### Estimated Price: ₹ {prediction:,.0f}")
    st.caption(
        "This is a point estimate from a machine learning model trained on "
        "historical sales data — treat it as a data-driven guideline, not "
        "an official valuation."
    )
    
st.divider()
with st.expander("About this model"):
    st.write(
        f"""
        - **Model used:** {model_name}
        - **Features:** {", ".join(feature_order)}
        - Trained and validated with an 80/20 train-test split plus
            5-fold cross-validation for hyperparameter tuning.
        - Selected as the best performer after comparing Ridge, Lasso,
            Decision Tree, Random Forest, and SVR (linear & RBF kernels)
            on held-out test data — see the notebook for the full comparison.
        """
    )