data = {"naam":"bjorn","leeftijd":30,"stad":"Genk"}
        #key    #value
data["postcode"] = "3600"#toevoegen naam van de key = waarde
#x = data.keys() ha
# for i in x:
#     print(i)
data["postcode"] = "3500"
for k,v in data.items():
    print(k,v)