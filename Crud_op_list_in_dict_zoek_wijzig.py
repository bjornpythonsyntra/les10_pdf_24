from tabulate import tabulate

# Definieer de lijst van programmeurs met gemeentes uit Belgisch Limburg
lijst_programmeurs = [
    {"naam": "Jan", "gemeente": "Hasselt", "uurloon": 50, "programmeertalen": ["Python", "Java"]},
    {"naam": "Emma", "gemeente": "Genk", "uurloon": 60, "programmeertalen": ["C#", "JavaScript", "SQL"]},
    {"naam": "Lars", "gemeente": "Maasmechelen", "uurloon": 55, "programmeertalen": ["Ruby", "PHP"]},
    {"naam": "Sophie", "gemeente": "Sint-Truiden", "uurloon": 48, "programmeertalen": ["Python", "Go", "Rust"]},
    {"naam": "Tom", "gemeente": "Tongeren", "uurloon": 52, "programmeertalen": ["Swift", "Objective-C"]},
    {"naam": "Lisa", "gemeente": "Beringen", "uurloon": 58, "programmeertalen": ["Kotlin", "C++", "Perl"]},
    {"naam": "Kevin", "gemeente": "Lommel", "uurloon": 47, "programmeertalen": ["Java", "Scala", "Python"]}
]


# Functie om een programmeertaal toe te voegen aan een programmeur
def voeg_programmeertaal_toe(naam, nieuwe_taal):
    for programmeur in lijst_programmeurs:
        if programmeur["naam"].lower() == naam.lower():
            if nieuwe_taal not in programmeur["programmeertalen"]:
                programmeur["programmeertalen"].append(nieuwe_taal)
                print(f"{nieuwe_taal} is toegevoegd aan {naam}'s programmeertalen.")
            else:
                print(f"{naam} kent al {nieuwe_taal}.")
            return
    print(f"Programmeur met de naam {naam} niet gevonden.")


# Functie om een programmeertaal te verwijderen van een programmeur
def verwijder_programmeertaal(naam, taal_om_te_verwijderen):
    for programmeur in lijst_programmeurs:
        if programmeur["naam"].lower() == naam.lower():
            if taal_om_te_verwijderen in programmeur["programmeertalen"]:
                programmeur["programmeertalen"].remove(taal_om_te_verwijderen)
                print(f"{taal_om_te_verwijderen} is verwijderd van {naam}'s programmeertalen.")
            else:
                print(f"{naam} kent geen {taal_om_te_verwijderen}.")
            return
    print(f"Programmeur met de naam {naam} niet gevonden.")


# Functie om het uurloon van een programmeur aan te passen
def pas_uurloon_aan(naam, nieuw_uurloon):
    for programmeur in lijst_programmeurs:
        if programmeur["naam"].lower() == naam.lower():
            programmeur["uurloon"] = nieuw_uurloon
            print(f"Het uurloon van {naam} is aangepast naar {nieuw_uurloon} EUR.")
            return
    print(f"Programmeur met de naam {naam} niet gevonden.")


# Functie om programmeurs te tonen in een tabel
def toon_programmeurs():
    table_data = [
        [p['naam'], p['gemeente'], p['uurloon'], ', '.join(p['programmeertalen'])]
        for p in lijst_programmeurs
    ]
    headers = ["Naam", "Gemeente", "Uurloon (EUR)", "Programmeertalen"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))


# Functie om programmeurs te zoeken op programmeertaal
def zoek_programmeurs_op_taal(taal):
    programmeurs_met_taal = [
        p for p in lijst_programmeurs if taal in p["programmeertalen"]
    ]

    if not programmeurs_met_taal:
        print(f"Geen programmeurs gevonden die de programmeertaal '{taal}' beheersen.")
        return

    # Toon de programmeurs in een tabel
    table_data = [
        [p['naam'], p['gemeente'], p['uurloon'], ', '.join(p['programmeertalen'])]
        for p in programmeurs_met_taal
    ]
    headers = ["Naam", "Gemeente", "Uurloon (EUR)", "Programmeertalen"]
    print(f"\nProgrammeurs die de programmeertaal '{taal}' beheersen:")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))


# Toon de oorspronkelijke lijst van programmeurs
print("Oorspronkelijke lijst van programmeurs:")
toon_programmeurs()

# Vraag de gebruiker om een programmeertaal om naar te zoeken
taal_om_te_zoeken = input("\nVoer een programmeertaal in om programmeurs te zoeken: ")

# Zoek en toon de programmeurs die deze programmeertaal beheersen
zoek_programmeurs_op_taal(taal_om_te_zoeken)

# Vraag naar de naam van de programmeur en het nieuwe uurloon
naam_voor_uurloon = input("\nVoer de naam van de programmeur in om het uurloon aan te passen: ")
nieuw_uurloon = float(input("Voer het nieuwe uurloon in (in EUR): "))

# Pas het uurloon aan
pas_uurloon_aan(naam_voor_uurloon, nieuw_uurloon)

# Toon de bijgewerkte lijst van programmeurs
print("\nBijgewerkte lijst van programmeurs:")
toon_programmeurs()
