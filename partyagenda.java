import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class PartyAgendaGame {
    private static final String[] ROLES = {
        "Mucca",
        "Pecora",
        "Cavallo",
        "Lupo",
        "Cinghiale",
        "Aquila"
    };

    private static final String[] AGENDAS = {
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
        "Togli un indumento esclamando \"che caldo!\"",
        "Accendi la luce durante o dopo il gioco",
        "Indossa un vestito di qualcun altro dopo il gioco",
        "Mantieni eye contact con qualcuno per almeno 15 secondi durante una conversazione",
        "Fai un complimento sulla voce o sugli occhi di qualcuno",
        "Sussurra a qualcuno \"lo so cosa stai facendo\" (che sia vero o no)",
        "Avvicinati fisicamente a qualcuno mentre parli fino a meno di 30cm",
        "Tocca il polso di qualcuno mentre gli parli",
        "Dì a qualcuno \"mi fai un effetto strano\" con faccia seria",
        "Appoggia la testa sulla spalla di qualcuno per almeno 5 secondi",
        "Fissa qualcuno da lontano finché non ti guarda, poi sorridi e distogli lo sguardo",
        "Dì a qualcuno \"dopo ti devo dire una cosa\" e poi quando ti cerca digli \"niente, niente\"",
        "Fai un complimento ambiguo tipo \"stasera sei pericoloso/a\"",
        "Prendi la mano di qualcuno per \"leggergli la mano\" (inventa tutto)",
        "Sussurra a qualcuno \"non fidarti di me\"",
        "Proponi di dividere qualcosa da bere/mangiare dallo stesso bicchiere/piatto",
        "Dì a qualcuno \"hai qualcosa qui\" e sfioragli il viso per togliere il nulla",
        "Dedica una canzone a qualcuno ad alta voce (anche solo il titolo)",
        "Mordi il collo a qualcuno",
        "Bacia qualcuno random durante un brindisi",
        "Accarezza i capelli a qualcuno mentre parla",
        "Dì a qualcuno \"sei bellissimo/a quando non sai di essere guardato/a\"",
        "Soffia nell'orecchio a qualcuno mentre gli sussurri qualcosa",
        "Prendi qualcuno per mano e portalo in un'altra stanza senza spiegare perché",
        "Siediti sulle ginocchia di qualcuno per almeno 10 secondi",
        "Fai un massaggio alle spalle a qualcuno senza che te lo chieda",
        "Disegna qualcosa sulla mano o sul braccio di qualcuno con un dito",
        "Dì a qualcuno \"hai le labbra screpolate, vieni che ti metto il burrocacao\" (che tu lo abbia o no)",
        "Annusa il collo di qualcuno e digli \"ma che profumo hai?\"",
        "Sfida qualcuno a chi distoglie lo sguardo per primo, a meno di 20cm di distanza"
    };

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("=== Party Agenda Game ===");
        System.out.println("6 giocatori, un unico telefono. Ogni persona rivela il suo ruolo in segreto.");
        System.out.println();

        List<String> players = askPlayerNames(scanner);
        List<String> roles = shuffleRoles();
        List<List<String>> assignments = assignAgendas(roles);

        System.out.println();
        System.out.println("Tutte le impostazioni sono pronte. Passa il telefono al giocatore #1.");
        System.out.println("Premi INVIO per iniziare la rivelazione dei ruoli uno a uno.");
        scanner.nextLine();

        for (int i = 0; i < players.size(); i++) {
            clearScreen();
            System.out.printf("Giocatore %d: %s%n", i + 1, players.get(i));
            System.out.printf("Ruolo: %s%n", roles.get(i));
            System.out.println("Missioni segrete:");

            List<String> playerAgendas = assignments.get(i);
            for (int j = 0; j < playerAgendas.size(); j++) {
                System.out.printf("  %d) %s%n", j + 1, playerAgendas.get(j));
            }

            if (i < players.size() - 1) {
                System.out.println();
                System.out.println("Passa il telefono al prossimo giocatore e premi INVIO.");
                scanner.nextLine();
            }
        }

        System.out.println();
        System.out.println("Tutti i ruoli e le missioni sono stati assegnati. Buon divertimento al party!");
        scanner.close();
    }

    private static List<String> askPlayerNames(Scanner scanner) {
        List<String> players = new ArrayList<>();
        System.out.println("Inserisci i nomi dei 6 giocatori (premi INVIO per usare nomi di esempio):");
        for (int i = 1; i <= 6; i++) {
            System.out.printf("Giocatore %d: ", i);
            String name = scanner.nextLine().trim();
            if (name.isEmpty()) {
                name = "Giocatore " + i;
            }
            players.add(name);
        }
        return players;
    }

    private static List<String> shuffleRoles() {
        List<String> roles = new ArrayList<>();
        Collections.addAll(roles, ROLES);
        Collections.shuffle(roles, new Random());
        return roles;
    }

    private static List<List<String>> assignAgendas(List<String> roles) {
        List<String> agendas = new ArrayList<>();
        Collections.addAll(agendas, AGENDAS);
        Collections.shuffle(agendas, new Random());

        List<List<String>> assignments = new ArrayList<>();
        int agendaIndex = 0;

        for (String role : roles) {
            int count = role.equals("Lupo") ? 3 : 1;
            List<String> playerAgendas = new ArrayList<>();
            for (int j = 0; j < count; j++) {
                if (agendaIndex >= agendas.size()) {
                    agendaIndex = 0; // in caso rimangano poche missioni, tornare all'inizio
                }
                playerAgendas.add(agendas.get(agendaIndex++));
            }
            assignments.add(playerAgendas);
        }

        return assignments;
    }

    private static void clearScreen() {
        for (int i = 0; i < 50; i++) {
            System.out.println();
        }
    }
}
