from tabulate import tabulate

# Begin met 4 dictionaries (personen) met naam, leeftijd en woonplaats
personen = [
    {"naam": "Jan", "leeftijd": 28, "woonplaats": "Amsterdam"},
    {"naam": "Lisa", "leeftijd": 34, "woonplaats": "Rotterdam"},
    {"naam": "Ahmed", "leeftijd": 22, "woonplaats": "Utrecht"},
    {"naam": "Sophie", "leeftijd": 40, "woonplaats": "Den Haag"}
]


# Functie om alle items in een tabulate-tabel te tonen
def toon_items(lijst):
    headers = ["#", "Naam", "Leeftijd", "Woonplaats"]
    tabel = []
    for index, persoon in enumerate(lijst, start=1):
        tabel.append([index, persoon["naam"], persoon["leeftijd"], persoon["woonplaats"]])

    print(tabulate(tabel, headers, tablefmt="grid"))


# Functie om een nieuw item (persoon) toe te voegen aan de lijst
def voeg_items_toe(lijst, naam, leeftijd, woonplaats):
    nieuwe_persoon = {"naam": naam, "leeftijd": leeftijd, "woonplaats": woonplaats}
    lijst.append(nieuwe_persoon)
    print(f"{naam} is toegevoegd aan de lijst.")


# Functie om een item te verwijderen op basis van index
def verwijder_item(lijst, index):
    try:
        verwijderde_persoon = lijst.pop(index - 1)
        print(f"{verwijderde_persoon['naam']} is verwijderd uit de lijst.")
    except IndexError:
        print(f"Fout: Er is geen persoon met index {index}.")


# Test de functies
print("Oorspronkelijke lijst:")
toon_items(personen)

print("\nVoeg een nieuwe persoon toe:")
voeg_items_toe(personen, "Karin", 25, "Leiden")

print("\nLijst na toevoegen:")
toon_items(personen)

print("\nVerwijder het 2e item (Lisa):")
verwijder_item(personen, 3)

print("\nLijst na verwijderen:")
toon_items(personen)
