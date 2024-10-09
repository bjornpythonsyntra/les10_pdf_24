persoon = {"naam":"jan","hobbies":["tennis","voetbal","golf","Fotografie"]}
print(persoon["hobbies"])
for hobby in persoon["hobbies"]:
    print(hobby)
nieuwe_hobby = input("geef een nieuwe hobby")
persoon["hobbies"].append(nieuwe_hobby)
for hobby in persoon["hobbies"]:
    print(hobby)
verwijder_hobby = input("welke hobby verwijderen")
if verwijder_hobby in persoon["hobbies"]:
    persoon["hobbies"].remove(verwijder_hobby)
else:
    print("niet in lijst")
for hobby in persoon["hobbies"]:
    print(hobby)
