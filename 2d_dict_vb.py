myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
myfamily["child4"] = {"name" : "Rinus","year" : 2013}
print(myfamily["child2"]["year"])
for child in myfamily.values():
  for k,v in child.items():
    print(k,v)
