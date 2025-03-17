
import pandas as pd

# Carica la tabella aggiornata delle offerte
df = pd.read_csv('Offerte_Museo_Egizio_Completo_Final.csv')

# Funzione di chatbot semplificato
def museo_chatbot():
    print("👋 Benvenuto! Ti aiuto a trovare il biglietto o l'esperienza migliore per visitare il Museo Egizio.")

    provenienza = input("👉 Vieni da Torino o sei in visita da fuori città? (Torino/Fuori): ").strip().lower()
    compagnia = input("👉 Con chi visiterai il museo? (Solo/Coppia/Famiglia/Amici): ").strip().lower()
    giorno = input("👉 Quando vorresti visitare il museo? (Feriale/Weekend): ").strip().lower()
    guida = input("👉 Preferisci una visita libera o guidata? (Libera/Guidata/Privata): ").strip().lower()
    tempo = input("👉 Quanto tempo vuoi dedicare alla visita? (1h/2h/Giornata/Più giorni): ").strip().lower()
    esclusiva = input("👉 Ti piacerebbe un'esperienza esclusiva o tranquilla? (Sì/No): ").strip().lower()

    print("\n📢 Ecco alcune proposte per te:\n")

    # Logica semplificata di raccomandazione
    if provenienza == "torino":
        print("- 🎫 Carnet 3 Ingressi Flessibili: per chi vuole tornare più volte durante l'anno.")
        print("- 🌇 Biglietto 'Sunset/Ultima ora': visita suggestiva al tramonto (perfetta se vuoi foto speciali).")
    elif provenienza == "fuori":
        print("- 🌍 Biglietto '3 Giorni Egizi': ideale per chi visita Torino e vuole scoprire il museo con calma in 72 ore.")

    if compagnia == "famiglia":
        print("- 👨‍👩‍👧‍👦 Visita guidata per famiglie 'A casa di Kha': per bambini 5-11 anni, esplorando la vita quotidiana.")
        print("- 🎟️ Biglietto Famiglia (2 adulti + 2 minori): per visita libera.")
    elif compagnia == "coppia":
        print("- ❤️ Biglietto 'Sunset/Ultima ora': perfetto per coppie, magari per un appuntamento speciale.")
        print("- 🤫 Biglietto 'Senza Folla': visita esclusiva fuori dagli orari di punta.")

    if giorno == "weekend":
        print("- ⚠️ Attenzione: il weekend è affollato. Ti consiglio di scegliere il biglietto 'Senza Folla' o visitare in orari meno frequentati.")

    if guida == "guidata":
        print("- 🗣️ Scopri le nostre visite guidate, anche per gruppi fino a 25 persone (es. 'Materia. Forma del Tempo').")
    elif guida == "privata":
        print("- 👤 Prenota una visita privata per un'esperienza su misura.")

    if tempo in ["più giorni", "giornata"]:
        print("- 🌍 Biglietto '3 Giorni Egizi': ideale per esplorare il museo con calma.")

    if esclusiva == "sì":
        print("- 🤫 Ti consiglio il Biglietto 'Senza Folla' per visitare il museo in tranquillità.")

    print("\n📝 Vuoi che ti mandi il link per prenotare uno di questi biglietti? (Sì/No)")

# Avvio chatbot
if __name__ == '__main__':
    museo_chatbot()
