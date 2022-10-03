import streamlit as st
from PIL import Image
import streamlit as st

st.title("Recommendations for the Stage of the Project")

with st.container():
    with st.form("my_form"):
        Recs = st.selectbox(
            'Stage of the project are you in',
            ('Initiating', 'Planning', 'Implementation', 'Operation'))

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted and Recs == 'Initiating':
            st.success("This is the recommendation for you")
            imgResult = Image.open('Initiate.jpg')
            st.image(imgResult, caption='Initiating Phase')
            st.markdown(
                '<ul><li>Simulations</li><li>study local regulation</li><li>See examples of our pilots</li></ul>', unsafe_allow_html=True)
            url = "https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py"
            st.markdown("[find out more](%s)" % url)
        elif submitted and Recs == 'Planning':
            st.success("This is the recommendation for you")
            imgResult = Image.open('plan.jpg')
            st.image(imgResult, caption='Planning Phase')
            st.markdown('<ul><li>Digital Twin for Planning Phase</li></ul>',
                        unsafe_allow_html=True)
            url = "https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py"
            st.markdown("[find out more](%s)" % url)
        elif submitted and Recs == 'Implementation':
            st.success("This is the recommendation for you")
            imgResult = Image.open('implem.jpg')
            st.image(imgResult, caption='Implementation Phase')
            st.markdown(
                '<ul><li>Investment protocols for access to finance</li><li>Business Models</li><li>contracting templates for CES</li></ul>', unsafe_allow_html=True)
            url = "https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py"
            st.markdown("[find out more](%s)" % url)
        elif submitted and Recs == 'Operation':
            st.success("This is the recommendation for you")
            imgResult = Image.open('operate.jpg')
            st.image(imgResult, caption='Operation Phase')
            st.markdown(
                '<ul><li>Management and trading platform</li><li>Digital Twin for Operation Phase</li></ul>', unsafe_allow_html=True)
            url = "https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py"
            st.markdown("[find out more](%s)" % url)

test123 = "goodluck"
