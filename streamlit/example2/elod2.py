import streamlit as st
import plotly.express as px
import streamlit.components.v1 as components
import pandas as pd
import numpy as np

# streamlit run elod2.py [-- script args]

# https://chart-selections-demo.streamlit.app/Plotly

# https://readmedium.com/how-to-get-all-plotly-themes-in-streamlit-24ef7730637f

st.write("Here's our <b> first attempt at using data to create a table v2")

st.plotly_chart(
    px.bar([1,5,3,7,9]),
    theme=None
)

# WITH IFRAME
# https://docs.streamlit.io/develop/api-reference/custom-components/st.components.v1.html

components.html('<b style="color:#f00">Hello</b>')

# https://docs.streamlit.io/develop/concepts/configuration/serving-static-files
components.html('<img src="/app/static/test.png">')

# WITHOUT IFRAME - JS NOT SUPPORTED
# https://docs.streamlit.io/develop/api-reference/text/st.html

st.html('<b style="color:#f00">Hello</b>')
st.html('<img src="/app/static/test.png">')
