#Dictionary Methods
d = {"black": "car", "red": "rose"}
print(d.keys())
print(d.values())
print(d.items())

#Inserting and removing elements in a dictionary
d = {"blue": "sky", "red": "rose"}
d["black"] = "car"
d.pop("red")
print(d)


#traverse a dictionary and perform len(), type()
d = {"blue": "Sky", "red": "rose", "yellow": "Sun"}

for i in d:
    print(i)
print(len(d))
print(type(d))

