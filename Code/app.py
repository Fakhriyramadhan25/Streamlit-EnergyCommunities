import streamlit as st
from PIL import Image

satu = "satu"


class Index:

    def main():

        def postimage(a, b, c):
            imgResult = Image.open(a)
            st.image(imgResult, caption=b, width=c)

        st.set_page_config(
            page_title="Energy Communities",
            page_icon=":shark:",
            layout="centered",
            initial_sidebar_state="expanded",
            menu_items={
                'Get Help': 'https://www.extremelycoolapp.com/help',
                'Report a bug': "https://www.extremelycoolapp.com/bug",
                'About': "# This is a header. This is an *extremely* cool app!"
            }
        )
        st.title("Energy Communitites")
        st.subheader("What is Energy Communities")
        postimage("energycommunity.png", "Energy Communities", 600)
        st.markdown('''
        <p>Energy communities are initiatives led by citizens, allowing them to take control of their energy production and consumption. They help decentralize 
        the energy systems where the grid is owned by local people with solar and wind farms set up in fields or solar panels installed on rooftops. That way, 
        local people consume the clean and renewable energy they produce at home, and every household becomes a player in the energy sector. Citizens take an 
        active role in the decision-making process and share the economy within the local community, as these projects stimulate local employment.</p>
        ''', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.subheader(f"Objectives")
            st.markdown('''
    <p>There are several objectives that R2M wants to pursue in this project. These objectives are associated with energy communities. These are:
    <span><ul><li>Calculating potential of the renewable energy and energy consumption</li><li>Calculating the cost needed for the capital and investment rate</li>
    <li>classifying the energy balance and energy dependency</li><li>Recommending Steps in the Phase Project</li></ul></span></p>
            ''', unsafe_allow_html=True)

        with col2:
            st.subheader(f"Who we are")
            postimage("r2m.png", "", 200)
            st.markdown('''
    <p>R2M solution is a company that works on research field specifically for renewable energy. In this project 
    they collaborate with other company to create an energy community approach.</p>
            ''', unsafe_allow_html=True)
        with st.container():
            st.subheader(f"How the calculation")
            st.markdown('''
    <p>The calculation is for assesing the potential of energy communities from the technical energy and economical aspect. Apparently it only
    provides for Solar PV. In the technical energy there are several output, these are: <span><ul><li>Energy Consumption</li>
    <li>Energy Saving</li><li>Energy Potential Generated</li><li>Energy Balance</li><li>Energy Dependencies</li><li>Phase Energy</li></ul></span>
    The technical aspect is utilized to know whether the location has a potential of renewable energy particularly 
    Solar PV. Will the available area of the rooftops can produce a good amount of energy or will be worthless. Indeed, that the Solar PV now is affordable however 
    it still requires big capital thus it needs economical observation. From the economical aspect, these are the outputs:
    <span><ul><li>Investment</li><li>Expenditure</li></ul></span></p>
            ''', unsafe_allow_html=True)


if __name__ == '__main__':
    ct = Index()
    Index.main()
