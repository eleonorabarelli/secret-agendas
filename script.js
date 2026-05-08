const ROLES = [
  'Mucca',
  'Pecora',
  'Cavallo',
  'Lupo',
  'Cinghiale',
  'Aquila'
];

const AGENDAS = [
  'Balla (anche solo un accenno) con qualcuno per almeno 10 secondi',
  'Riesci a farti offrire da bere da qualcuno',
  'Tieni un braccio intorno alle spalle di qualcuno per almeno 20 secondi',
  'Sussurra qualcosa all\'orecchio di qualcuno facendo in modo che un terzo vi noti',
  'Fai un gioco di mani (tipo morra, sasso-carta-forbice) con qualcuno',
  'Siediti più vicino possibile a una persona specifica per almeno 2 minuti',
  'Riesci a far alzare qualcuno in piedi per un motivo inventato',
  'Fai un selfie con almeno 2 persone',
  'Ruba un oggetto a qualcuno (bicchiere, telefono, accendino) e vedi quanto ci mette a notarlo',
  'Proponi un gioco fisico (braccio di ferro, pollice, ecc.) e fallo partire',
  'Guida qualcuno da qualche parte toccandogli la schiena',
  'Convinci qualcuno a ballare un ballo tipico della tua regione',
  'Resta 5 minuti vicino a qualcuno senza parlare',
  'Offri due drink alla stessa persona (in momenti diversi)',
  'Abbraccia qualcuno per due volte consecutive',
  'Togli un indumento esclamando "che caldo!"',
  'Accendi la luce durante o dopo il gioco',
  'Indossa un vestito di qualcun altro dopo il gioco',
  'Mantieni eye contact con qualcuno per almeno 15 secondi durante una conversazione',
  'Fai un complimento sulla voce o sugli occhi di qualcuno',
  'Sussurra a qualcuno "lo so cosa stai facendo" (che sia vero o no)',
  'Avvicinati fisicamente a qualcuno mentre parli fino a meno di 30cm',
  'Tocca il polso di qualcuno mentre gli parli',
  'Dì a qualcuno "mi fai un effetto strano" con faccia seria',
  'Appoggia la testa sulla spalla di qualcuno per almeno 5 secondi',
  'Fissa qualcuno da lontano finché non ti guarda, poi sorridi e distogli lo sguardo',
  'Dì a qualcuno "dopo ti devo dire una cosa" e poi quando ti cerca digli "niente, niente"',
  'Fai un complimento ambiguo tipo "stasera sei pericoloso/a"',
  'Prendi la mano di qualcuno per "leggergli la mano" (inventa tutto)',
  'Sussurra a qualcuno "non fidarti di me"',
  'Proponi di dividere qualcosa da bere/mangiare dallo stesso bicchiere/piatto',
  'Dì a qualcuno "hai qualcosa qui" e sfioragli il viso per togliere il nulla',
  'Dedica una canzone a qualcuno ad alta voce (anche solo il titolo)',
  'Mordi il collo a qualcuno',
  'Bacia qualcuno random durante un brindisi',
  'Accarezza i capelli a qualcuno mentre parla',
  'Dì a qualcuno "sei bellissimo/a quando non sai di essere guardato/a"',
  'Soffia nell\'orecchio a qualcuno mentre gli sussurri qualcosa',
  'Prendi qualcuno per mano e portalo in un\'altra stanza senza spiegare perché',
  'Siediti sulle ginocchia di qualcuno per almeno 10 secondi',
  'Fai un massaggio alle spalle a qualcuno senza che te lo chieda',
  'Disegna qualcosa sulla mano o sul braccio di qualcuno con un dito',
  'Dì a qualcuno "hai le labbra screpolate, vieni che ti metto il burrocacao" (che tu lo abbia o no)',
  'Annusa il collo di qualcuno e digli "ma che profumo hai?"',
  'Sfida qualcuno a chi distoglie lo sguardo per primo, a meno di 20cm di distanza'
];

