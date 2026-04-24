import streamlit as st
import pickle

model = pickle.load(open('model.pkl', 'rb'))

st.title("Marks Predictor")

mid = st.number_input("Enter Mid Marks", min_value=0.0, max_value=100.0)

if st.button("Predict"):
    result = model.predict([[mid]])
    
    # FIX HERE 👇
    st.write("DEBUG result:", result)
    st.write("DEBUG type:", type(result))
    final_marks = float(result[0])
    
    st.write("Predicted Final Marks:", round(final_marks, 2))
