import datetime
import random
import streamlit as st

st.set_page_config(
    page_title="Pyjama Party Game",
    page_icon="🎉",
    layout="centered",
)

player_names = ["Eleonora", "Eugenio", "Maurizio", "Luca", "Natalia", "Sophie"]
roles = ["Mucca", "Pecora", "Cavallo", "Lupo", "Cinghiale", "Aquila"]
secret_agendas = [
    "Balla (anche solo un accenno) con qualcuno per almeno 10 secondi",
    "Riesci a farti offrire da bere da qualcuno",
    "Tieni un braccio intorno alle spalle di qualcuno per almeno 20 secondi",
    "Sussurra qualcosa all'orecchio di qualcuno facendo in modo che un terzo vi noti",
    "Fai un gioco di mani (tipo morra, sasso-carta-forbice) con qualcuno",
    "Siediti più vicino possibile a una persona specifica per almeno 2 minuti",
    "Riesci a far alzare qualcuno in piedi per un motivo inventato",
    "Fai un selfie con almeno 2 persone",
    "Ruba un oggetto a qualcuno (bicchiere, telefono, accendino) e vedi quanto ci mette a notarlo",
    "Proponi un gioco fisico (braccio di ferro, pollice, ecc.) e fallo partire",
    "Guida qualcuno da qualche parte toccandogli la schiena",
    "Convinci qualcuno a ballare un ballo tipico della tua regione",
    "Resta 5 minuti vicino a qualcuno senza parlare",
    "Offri due drink alla stessa persona (in momenti diversi)",
    "Abbraccia qualcuno per due volte consecutive",
    "Togli un indumento esclamando 'che caldo!'",
    "Accendi la luce durante o dopo il gioco",
    "Indossa un vestito di qualcun altro dopo il gioco",
    "Mantieni eye contact con qualcuno per almeno 15 secondi durante una conversazione",
    "Fai un complimento sulla voce o sugli occhi di qualcuno",
    "Sussurra a qualcuno 'lo so cosa stai facendo' (che sia vero o no)",
    "Avvicinati fisicamente a qualcuno mentre parli fino a meno di 30cm",
    "Tocca il polso di qualcuno mentre gli parli",
    "Dì a qualcuno 'mi fai un effetto strano' con faccia seria",
    "Appoggia la testa sulla spalla di qualcuno per almeno 5 secondi",
    "Fissa qualcuno da lontano finché non ti guarda, poi sorridi e distogli lo sguardo",
    "Dì a qualcuno 'dopo ti devo dire una cosa' e poi quando ti cerca digli 'niente, niente'",
    "Fai un complimento ambiguo tipo 'stasera sei pericoloso/a'",
    "Prendi la mano di qualcuno per 'leggergli la mano' (inventa tutto)",
    "Sussurra a qualcuno 'non fidarti di me'",
    "Proponi di dividere qualcosa da bere/mangiare dallo stesso bicchiere/piatto",
    "Dì a qualcuno 'hai qualcosa qui' e sfioragli il viso per togliere il nulla",
    "Dedica una canzone a qualcuno ad alta voce (anche solo il titolo)",
    "Mordi il collo a qualcuno",
    "Bacia qualcuno random durante un brindisi",
    "Accarezza i capelli a qualcuno mentre parla",
    "Dì a qualcuno 'sei bellissimo/a quando non sai di essere guardato/a'",
    "Soffia nell'orecchio a qualcuno mentre gli sussurri qualcosa",
    "Prendi qualcuno per mano e portalo in un'altra stanza senza spiegare perché",
    "Siediti sulle ginocchia di qualcuno per almeno 10 secondi",
    "Fai un massaggio alle spalle a qualcuno senza che te lo chieda",
    "Disegna qualcosa sulla mano o sul braccio di qualcuno con un dito",
    "Dì a qualcuno 'hai le labbra screpolate, vieni che ti metto il burrocacao' (che tu lo abbia o no)",
    "Annusa il collo di qualcuno e digli 'ma che profumo hai?'",
    "Sfida qualcuno a chi distoglie lo sguardo per primo, a meno di 20cm di distanza",
]

