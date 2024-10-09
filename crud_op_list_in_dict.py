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

# Functie om de programmeurs te tonen in een tabel
def toon_programmeurs():
    table_data = [
        [p['naam'], p['gemeente'], p['uurloon'], ', '.join(p['programmeertalen'])]
        for p in lijst_programmeurs
    ]
    headers = ["Naam", "Gemeente", "Uurloon (EUR)", "Programmeertalen"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

# Toon de oorspronkelijke lijst van programmeurs
print("Oorspronkelijke lijst van programmeurs:")
toon_programmeurs()

# Vraag naar de naam van de programmeur en de nieuwe programmeertaal
naam = input("Voer de naam van de programmeur in om een programmeertaal toe te voegen: ")
nieuwe_taal = input("Voer de nieuwe programmeertaal in: ")

# Voeg de programmeertaal toe aan de programmeur
voeg_programmeertaal_toe(naam, nieuwe_taal)

# Toon de bijgewerkte lijst van programmeurs
print("\nBijgewerkte lijst van programmeurs:")
toon_programmeurs()

# Vraag naar de naam van de programmeur en de programmeertaal om te verwijderen
naam_verwijderen = input("\nVoer de naam van de programmeur in om een programmeertaal te verwijderen: ")
taal_om_te_verwijderen = input("Voer de programmeertaal in die je wilt verwijderen: ")

# Verwijder de programmeertaal van de programmeur
verwijder_programmeertaal(naam_verwijderen, taal_om_te_verwijderen)

# Toon de uiteindelijke lijst van programmeurs
print("\nUiteindelijke lijst van programmeurs:")
toon_programmeurs()
