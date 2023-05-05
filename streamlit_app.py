import streamlit as st
import pandas as pd
import numpy as np
import mymodel as m

st.title("What is this!??!")

windows = st.slider("Slide this to the right")
st.write(m.run(window=window))

