# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 20:58:15 2024

@author: Sreejit
"""
#import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottie(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

dragon = load_lottie("https://lottie.host/be9c74d3-c475-4d1d-802c-ae6cb1c23211/PDq2IC7pkd.json")

st.title("Our Top 5 Dates")

# Romantic note
st.write("""
Hi Shree,

Now that my exams are over, I have tons of time, and I've decided to use this time to make you a nice website showcasing our most memorabel dates. With each date, I'll share the things I love the most about you.

You mean the world to me, and I can't wait to create more beautiful memories together.

Here's a dragon for you :bouquet:

Love,
Dum Dum
""")

# Animated dragon
st_lottie(dragon, key=None, loop=True)


st.header("[When we first met](https://x7pbbychhwftrnc3gjeoop.streamlit.app/)")
    


