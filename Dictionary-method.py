#dictionary is ordered,changeable, and not allow duplicate
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
#Duplicate values will overwrite existing values
print(thisdict)

- - - - - -

# checking dictionary length
print(len(thisdict))

- - - - - -

#Print the data type of a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

- - - - - -

#Using the dict() method to make a dictionary
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

- - - - - -

#Accessing Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]#Get the value of the key "model"

x = thisdict.get("model")#get() that will give you the same result

x = thisdict.keys()#keys() method will return a list of all the keys in the dictionary

- - - - - -

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
#keys() method will update the key if there is a change
print(x) #before the change

car["color"] = "white"
print(x) # after changed

- - - - - -

#The values() method will return a list of all the values in the dictionary
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
#values() method will get update when there is a change
print(x) #before the change

car["year"] = 2020
print(x) #after the change

- - - - - -

#Get a list of the key:value pairs
x = thisdict.items()

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()
#items() method will get update if there is a change
print(x) #before the change

car["year"] = 2020
print(x) #after the change

- - - - - -

#Removing Items
#The pop() method removes the item with the specified key name
thisdict.pop("model")
print(thisdict)

- - - - - -

#The popitem() method removes the last inserted item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

- - - - - -

#The del keyword removes the item with the specified key name
#del keyword can also delete the dictionary completely
del thisdict["model"]
print(thisdict)

- - - - - -

#The clear() method empties the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

- - - - - -

#Copy a Dictionary
#Make a copy of a dictionary with the copy() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

- - - - - -

#Some other dictionary Methods
"""
clear()
copy()
fromkeys()
get()
items()
keys()
pop()
popitem()
setdefault()
update()
values()
"""