const form = document.getElementById('player-form');
const setupSection = document.getElementById('setup-section');
const revealSection = document.getElementById('reveal-section');
const currentPlayerNumber = document.getElementById('current-player-number');
const playerNameLabel = document.getElementById('player-name');
const playerRoleLabel = document.getElementById('player-role');
const agendasList = document.getElementById('agendas-list');
const nextButton = document.getElementById('next-button');
const restartButton = document.getElementById('restart-button');
const unlockButton = document.getElementById('unlock-button');
const lockScreen = document.getElementById('lock-screen');
const revealContent = document.getElementById('reveal-content');
const nextPlayerName = document.getElementById('next-player-name');

let players = [];
let roles = [];
let assignments = [];
let currentIndex = 0;
let isUnlocked = false;

form.addEventListener('submit', event => {
  event.preventDefault();
  players = Array.from(form.querySelectorAll('input[name="player"]')).map((input, index) => input.value.trim() || `Giocatore ${index + 1}`);
  if (players.length !== 6) {
    return;
  }
  startSession();
});

unlockButton.addEventListener('click', () => {
  isUnlocked = true;
  lockScreen.classList.add('hidden');
  revealContent.classList.remove('hidden');
  nextButton.classList.remove('hidden');
});

nextButton.addEventListener('click', () => {
  currentIndex += 1;
  if (currentIndex >= players.length) {
    showFinalScreen();
  } else {
    isUnlocked = false;
    renderPlayerReveal();
  }
});

restartButton.addEventListener('click', () => {
  resetGame();
});

function startSession() {
  roles = shuffle([...ROLES]);
  assignments = assignAgendas(roles);
  currentIndex = 0;
  setupSection.classList.add('hidden');
  revealSection.classList.remove('hidden');
  restartButton.classList.add('hidden');
  nextButton.classList.add('hidden');
  renderPlayerReveal();
}

function renderPlayerReveal() {
  currentPlayerNumber.textContent = currentIndex + 1;
  nextPlayerName.textContent = players[currentIndex];
  playerNameLabel.textContent = `Nome: ${players[currentIndex]}`;
  playerRoleLabel.textContent = `Ruolo: ${roles[currentIndex]}`;
  agendasList.innerHTML = '';
  assignments[currentIndex].forEach((agenda, index) => {
    const item = document.createElement('li');
    item.textContent = `${index + 1}. ${agenda}`;
    agendasList.appendChild(item);
  });
  if (currentIndex === players.length - 1) {
    nextButton.textContent = 'Fine sessione';
  } else {
    nextButton.textContent = 'Passa al prossimo';
  }
  lockScreen.classList.remove('hidden');
  revealContent.classList.add('hidden');
  nextButton.classList.add('hidden');
}

function showFinalScreen() {
  currentPlayerNumber.textContent = players.length;
  playerNameLabel.textContent = 'Tutti i ruoli sono stati assegnati.';
  playerRoleLabel.textContent = 'Buon divertimento al party!';
  agendasList.innerHTML = '<li>Hai finito. Ora divertitevi e cercate di completare le missioni.</li>';
  lockScreen.classList.add('hidden');
  revealContent.classList.remove('hidden');
  nextButton.classList.add('hidden');
  restartButton.classList.remove('hidden');
}

function resetGame() {
  setupSection.classList.remove('hidden');
  revealSection.classList.add('hidden');
  form.reset();
  const inputs = form.querySelectorAll('input[type="text"]');
  inputs.forEach((input, index) => {
    input.value = `Giocatore ${index + 1}`;
  });
}

function assignAgendas(rolesList) {
  const shuffledAgendas = shuffle([...AGENDAS]);
  const result = [];
  let index = 0;

  rolesList.forEach(role => {
    const count = role === 'Lupo' ? 3 : 1;
    result.push(shuffledAgendas.slice(index, index + count));
    index += count;
  });

  return result;
}

function shuffle(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
}
