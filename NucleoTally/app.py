import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open('images/dna.png')
st.image(image, use_column_width=True)
st.write("""
# NucleoTally
### DNA Nucleotide Counting Web App

***

## Enter DNA Sequence
""")
         
sequence_input = "AGCTCAGTGGTAGCTTAGCC\nTACGGACCTTATGAGAACGA\nGCTTAGCTAGATCCGACGTT"

sequence = st.text_area("DNA Sequences", sequence_input, height=150) 

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
        
def dna_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C')),

    ])
    return d

x = dna_nucleotide_count(sequence)
x_label = list(x)
x_values = list(x.values())

x

df = pd.DataFrame.from_dict(x, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'nucleotide'})
df

p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)

p = p.properties(
    width=alt.Step(80)
)

st.write(p)

