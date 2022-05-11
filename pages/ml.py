import streamlit as st
from PIL import Image

def app():
    st.markdown("### User cenetered fraework for the design of the visual components of the metaverse")
    st.write("\n")
    st.markdown('''The proposed framework contains four stages:
1. Understanding the users and the context of design
2. Planning and ideating design solutions
3. Designing the visual components
4. Evaluating the design
The design process is iterative. Internal and external feedback needs
to be obtained at each step. Changes based on the feedback should be
incorporated into the design. Users are involved in each stage of the
design and feedback process.
                    ''')
    image1 = Image.open('/home/ray/Desktop/WhatsApp Image 2022-05-10 at 3.22.48 PM.jpeg')
    st.image(image1)
    st.write("\n")
   
