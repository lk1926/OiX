X = "X"
O = "O"
puste = " "
remis = "REMIS"
liczba_pol = 9

def instrukcja_gry():
    """Instrukcję gry."""  
    print(
    """
    Witaj w grze 'Kółko i krzyżyk'!!! 

    Swoje posunięcie wskażesz poprzez wprowadzenie liczby z zakresu 0 - 8.
    Liczba ta odpowiada pozycji na planszy zgodnie z poniższym schematem:
    
                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8

    """
    )
    
def tak_czy_nie(pytanie):
    """Pytanie kto chce pierwszy zacząć."""
    odpowiedz = None
    while odpowiedz not in ("t", "n"):
        odpowiedz = input(pytanie).lower()
    return odpowiedz

def podaj_liczbe(pytanie, low, high):
    """Ppodanie liczby z odpowiedniego zakresu."""
    odpowiedz = None
    while odpowiedz not in range(low, high):
        odpowiedz = int(input(pytanie))
    return odpowiedz

def pierwszy_ruch():
    """Czy pierwszy ruch należy do gracza, czy do komputera."""
    pierwszy = tak_czy_nie("Czy chcesz mieć prawo do pierwszego ruchu? (t/n): ")
    if pierwszy == "t":
        print("\nWięc pierwszy ruch należy do Ciebie.")
        czlowiek = X
        computer = O
    else:
        print("\nJa wykonuję pierwszy ruch.")
        computer = X
        czlowiek = O
    return computer, czlowiek


def nowa_plansza():
    """Nowa plansza gry."""
    plansza = []
    for pole in range(liczba_pol):
        plansza.append(puste)
    return plansza

def wyswietlona_plansz(plansza):
    """Wyświetla planszę gry na ekranie."""
    print("\n\t", plansza[0], "|", plansza[1], "|", plansza[2])
    print("\t", "---------")
    print("\t", plansza[3], "|", plansza[4], "|", plansza[5])
    print("\t", "---------")
    print("\t", plansza[6], "|", plansza[7], "|", plansza[8], "\n")


def prawidlowy_ruch(plansza):
    """Lista prawidłowych ruchów."""
    lista_ruchow = []
    for pole in range(liczba_pol):
        if plansza[pole] == puste:
            lista_ruchow.append(pole)
    return lista_ruchow

def zwyciezca(plansza):
    """Ustala zwycięzcę gry."""
    jak_wygrac = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    
    for row in jak_wygrac:
        if plansza[row[0]] == plansza[row[1]] == plansza[row[2]] != puste:
            zwyciezca = plansza[row[0]]
            return zwyciezca

    if puste not in plansza:
        return remis

    return None

def ruch_czlowieka(plansza, czlowiek):
    """Odczytuje ruch człowieka."""  
    legal = prawidlowy_ruch(plansza)
    ruch = None
    while ruch not in legal:
        ruch = podaj_liczbe("Jaki będzie Twój ruch? (0 - 8):", 0, liczba_pol)
        if ruch not in legal:
            print("\nTo pole jest już zajęte... Wybierz inne.\n")
    print("Znakomicie...")
    return ruch


def ruch_kompa(plansza, computer, czlowiek):
    """Ruch komputera."""
    plansza = plansza[:]
    najlepszy_ruch = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print("Wybieram pole numer", end=" ")
    
    for ruch in prawidlowy_ruch(plansza):
        plansza[ruch] = computer
        if zwyciezca(plansza) == computer:
            print(ruch)
            return ruch
        plansza[ruch] = puste

    for ruch in prawidlowy_ruch(plansza):
        plansza[ruch] = czlowiek
        if zwyciezca(plansza) == czlowiek:
            print(ruch)
            return ruch
        plansza[ruch] = puste


    for ruch in najlepszy_ruch:
        if ruch in prawidlowy_ruch(plansza):
            print(ruch)
            return ruch


