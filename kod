import random
def powitanie_i_parametry():
    """
    Funkcja powitanie_i_parametry() wita użytkownika i pobiera parametry gry.

    Wyświetla także wiadomość powitalną, pyta użytkownika o wybór trybu gry oraz o
    długość szyfru. Zwraca też wybrane parametry. Gdy gracz poda inny tryb niż 1 lub 2 to gra wyrzuca błąd- trzeba poprawnie wprowadzić poprawne dane

    Zwracane parametry:
    - int tryb_gry: wartość numeru trybu gry (1: dwóch graczy, 2: gra z komputerem)
    - int dlugosc_szyfru: długość szyfru
    
    Przykład użycia funkcji: 
   < Gracz wybiera 1 tryb > 
   < Gracz wpisuje liczbę 4 >
    tryb_gry, dlugosc_szyfru = powitanie_i_parametry()
    print(f"Wybrany tryb gry: {1}")
    print(f"Długość szyfru: {4})
    
    """
    print("Witaj w grze w odgadywanie!")
    while True:
        tryb_gry = int(input("Wybierz tryb gry (1: dwóch graczy, 2: gra z komputerem): "))
        if tryb_gry in [1, 2]:
            break
        else:
            print("Niepoprawny wybór. Wybierz 1 lub 2.")
    
    dlugosc_szyfru = int(input("Podaj liczbę cyfr w szyfrze: "))
    return tryb_gry, dlugosc_szyfru

def tworzenie_kodu(dlugosc_szyfru):
    """
    Tworzenie losowego szyfru o podanej liczbie cyfr.
    Funkcja generuje listę liczb całkowitych, które są cyframi w przedziale od 0 do 9.

    Parametry:
        dlugosc_szyfru (int): Liczba cyfr w generowanym kodzie.

    Zwraca:
        list:
         - Lista liczb całkowitych reprezentujących losowy kod.

    Raises:
        ValueError: Jeśli podano liczbę mniejszą niż 1 jako `dlugosc_szyfru`.

    Przykłady:
        >>> tworzenie_kodu(4)
        [3, 8, 1, 5]  # Przykład szyfru czterocyfrowego
        >>> tworzenie_kodu(6) # Przykład szyfru sześciocyfrowego
        [0, 9, 4, 7, 2, 6]
    """
    if dlugosc_szyfru < 1:
        raise ValueError("Długość kodu musi być większa lub równa 1.")

    return [random.randint(0, 9) for _ in range(dlugosc_szyfru)]
    
def wprowadz_zgadywanie(dlugosc_szyfru):
    """
    Funkcja umożliwia użytkownikowi wprowadzenie szyfru o określonej długości. 

    Przyjmuje wyłącznie cyfry, a liczba wprowadzonych cyfr musi być zgodna z podaną długością. 
    W przypadku błędnego wprowadzenia, funkcja wyświetla komunikat i prosi o ponowne wprowadzenie szyfru.

    Zwracane parametry:
    -int list - lista liczb całkowitych w odgadywanym kodzie

    Przykład użycia:
    # Długość szyfru wynosi 4
    dlugosc_szyfru = 4

    # Wywołanie funkcji
    szyfr = wprowadz_zgadywanie(dlugosc_szyfru)

    print(f"Podano szyfr: {szyfr}")
    """
    while True:
        strona_zgadywania = input(f"Wprowadź swój szyfr ({dlugosc_szyfru} cyfrowy): ")
        if len(strona_zgadywania) == dlugosc_szyfru and strona_zgadywania.isdigit():
            return [int(cyfra) for cyfra in strona_zgadywania]
        print(f"Proszę wprowadzić szyfr dokładnie {dlugosc_szyfru} cyfrowy.")

def ocena_zgadywanie(kod, zgadywanie):
    """
    Funkcja sprawdza, ile cyfr w podanym przez gracza szyfrze znajduje się na właściwych miejscach,
    oraz ile cyfr jest obecnych w szyfrze, ale na niewłaściwych miejscach.

    Parametry:
    kod (list[int]): Lista cyfr, które stanowią prawdziwy kod do odgadnięcia.
    strona_zgadywania (list[int]): Lista cyfr próby zgadywania gracza.

    Zwraca:
    tuple:
        - miejsca_poprawne (int): Liczba cyfr, które gracz zgadł na właściwych miejscach.
        - cyfry_poprawne (int): Liczba cyfr, które gracz zgadł, ale są na niewłaściwych miejscach.

    Przykład użycia funkcji:
    >>> ocena_zgadywanie([1, 2, 3, 4], [1, 5, 3, 4])
    (2, 2)

    Wyjaśnienie otrzymanego wyniku:
    - miejsca_poprawne: 2 (pierwsza i czwarta cyfra: 1 i 4)
    - cyfry_poprawne: 2 (trzecia cyfra 3 oraz druga cyfra 5 znajdują się w kodzie, ale na innych miejscach w szyfrze)
    """
    miejsca_poprawne = sum(1 for i in range(len(kod)) if kod[i] == zgadywanie[i])
    cyfry_poprawne = sum(min(kod.count(cyfra), zgadywanie.count(cyfra)) for cyfra in set(zgadywanie)) - miejsca_poprawne
    return miejsca_poprawne, cyfry_poprawne
   

