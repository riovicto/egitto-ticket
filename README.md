
# Museo Egizio Chatbot - Sistema di raccomandazione biglietti

Questo progetto contiene un chatbot per aiutare i visitatori del Museo Egizio a trovare il biglietto o l'esperienza migliore, integrato con la tabella completa delle offerte.

## Contenuto della cartella

- `museo_chatbot.py`: versione da terminale (console).
- `museo_chatbot_streamlit.py`: versione web interattiva (Streamlit).
- `Museo_Egizio_Chatbot_Colab.ipynb`: versione notebook per Google Colab.
- `Offerte_Museo_Egizio_Completo_Final.csv`: tabella completa delle offerte.
- `requirements.txt`: librerie necessarie.
- `README.md`: questa guida.

## Come usarlo

### Opzione 1: Eseguire da terminale (Python puro)

1. Assicurati di avere Python installato.
2. Installa le dipendenze:
    ```
    pip install -r requirements.txt
    ```
3. Avvia il chatbot da terminale:
    ```
    python museo_chatbot.py
    ```

### Opzione 2: Eseguire versione web (Streamlit)

1. Installa Streamlit:
    ```
    pip install streamlit
    ```
2. Avvia il chatbot web:
    ```
    streamlit run museo_chatbot_streamlit.py
    ```

### Opzione 3: Caricare su Google Colab

1. Carica il file `Museo_Egizio_Chatbot_Colab.ipynb` su Google Colab.
2. Esegui direttamente online.

### Opzione 4: Pubblicare su Streamlit Cloud

1. Crea un repository su GitHub.
2. Carica tutti i file.
3. Vai su [https://streamlit.io/cloud](https://streamlit.io/cloud).
4. Connetti il tuo repo e avvia l'app.

**Nota**: Mantieni il file CSV nella stessa cartella del codice per funzionare correttamente.

## Librerie richieste

- pandas
- streamlit
