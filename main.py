import asyncio
from datetime import datetime
import random
import inflect
from better_profanity import profanity
import discord
import openai
from config import DISCORD_TOKEN
from config import GPT_API_KEY
from config import canale_messa_id
import nltk
from nltk.stem import WordNetLemmatizer


# Inizializza il client Discord e il modello ChatGPT
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

openai.api_key = GPT_API_KEY

# Lista di risposte predefinite per le confessioni
confessioni_predefinite = [
    "Pregherò per te.",
    "Dio ti ama incondizionatamente e ti perdona.",
    "Troverai la forza per affrontare i tuoi errori e superarli.",
    "La tua confessione è ascoltata e accolta con amore.",
    "Ricorda che nessuno è perfetto, ma la volontà di cambiare può portare alla redenzione.",
]
# Lista di prediche
prediche = [
    "Ama il prossimo tuo come te stesso.",
    "La fede muove montagne.",
    "La speranza è la luce che ci guida.",
    "La pazienza è una virtù.",
    "Non giudicare gli altri, ma guarda prima te stesso.",
    "Non osare ad insultare il Divino!"
]


# Lista di parole custom da considerare inappropriate
parole_inappropriate = [
    "porco",
    "porca",
    "porche",
    "dio",
    "dei",
    "troia",
    "troie",
    "madonna",
    "madonne",
    "gesù",
    "cazzo",
    "cazzi",
    "figa",
    "fighe"
    "culo",
    "culi",
    "puttana",
    "puttane",
    "ddio"
    # Aggiungi qui altre parole custom
]
# Inizializza il lemmatizzatore
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

# Inizializza l'oggetto Inflect
p = inflect.engine()
# Funzione per inviare una predica casuale nel canale specificato
async def invia_predica():
    try:
        canale_messa = client.get_channel(1120757774062719026)
        if canale_messa:
            await canale_messa.send(""""Confesso a Dio onnipotente e a voi, fratelli e sorelle,
che ho molto peccato
in pensieri, parole, opere e omissioni,
per mia colpa, mia colpa, mia grandissima colpa.
E supplico la beata sempre Vergine Maria,
gli angeli, i santi e voi, fratelli e sorelle,
di pregare per me il Signore Dio nostro.""")
        else:
            print(f"Il canale_messa con ID {canale_messa_id} non è stato trovato.")
    except Exception as e:
           print(f"Si è verificato un errore durante l'invio della predica: {e}")



# Aggiungi le parole custom alla lista delle parole inappropriare della libreria
profanity.load_censor_words(parole_inappropriate)
# Inizializza il lemmatizzatore
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

# Funzione per lemmatizzare una parola
def lemmatize_word(word):
    return lemmatizer.lemmatize(word, pos='n').lower()
# Funzione per inviare una predica casuale o una confessione casuale nel canale specificato
async def invia_messa_o_confessione(messaggio):
    canale_messa_e_confessioni = client.get_channel(1120757774062719026)
    if canale_messa_e_confessioni:
        # Controlla se il messaggio contiene insulti
        if profanity.contains_profanity(messaggio.content):
            # Invia una predica casuale in risposta agli insulti
            predica_casuale = random.choice(prediche)
            await canale_messa_e_confessioni.send(predica_casuale)
        # Controlla se il messaggio inizia con il comando per la confessione
        elif messaggio.content.startswith('!confessione'):
            confessione_casuale = random.choice(confessioni_predefinite)
            await canale_messa_e_confessioni.send(confessione_casuale)
    else:
        print(f"Il canale_messa_e_confessioni con ID 1120757774062719026 non è stato trovato.")


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    print('------')
    # Avvia la task per eseguire la messa o la confessione
    await esegui_messa_o_confessione()
async def esegui_messa_o_confessione():
    while True:
        ora_corrente = datetime.now()
        # Controlla se è domenica e l'ora è 10:00
        if ora_corrente.weekday() == 6 and ora_corrente.hour == 10:
            await invia_messa_o_confessione()
            # Attendi un minuto per evitare di inviare più messaggi nella stessa ora
            await asyncio.sleep(60)
        # Attendi un minuto prima di verificare nuovamente
        await asyncio.sleep(60)
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Verifica se il messaggio contiene insulti
    if profanity.contains_profanity(message.content):
        # Non inviare alcuna risposta qui
        pass

    # Verifica se il messaggio inizia con il comando per la confessione
    elif message.content.startswith('!confessione'):
        confessione_casuale = random.choice(confessioni_predefinite)
        await message.channel.send(confessione_casuale)

    # Invia il messaggio come parametro alla funzione per la predica o confessione
    await invia_messa_o_confessione(message)

if __name__ == "__main__":
    # Carica la lista di parole inappropriate nella libreria better_profanity
    profanity.load_censor_words(parole_inappropriate)
    client.run(DISCORD_TOKEN)
