import requests

def invia_patch_note_via_webhook(webhook_url, patch_note):
    headers = {
        'Content-Type': 'application/json'
    }

    payload = {
        'content': patch_note
    }

    response = requests.post(webhook_url, json=payload, headers=headers)

    if response.status_code == 204:
        print("Patch note inviato con successo tramite webhook.")
    else:
        print(f"Errore nell'invio delle patch note tramite webhook. Codice di stato: {response.status_code}")

# Esempio di utilizzo della funzione
def main():
    # URL del webhook - Sostituisci 'URL_WEBHOOK' con l'URL effettivo del webhook
    URL_WEBHOOK = 'https://discord.com/api/webhooks/1123645595584835694/TRsYLTr7Mzr8m8kLDgetO6dOZERw-XPASmyS-qu3xeX6ktZNPLFc3x5JH9Qya6MEA3_w'

    # Patch note da inviare
    patch_note = """\
 Padre Maronno Versione 1.1.0 (Data di rilascio: [data])

Nuove funzionalità:

Implementata la funzione per inviare una predica casuale in un canale specifico quando viene rilevato un insulto.
Aggiunta la possibilità di eseguire la "messa" ogni domenica alle 10:00 in un canale specifico.
Cambiamenti e miglioramenti:

Aggiunta la libreria better_profanity per rilevare insulti e linguaggio volgare nei messaggi.
Implementata la possibilità di utilizzare una lista custom di parole inappropriate con better_profanity.
Aggiunte prediche personalizzate per la "messa" tramite una lista di prediche.
Ottimizzata la gestione degli errori e stampa dei messaggi di debug per facilitare il rilevamento e la risoluzione dei problemi.
Correzioni di bug:

Risolto un problema che impediva l'invio delle prediche in un canale specificato.
Corretta l'importazione del modulo datetime per evitare conflitti con il modulo incluso di default in Python.
Istruzioni per l'uso:

Installare le librerie discord.py, openai (per la chat GPT), e better_profanity (per il rilevamento degli insulti) tramite pip install discord.py openai better_profanity.
Impostare il token di accesso del bot Discord in TOKEN.
Configurare l'ID del canale per la "messa" in canale_messa_id.
Aggiungere prediche personalizzate nella lista prediche per la funzione "messa".
Avviare lo script per far partire il bot."""

    # Invia le patch note tramite il webhook
    invia_patch_note_via_webhook(URL_WEBHOOK, patch_note)

if __name__ == "__main__":
    main()
