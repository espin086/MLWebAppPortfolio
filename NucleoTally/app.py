import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

st.write("""
# NucleoTally
### DNA Nucleotide Counting Web App

***

## Enter DNA Sequence
""")
         
sequence_input = "AGCTCAGTGGTAGCTTAGCC\nTACGGACCTTATGAGAACGA\nGCTTAGCTAGATCCGACGTT"

sequence = st.text_area("DNA Sequences", sequence_input, height=250) 

sequence = sequence.splitlines()
sequence = ''.join(sequence)

st.write("""
***
## Input (DNA Query)
""")
sequence

st.write("""
***
## Output (DNA Nucleotide Count)
""")


