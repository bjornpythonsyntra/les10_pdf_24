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

# Maak de data klaar voor tabulate
table_data = [
    [p['naam'], p['gemeente'], p['uurloon'], ', '.join(p['programmeertalen'])]
    for p in lijst_programmeurs
]

# Headers voor de tabel
headers = ["Naam", "Gemeente", "Uurloon (EUR)", "Programmeertalen"]

# Toon de tabel met tabulate
print(tabulate(table_data, headers=headers, tablefmt="grid"))