def tryb_dla_graczy(dlugosc_szyfru):
    """
    Funkcja służy do wprowadzenia kodu przez pierwszego gracza.

    Parametry:
    dlugosc_szyfru (int): Długość kodu, który ma wprowadzić gracz.

    Zwraca:
    list: Lista cyfr, które zostały wprowadzone przez gracza.

    Przykład użycia funkcji: 
    
    dlugosc_szyfru = 4
    kod = tryb_dla_graczy(dlugosc_szyfru)
    print(f"Gracz pierwszy wprowadził kod: {kod}")
    """
    from getpass import getpass
    print(f"Gracz pierwszy: Wprowadź kod ({dlugosc_szyfru} cyfrowy, zapisz go lub zapamiętaj): ", end="")
    kod = [int(cyfra) for cyfra in getpass("").strip()]
    return kod
    

def tryb_komputerowy(dlugosc_szyfru):
    """
    Generuje kod w trybie  gry z komputerem.

    Funkcja symuluje generowanie kodu przez komputer, a następnie zwraca ten kod.
    
    Parametry:
    dlugosc_szyfru (int): liczba określająca długość szyfru, który ma zostać wygenerowany.

    Zwraca:
    liste: lista liczb całkowitych reprezentujących wygenerowany kod.
    """
    print("Kod wygenerowany przez komputer.")
    return tworzenie_kodu(dlugosc_szyfru)
    
def przebieg_gry(tryb_gry, dlugosc_szyfru):
    """
    Gracz zgaduje kod wprowadzony przez drugiego gracza lub wygenerowany przez komputer.

    Funkcja odpowiada za przebieg gry, od momentu wyboru kodu (w zależności od trybu gry z komputerem lub gry dwóch uczestników ) po zgadywanie kodu przez gracza. 
    Każda próba gracza jest oceniana, a gra kończy się, gdy kod zostanie poprawnie odgadnięty.

    Parametry:
        tryb_gry (int): Tryb gry, gdzie:
            - `1` oznacza grę dwóch graczy (jednen gracz wprowadza wymyślony szyfr, a drugi gracz zgaduje kod ),
            - `2` oznacza grę z komputerem (kod generowany losowo przez komputer).
        dlugosc_szyfru (int): Liczba cyfr w kodzie do odgadnięcia.

    Raises:
        ValueError: Jeśli `tryb_gry` nie jest równy 1 lub 2.
        ValueError: Jeśli `dlugosc_szyfru` jest mniejsze niż 1.

    Zwraca:
        None: Funkcja nie zwraca wartości, wyłącznie wyświetla informacje o przebiegu gry.

    Przykłady:
        >>> przebieg_gry(1, 4)
        W grze dwóch graczy gracz pierwszy wprowadza kod.
        Gracz drugi zgaduje kod i otrzymuje wskazówki, aż do poprawnego odgadnięcia.
        >>> przebieg_gry(2, 3)
        Komputer generuje kod o długości 3 cyfr. Gracz zgaduje kod, a gra kończy się sukcesem po odgadnięciu szyfru.

    """
    if tryb_gry not in (1, 2):
        raise ValueError("Niepoprawny tryb gry. Wybierz 1 (gra dwóch graczy) lub 2 (gra z komputerem).")
    
    if tryb_gry == 1:
        kod = tryb_dla_graczy(dlugosc_szyfru)
    else:
        kod = tryb_komputerowy(dlugosc_szyfru)

    liczba_prob = 0  

    while True:
        zgadywanie = wprowadz_zgadywanie(dlugosc_szyfru) 
        liczba_prob += 1 
        miejsca_poprawne, cyfry_poprawne = ocena_zgadywanie(kod, zgadywanie)  

    
        print(f"Cyfry na właściwych miejscach: {miejsca_poprawne}")
        print(f"Cyfry w kodzie, ale nie na swoich miejscach: {cyfry_poprawne}")

    
        if miejsca_poprawne == dlugosc_szyfru:
            print(f"Gratulacje! Szyfr został złamany w {liczba_prob} próbach.")
            break

def main():
    """
    Główna funkcja programu, która uruchamia grę.

    Funkcja ta:
    - Wywołuje funkcję powitanie_i_parametry(), aby pobrać tryb gry oraz liczbę cyfr w szyfrze od gracza.
    - Przekazuje te dane do funkcji przebieg_gry(), która zarządza całą logiką rozgrywki w odgadywanie.

    Zmienne:
    - tryb_gry (int): Tryb gry wybrany przez gracza (1: dwóch graczy, 2: gra z komputerem).
    - dlugosc_szyfru (int): Długość szyfru (liczba cyfr w szyfrze) wybrana przez gracza.

    Przykład:
    >>> main()
    """
    tryb_gry, dlugosc_szyfru = powitanie_i_parametry() 
    przebieg_gry(tryb_gry, dlugosc_szyfru) 
    

if __name__ == "__main__":
    main() 
