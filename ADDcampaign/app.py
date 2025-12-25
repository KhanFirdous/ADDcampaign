import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("campaign_model.pkl")

st.title(" Product Ad Campaign Order Predictor")

st.write("Enter campaign details to predict expected orders")

# Input fields
st.subheader("Campaign Inputs")

email_rate = st.slider("Email Rate", 0.1, 0.9, 0.4)
price = st.number_input("Product Price", min_value=0, value=160)
discount_rate = st.slider("Discount Rate", 0.0, 1.0, 0.8)
hour_resouces = st.number_input("Hour Resources", value=800)
campaign_fee = st.number_input("Campaign Fee", value=3000)

limit_infor = st.selectbox("Limit Info", [0, 1])
campaign_type = st.selectbox("Campaign Type", [0,1,2,3,4,5,6])
campaign_level = st.selectbox("Campaign Level", [0,1])
product_level = st.selectbox("Product Level", [1,2,3])
resource_amount = st.selectbox("Resource Amount", [1,2,3,4,5,6,7,8])



if st.button("Predict Orders"):
    input_df = pd.DataFrame([{
        'limit_infor': limit_infor,
        'campaign_type': campaign_type,
        'campaign_level': campaign_level,
        'product_level': product_level,
        'resource_amount': resource_amount,
        'email_rate': email_rate,
        'price': price,
        'discount_rate': discount_rate,
        'hour_resouces': hour_resouces,
        'campaign_fee': campaign_fee
    }])

    prediction = model.predict(input_df)[0]
    st.success(f"📦 Predicted Orders: {int(prediction)}")

