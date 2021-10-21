import streamlit as st

_, col1, _ = st.columns([2,4,2])

with col1:
    st.image("logo.png")


st.markdown("<h1 style='text-align: center; color: green;font-family:Bahnschrift;font-size: 75px;'>Essence De Lahore!</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: gray;font-family:Brush Script MT;'>4528 Renaud Rue , Contrecoeur, QC, J0L 1C0</h2>", unsafe_allow_html=True)


st.markdown("<hr/>", unsafe_allow_html=True)
st.markdown("<br/>", unsafe_allow_html=True)