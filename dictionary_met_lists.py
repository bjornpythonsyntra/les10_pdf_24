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

# Toon de data van de programmeurs
for programmeur in lijst_programmeurs:
    print(f"Naam: {programmeur['naam']}")
    print(f"Gemeente: {programmeur['gemeente']}")
    print(f"Uurloon: {programmeur['uurloon']} EUR")
    print(f"Programmeertalen: {', '.join(programmeur['programmeertalen'])}")
    print("-" * 30)# 30 streepjes