role_counts = {"Lupo": 3, "Mucca": 1, "Pecora": 1, "Cavallo": 1, "Cinghiale": 1, "Aquila": 1}

if "players" not in st.session_state:
    st.session_state.players = []
    st.session_state.current_index = 0
    st.session_state.revealed = False
    st.session_state.timer_end = None

st.title("Pyjama Party: Secret Agenda Game")
st.markdown(
    "Un solo telefono, 6 giocatori: pesca il ruolo e scopri le missioni segrete da completare durante il party."
)

player_names_input = st.text_area(
    "Nomi giocatori (6 separati da virgola)",
    value=", ".join(player_names),
    height=80,
)
custom_player_names = [name.strip() for name in player_names_input.split(",") if name.strip()]
if len(custom_player_names) == 6:
    player_names = custom_player_names
else:
    st.warning("Inserisci esattamente 6 nomi separati da virgola. Verranno usati i nomi di default finché non sono corretti.")

col1, col2 = st.columns([2, 1])
with col1:
    st.subheader("Giocatori:")
    st.write(", ".join(player_names))
    st.subheader("Ruoli:")
    st.write("Mucca, Pecora, Cavallo, Lupo, Cinghiale, Aquila")
with col2:
    st.subheader("Regole")
    st.write(
        "- Il Lupo riceve 3 missioni segrete\n"
        "- Gli altri ruoli ricevono 1 missione\n"
        "- Mostra il ruolo a un giocatore alla volta\n"
        "- Usa il tasto 'Prossimo' per passare al giocatore successivo"
    )

now = datetime.datetime.now()
if st.button("Inizia timer 25 minuti"):
    st.session_state.timer_end = now + datetime.timedelta(minutes=25)
    st.experimental_rerun()
if st.button("Reset timer"):
    st.session_state.timer_end = None

if st.session_state.timer_end:
    remaining = st.session_state.timer_end - now
    if remaining.total_seconds() <= 0:
        st.success("Timer terminato! 25 minuti passati.")
        st.session_state.timer_end = None
    else:
        minutes = remaining.seconds // 60
        seconds = remaining.seconds % 60
        st.info(f"Tempo rimanente: {minutes:02d}:{seconds:02d}")
else:
    st.info("Timer non attivo. Premi 'Inizia timer 25 minuti' quando vuoi partire.")

st.markdown("---")

if st.button("Inizia sessione"):
    shuffled_roles = roles.copy()
    random.shuffle(shuffled_roles)
    players = []
    available_agendas = secret_agendas.copy()
    random.shuffle(available_agendas)

    for name, role in zip(player_names, shuffled_roles):
        count = role_counts[role]
        tasks = [available_agendas.pop() for _ in range(count)]
        players.append({"name": name, "role": role, "tasks": tasks})

    st.session_state.players = players
    st.session_state.current_index = 0
    st.session_state.revealed = False

if not st.session_state.players:
    st.info("Premi 'Inizia sessione' per generare i ruoli e le missioni.")
    st.stop()

current_player = st.session_state.players[st.session_state.current_index]
player_num = st.session_state.current_index + 1
st.header(f"Giocatore {player_num} / 6: {current_player['name']}")

if not st.session_state.revealed:
    st.write("Premi il pulsante per mostrare il ruolo e la missione al giocatore corrente.")
    if st.button("Mostra ruolo e missione"):
        st.session_state.revealed = True
        st.experimental_rerun()
else:
    st.subheader(f"Ruolo: {current_player['role']}")
    st.markdown("**Missioni segrete:**")
    for task in current_player["tasks"]:
        st.write(f"- {task}")

    cols = st.columns(2)
    if cols[0].button("Rivela di nuovo"):
        st.session_state.revealed = False
        st.experimental_rerun()
    if cols[1].button("Prossimo giocatore"):
        if st.session_state.current_index < len(st.session_state.players) - 1:
            st.session_state.current_index += 1
            st.session_state.revealed = False
            st.experimental_rerun()
        else:
            st.success("Hai mostrato tutti i ruoli! Ora godetevi il party e completate le missioni.")

st.markdown("---")
st.write("Consiglio: passate il telefono in modo che ogni giocatore veda il suo ruolo senza farlo vedere agli altri.")
