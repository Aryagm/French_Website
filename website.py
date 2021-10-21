import streamlit as st
import pandas as pd

_, col1, _ = st.columns(3)

with col1:
    st.image("images/logo.png")


st.markdown("<h1 style='text-align: center; color: green;font-family:Bahnschrift;font-size: 50px;'>Essence De Lahore!</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: orange;font-family:Brush Script MT;font-size: 40px;'>Cuisine de Lahori!</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: black;font-family:Bahnschrift;'>3003 Boul. le Carrefour, Laval, QC H7T 1C7</h2>", unsafe_allow_html=True)


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
    st.markdown("<br/>", unsafe_allow_html=True)

    b = st.button("Lahori Biryani!")
    st.markdown("<br/>", unsafe_allow_html=True)

    c = st.button("Poisson Frit Lahori!")
    st.markdown("<br/>", unsafe_allow_html=True)

    d = st.button("Information Additionnelle!")
    st.markdown("<br/>", unsafe_allow_html=True)

    inp = st.text_input("D'autres questions?")

if not a and not b and not c and not d and not inp:
    with col3:
        st.title("👈 Cliquez sur les boutons à gauche!")

if a:
    with col3:
        st.title("Bonjour!")

        st.warning('Bienvenue à Essence de Lahore, Je suis votre "virtual waiter"! Je vais vous donner des informations sur notre food truck. Nous servons une cuisine traditionnelle Lahori. Cliquez sur les boutons pour en savoir plus! 😋')

        st.audio("Audio/bonjour.mp3")

if b:
    with col3:
        st.image("images/biryani.jpg")
        st.warning("Lahori Biryani est notre premier plat de spécialité. C'est un plat épicé à base de riz et de mouton. Il a beaucoup de saveur! Un repas parfait! 🍛")
        products = ["Lahori Biryani", "Drink", "Salade", "SubTotal:"]
        prices = ["$7.50", "$2.50", "$4.99", "$14.99"]
        df_dict = {"Produit": products, "Prix": prices}
        df = pd.DataFrame(df_dict)
        st.table(df)
        st.audio("Audio/biryani.mp3")

if c:
    with col3:
        # st.markdown("## Lahori Fried Fish!")
        st.image("images/fried_fish.jpg")
        st.warning("Le poisson frit Lahori est notre deuxième délice ! Le plat est du saumon frit trempé dans un mélange salé. Il est servi avec une sauce piquante et garni d'épices! Délicieux! 🐟")
        products = ["Lahori Poisson Frit", "Drink", "Salade", "SubTotal:"]
        prices = ["$8.50", "$2.50", "$4.99", "$15.99"]
        df_dict = {"Produit": products, "Prix": prices}
        df = pd.DataFrame(df_dict)
        st.table(df)
        st.audio("Audio/fish.mp3")

if d:
    with col3:
        st.title("Information Additionnelle!")
        # """ st.markdown("🏡 Notre adresse est: 3003 Boul. le Carrefour, Laval, QC H7T 1C7")
        #st.markdown("📞 Vous pouvez nous contacter au: +1 514 555 1480")
        #st.markdown("🌐 Notre site Web est: www.essencedelahore.ca")
        # st.markdown("🕙 Nous sommes ouverts de 10h à 22") """
        medium = ["Address", "Telephone", "Website", "Opening Hours"]
        prices = ["3003 Boul. le Carrefour, Laval, QC H7T 1C7",
                  "+1 514 555 1480", "www.essencedelahore.ca", "10am to 10pm"]
        df_dict = {"Information": medium, "   ": prices}
        df = pd.DataFrame(df_dict)
        st.table(df)

if not a and not b and not c and not d and inp:
    with col3:
        if "biryani" in inp.lower():
            st.title("Reponse")
            st.warning("Le prix de Lahori Biryani est de $14.99")
            products = ["Lahori Biryani", "Drink", "Salade", "SubTotal:"]
            prices = ["$7.50", "$2.50", "$4.99", "$14.99"]
            df_dict = {"Produit": products, "Prix": prices}
            df = pd.DataFrame(df_dict)
            st.table(df)
            st.audio("Audio/question_biryani.mp3")
            
        if "poisson" in inp.lower():
            st.title("Reponse")
            st.warning("Le prix de Poisson Frit Lahori est de $15.99")
            products = ["Lahori Poisson Frit", "Drink", "Salade", "SubTotal:"]
            prices = ["$7.50", "$2.50", "$4.99", "$15.99"]
            df_dict = {"Produit": products, "Prix": prices}
            df = pd.DataFrame(df_dict)
            st.table(df)
            st.audio("Audio/question_fish.mp3")
