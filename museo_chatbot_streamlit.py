
import streamlit as st
import pandas as pd

# Carica la tabella aggiornata delle offerte
@st.cache
def load_data():
    return pd.read_csv('Offerte_Museo_Egizio_Completo_Final.csv')

df = load_data()

st.title("🎟️ Museo Egizio - Trova il tuo biglietto ideale")

st.write("Benvenuto! Rispondi a queste semplici domande per scoprire il biglietto o l'esperienza migliore per te.")

# Domande interattive
provenienza = st.radio("👉 Vieni da Torino o sei in visita da fuori città?", ["Torino", "Fuori"])
compagnia = st.radio("👉 Con chi visiterai il museo?", ["Solo", "Coppia", "Famiglia", "Amici"])
giorno = st.radio("👉 Quando vorresti visitare il museo?", ["Feriale", "Weekend"])
guida = st.radio("👉 Preferisci una visita libera o guidata?", ["Libera", "Guidata", "Privata"])
tempo = st.radio("👉 Quanto tempo vuoi dedicare alla visita?", ["1h", "2h", "Giornata", "Più giorni"])
esclusiva = st.radio("👉 Ti piacerebbe un'esperienza esclusiva o tranquilla?", ["Sì", "No"])

# Raccomandazioni dinamiche
st.subheader("📢 Ecco alcune proposte per te:")

if provenienza == "Torino":
    st.write("- 🎫 **Carnet 3 Ingressi Flessibili**: per chi vuole tornare più volte durante l'anno.")
    st.write("- 🌇 **Biglietto 'Sunset/Ultima ora'**: visita suggestiva al tramonto (perfetta se vuoi foto speciali).")
elif provenienza == "Fuori":
    st.write("- 🌍 **Biglietto '3 Giorni Egizi'**: ideale per chi visita Torino e vuole scoprire il museo con calma in 72 ore.")

if compagnia == "Famiglia":
    st.write("- 👨‍👩‍👧‍👦 **Visita guidata per famiglie 'A casa di Kha'**: per bambini 5-11 anni, esplorando la vita quotidiana.")
    st.write("- 🎟️ **Biglietto Famiglia (2 adulti + 2 minori)**: per visita libera.")
elif compagnia == "Coppia":
    st.write("- ❤️ **Biglietto 'Sunset/Ultima ora'**: perfetto per coppie, magari per un appuntamento speciale.")
    st.write("- 🤫 **Biglietto 'Senza Folla'**: visita esclusiva fuori dagli orari di punta.")

if giorno == "Weekend":
    st.write("- ⚠️ **Attenzione**: il weekend è affollato. Ti consiglio il biglietto 'Senza Folla' o visitare in orari meno frequentati.")

if guida == "Guidata":
    st.write("- 🗣️ Scopri le nostre **visite guidate**, anche per gruppi fino a 25 persone (es. 'Materia. Forma del Tempo').")
elif guida == "Privata":
    st.write("- 👤 Prenota una **visita privata** per un'esperienza su misura.")

if tempo in ["Più giorni", "Giornata"]:
    st.write("- 🌍 **Biglietto '3 Giorni Egizi'**: ideale per esplorare il museo con calma.")

if esclusiva == "Sì":
    st.write("- 🤫 Ti consiglio il **Biglietto 'Senza Folla'** per visitare il museo in tranquillità.")

st.write("\n📝 Vuoi ricevere il link per prenotare uno di questi biglietti? Contatta il nostro staff!")
