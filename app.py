import streamlit as st
import pickle

model = pickle.load(open('model.pkl', 'rb'))

st.title("Marks Predictor")

mid = st.number_input("Enter Mid Marks", min_value=0.0, max_value=100.0)

if st.button("Predict"):
    result = model.predict([[mid]])
    st.write("Predicted Final Marks:", round(result[0], 2))
