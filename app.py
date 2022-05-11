import streamlit as st

# Custom imports 
from multipage import MultiPage
from pages import about, data_viz, ml

# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.title("Demo for the paper:")
st.subheader("User Centered Framework for the Design of the Visual Components of the Metaverse")
# Add all your applications (pages) here
app.add_page("About the Project", about.app)
app.add_page("Human Centered Design", data_viz.app)
app.add_page("Main Framework", ml.app)


# The main app
app.run()