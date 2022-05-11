
import streamlit as st

from PIL import Image


def app():
    
        # Show predictions
    #st.write('No hate speech found in the tweet with '+str(confidence())+'%'+' confidence' if prediction[0]==4 else 'Hate speech found in the tweet with '+str(confidence())+"%"+" confidence")
    image1 = Image.open("/home/ray/Desktop/WhatsApp Image 2022-05-10 at 3.22.47 PM.jpeg")
    st.image(image1, caption="Human centered design framework")
    