import streamlit as st
import webbrowser


def app():
    
    st.write("\n")
    
    st.markdown("##### ABOUT")
    st.write("\n")
    st.markdown('''With  advancement in  we are moving closer to
living in the metaverse. Metaverse is a virtual world where users exist as
avatars of themselves and interact with one another. The development of
metaverse is based on various domains of  such as virtual
reality, 3D , haptic devices, etc. The  of metaverse
largely depends on the users sense of  in the virtual world.
As the development of the metaverse is still in its early stages, not a lot
of work has been done to ensure that users are at  of the
metaverse design process. This project proposes a  for the
user centered design of  components of the metaverse based on
the existing user centered design framework for interfaces. The visual
components involved are avatars, non-player characters, and
environment.''')
    st.write("\n")
    st.markdown("The paper for this project can be viewed by clicking on the button below:")
    url = "https://drive.google.com/drive/folders/1kpGRcgtqfdMegpJVnkoaSaoope1VWZ7A?usp=sharing"
    if st.button("Paper"):
        webbrowser.open_new_tab(url)
    st.write("\n")
    st.markdown("This paper is accepted by the International Conference On Advance Technology In Engineering (ICACITE2022)")
    st.write("\n")
    st.markdown("Developed by Vaidehi Mahida")
    st.markdown("Under the guidance of: Dr. A. Jeyasekar")