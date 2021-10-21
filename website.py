import streamlit as st

_, col1, _ = st.columns(3)

with col1:
    st.image("logo.png")


st.markdown("<h1 style='text-align: center; color: green;font-family:Bahnschrift;font-size: 50px;'>Essence De Lahore!</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: white;font-family:Brush Script MT;'>4528 Renaud Rue , Contrecoeur, QC, J0L 1C0</h2>", unsafe_allow_html=True)


st.markdown("<hr/>", unsafe_allow_html=True)
st.markdown("<br/>", unsafe_allow_html=True)

m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: white;
    color:green;
    height: 4em;
    width: 8em; 
}
</style>""", unsafe_allow_html=True)

col2, col3 = st.columns(2)
with col2:
    a = st.button("Bonjour!")

    c = st.button("Lahori Biryani!")

    c = st.button("Lahori Fried Fish!")

    c = st.button("Information Additionnelle!")

    st.text_input("Any Other Questions")

if a:
    with col3:
        st.title("Bonjour!")

        st.warning('Bienvenue à Essence de Lahore, Je suis votre "virtual waiter"! Je vais vous donner des informations sur notre food truck. Cliquez sur les boutons ci-dessous! 😋')
        
        st.audio("Audio/bonjour.mp3")
