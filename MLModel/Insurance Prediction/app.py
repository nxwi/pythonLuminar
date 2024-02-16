import streamlit as st
import pickle
from PIL import Image


def main():
    st.title('Insurance Prediction')
    image = Image.open('image.jpeg')
    st.image(image, width=800)
    age = st.text_input('Age', placeholder='Type here')
    employmentType = st.text_input('Employment Type', placeholder='Type here')
    graduateOrNot = st.text_input('Graduate Or Not', placeholder='Type here')
    annualIncome = st.text_input('Annual Income', placeholder='Type here')
    familyMembers = st.text_input('Family Members', placeholder='Type here')
    chronicDiseases = st.text_input('Chronic Diseases', placeholder='Type here')
    frequentFlyer = st.text_input('Frequent Flyer', placeholder='Type here')
    everTravelledAbroad = st.text_input('Ever Travelled Abroad', placeholder='Type here')

    features = [age, employmentType, graduateOrNot, annualIncome, familyMembers, chronicDiseases, frequentFlyer,
                everTravelledAbroad]

    model = pickle.load(open('model.sav', 'rb'))  # rb-->read binarey
    scaler = pickle.load(open('scaler.sav', 'rb'))

    pred = st.button('PREDICT')  # FOR PREDICTION BUTTON

    if pred:
        prediction = model.predict(scaler.transform([features]))
        if prediction == 0:
            st.write('Will buy insurance')  # writ-->instead of print in st
        else:
            st.write('Will not buy insurance')


main()
