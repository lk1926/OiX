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



