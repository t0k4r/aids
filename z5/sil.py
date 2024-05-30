def maksymalna_wartosc(przedmioty, pojemnosc_plecaka):

  n = len(przedmioty)
  wartosci_max = 0
  wagi_max = 0
  wybrane_przedmioty = []

  # Generowanie wszystkich możliwych kombinacji przedmiotów
  for maska in range(2**n):
    waga_kombinacji = 0
    wartosc_kombinacji = 0
    kombinacja_przedmiotow = []
    for i in range(n):
        #czy i-ty przedmiot wybrany w konfiguracji
      if (maska & (1 << i)) > 0:
        waga_kombinacji += przedmioty[i][0]
        wartosc_kombinacji += przedmioty[i][1]
        kombinacja_przedmiotow.append(przedmioty[i])

    # Sprawdzenie, czy waga kombinacji mieści się w limicie plecaka
    if waga_kombinacji <= pojemnosc_plecaka:
      # Aktualizacja wartości maksymalnej i listy wybranych przedmiotów
      if wartosc_kombinacji > wartosci_max:
        wartosci_max = wartosc_kombinacji
        wagi_max = waga_kombinacji
        wybrane_przedmioty = kombinacja_przedmiotow

  return wagi_max, wartosci_max, wybrane_przedmioty

# Pobranie danych od użytkownika
# n, pojemnosc_plecaka = map(int, input("Podaj liczbę przedmiotów i pojemność plecaka (n b): ").split())

# przedmioty = []
# for i in range(n):
#   r, w = map(int, input(f"Podaj rozmiar i wartość przedmiotu {i+1} (r w): ").split())
#   przedmioty.append((r, w))


# cap=7
# items= [(3,5),(1,2),(4,8),(5,9),(2,3),(3,6),(4,7),(2,4)]
items = [(3,5),(1,2),(4,8),(5,9), (2,3)]
pojemnosc_plecaka = 7
przedmioty = [(3,5),(1,2),(4,8),(5,9), (2,3)]


waga_max, wartosc_max, wybrane_przedmioty = maksymalna_wartosc(przedmioty, pojemnosc_plecaka)

# print(f"Maksymalna waga: {waga_max}")
# print(f"Maksymalna wartość: {wartosc_max}")
# print("Wybrane przedmioty:")
# for przedmiot in wybrane_przedmioty:
#   print(f"Rozmiar: {przedmiot[0]}, Wartość: {przedmiot[1]}")