
import pickle
import numpy as np
import streamlit as st
import pandas as pd

# Load the model from the .pkl file
with open('Model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the Streamlit app
def main():
    st.title("ABS Logistics")
    text = st.text_input("Enter the hold code:")
    t=st.selectbox('Different Hold Codes',('MFG Part # Missing', 'ACK Missing', 'PO Missing'))
    if st.button("Predict Resolution Code"):
        sequence = np.array([text])
        prediction = model.predict(sequence)
        # Convert the prediction to a label
        st.success("The resolution code is {}".format(prediction))

if __name__ == "__main__":
    main()




 

