import streamlit as st
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["a", "b", "c"])

data2 = pd.DataFrame(
    np.array([[1, 0, 0], [0, 2, 0], [0, 0, 4]]),
    columns=["Energy Generated", "Energy Consumption", "Energy Savings"])


st.write(chart_data)

st.bar_chart(chart_data)
st.bar_chart(data2)
