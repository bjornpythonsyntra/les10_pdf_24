persoon = {"naam":"jan","hobbies":["tennis","voetbal","golf",["kunst foto"
                                   ,"industrie","stilleven","portret","naakt"],"krant lezen"]}
print(persoon["hobbies"])
for hobby in persoon["hobbies"]:
    if type(hobby) == list:
        print("uitbreiding hobby")
        for inner_hobby in hobby:
            print(inner_hobby,end="\t")
        print("")
    else:
        print(hobby)