import datetime
import random
import streamlit as st

st.set_page_config(
    page_title="Pyjama Party Game",
    page_icon="🎉",
    layout="centered",
)

player_names = ["Eleonora", "Eugenio", "Maurizio", "Luca", "Natalia", "Sophie"]
roles = ["Mucca", "Pecora", "Cacallo", "Lupo", "Cinghiale", "Aquila"]
secret_agendas = [
    "19. Balla (anche solo un accenno) con qualcuno per almeno 10 secondi",
    "20. Riesci a farti offrire da bere da qualcuno",
    "21. Tieni un braccio intorno alle spalle di qualcuno per almeno 20 secondi",
    "22. Sussurra qualcosa all'orecchio di qualcuno facendo in modo che un terzo vi noti",
    "23. Fai un gioco di mani (tipo morra, sasso-carta-forbice) con qualcuno",
    "24. Siediti più vicino possibile a una persona specifica per almeno 2 minuti",
    "25. Riesci a far alzare qualcuno in piedi per un motivo inventato",
    "26. Fai un selfie con almeno 2 persone",
    "27. Ruba un oggetto a qualcuno (bicchiere, telefono, accendino) e vedi quanto ci mette a notarlo",
    "28. Proponi un gioco fisico (braccio di ferro, pollice, ecc.) e fallo partire",
    "29. Guida qualcuno da qualche parte toccandogli la schiena",
    "30. Convinci qualcuno a ballare un ballo tipico della tua regione",
    "31. Resta 5 minuti vicino a qualcuno senza parlare",
    "32. Offri due drink alla stessa persona (in momenti diversi)",
    "33. Abbraccia qualcuno per due volte consecutive",
    "34. Togli un indumento esclamando 'che caldo!'",
    "35. Accendi la luce durante o dopo il gioco",
    "36. Indossa un vestito di qualcun altro dopo il gioco",
    "37. Mantieni eye contact con qualcuno per almeno 15 secondi durante una conversazione",
    "38. Fai un complimento sulla voce o sugli occhi di qualcuno",
    "39. Sussurra a qualcuno 'lo so cosa stai facendo' (che sia vero o no)",
    "40. Avvicinati fisicamente a qualcuno mentre parli fino a meno di 30cm",
    "41. Tocca il polso di qualcuno mentre gli parli",
    "42. Dì a qualcuno 'mi fai un effetto strano' con faccia seria",
    "43. Appoggia la testa sulla spalla di qualcuno per almeno 5 secondi",
    "44. Fissa qualcuno da lontano finché non ti guarda, poi sorridi e distogli lo sguardo",
    "45. Dì a qualcuno 'dopo ti devo dire una cosa' e poi quando ti cerca digli 'niente, niente'",
    "46. Fai un complimento ambiguo tipo 'stasera sei pericoloso/a'",
    "47. Prendi la mano di qualcuno per 'leggergli la mano' (inventa tutto)",
    "48. Sussurra a qualcuno 'non fidarti di me'",
    "49. Proponi di dividere qualcosa da bere/mangiare dallo stesso bicchiere/piatto",
    "50. Dì a qualcuno 'hai qualcosa qui' e sfioragli il viso per togliere il nulla",
    "51. Dedica una canzone a qualcuno ad alta voce (anche solo il titolo)",
    "52. Mordi il collo a qualcuno",
    "53. Bacia qualcuno random durante un brindisi",
    "54. Accarezza i capelli a qualcuno mentre parla",
    "55. Dì a qualcuno 'sei bellissimo/a quando non sai di essere guardato/a'",
    "56. Soffia nell'orecchio a qualcuno mentre gli sussurri qualcosa",
    "57. Prendi qualcuno per mano e portalo in un'altra stanza senza spiegare perché",
    "58. Siediti sulle ginocchia di qualcuno per almeno 10 secondi",
    "59. Fai un massaggio alle spalle a qualcuno senza che te lo chieda",
    "60. Disegna qualcosa sulla mano o sul braccio di qualcuno con un dito",
    "61. Dì a qualcuno 'hai le labbra screpolate, vieni che ti metto il burrocacao' (che tu lo abbia o no)",
    "62. Annusa il collo di qualcuno e digli 'ma che profumo hai?'",
    "63. Sfida qualcuno a chi distoglie lo sguardo per primo, a meno di 20cm di distanza",
]

role_counts = {"Lupo": 3, "Mucca": 1, "Pecora": 1, "Cacallo": 1, "Cinghiale": 1, "Aquila": 1}

if "players" not in st.session_state:
    st.session_state.players = []
    st.session_state.current_index = 0
    st.session_state.revealed = False
    st.session_state.timer_end = None

st.title("Pyjama Party: Secret Agenda Game")
st.markdown(
    "Un solo telefono, 6 giocatori: pesca il ruolo e scopri le missioni segrete da completare durante il party."
)

col1, col2 = st.columns([2, 1])
with col1:
    st.subheader("Giocatori:")
    st.write(", ".join(player_names))
    st.subheader("Ruoli:")
    st.write("Mucca, Pecora, Cacallo, Lupo, Cinghiale, Aquila")
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
