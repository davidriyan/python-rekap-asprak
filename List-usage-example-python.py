# list is allow duplicate item
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist,"\n")

- - - - -

# checking list length
print(len(thislist),"\n")

- - - - -

# list can contain any data type
list1 = ["abc", 34, True, 40, "male"]

- - - - -

# checking list type
mylist = ["apple", "banana", "cherry"]
print(type(mylist),"\n")

- - - - -

# list constructor
thislist = list((
"apple", 
"banana", 
"cherry"))# note the double round-brackets
print(thislist,"\n")

- - - - -

#accesing item in list
print(thislist[1],"\n")

print(thislist[-1],"\n")
#accesing the item from the last item

# using range index
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5],"\n")

print(thislist[:4],"\n")

print(thislist[2:],"\n")

print(thislist[-4:-1],"\n")

- - - - -

#checking list item

if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list","\n")

- - - - -

#changing list item
thislist[1] = "blackcurrant"
print(thislist, "\n")

- - - - -

#selecting the index that wanted to change
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist,"\n")

- - - - -

#changin 1 item to 2 item
thislist[0] = ["blackcurrant", "watermelon"]
print(thislist,"\n")

#changin 2 item to 1 item
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist,"\n")

- - - - -

#adding item to a list
thislist.insert(2, "watermelon")
print(thislist,"\n")#adding to specific index

thislist.append("orange")
print(thislist,"\n")#adding at the end


- - - - -
#adding another list
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist,"\n")

- - - - -

#adding any iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")

thislist.extend(thistuple)
print(thislist,"\n")

- - - - -

#Removing list item
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")#removing specified item at first occurance
print(thislist,"\n")

- - - - -

thislist.pop(1)#removing specified index or the last item
print(thislist)

- - - - -

del thislist[0]#delete specified index or delete all the list completely
print(thislist)

- - - - -

thislist = ["apple", "banana", "cherry"]
thislist.clear()#clear the list but not deleting the list
print(thislist,"\n")

- - - - -

#Looping list
thislist = ["apple", "banana", "cherry"]
for x in thislist:#looping through the list
  print(x)
  
print ("\n")

- - - - -

for i in range(len(thislist)):#loopinf through index number
    print(thislist[i])

print ("\n")

- - - - -
#using while loop for the looping
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

print("\n")

- - - - -

#list comprehension

newlist = []
for x in thislist:
  if "a" in x:
    newlist.append(x)
print(newlist,"\n")#without list comprehension 

newlist = [x for x in thislist if "a" in x]
#with list comprehension 
print(newlist,"\n")

- - - - -

#filtering list item with condition
newlist = [x for x in thislist if x != "apple"]#print any item from thislist except for "apple"
print (newlist,"\n")

- - - - -

newlist = [x for x in thislist]#include all item from another list without filtering
print (newlist,"\n")

- - - - -

newlist = [x for x in range(10) if x < 5]#accepting number below 5
print (newlist,"\n")

- - - - -

newlist = [x.upper() for x in thislist]#set new list to uppercase
print (newlist,"\n")

- - - - -

newlist = ['hello' for x in thislist]#set all new item in newlist to 'hello'
print (newlist,"\n")

- - - - -

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]#adding orange instead of banana
print (newlist,"\n")

- - - - -

#Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()#sorting list from a to z
print(thislist,"\n")

- - - - -

thislist = [100, 50, 65, 82, 23]
thislist.sort()#sorting list from the smallest number
print(thislist,"\n")

- - - - -

thislist.sort(reverse = True)#sorting item in descending using keyword argument for sort
print(thislist,"\n")
#this will reverse and sorting the item from the bigger number
- - - - -

#using function as a key for sort
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]#Sort the list based on how close the number is to 50
thislist.sort(key = myfunc)
print(thislist)

- - - - -

#Case Insensitive Sort

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()#this will sort from the capital word
print(thislist,"\n")

- - - - -

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)#set sort to default alphanumerical even when there is a capital word
print(thislist,"\n")

- - - - -

thislist = ["banana", "Orange", "Kiwi", "cherry", 5]
thislist.reverse()#reverse the list regardless the alphanumeric
print(thislist,"\n")

- - - - -

#copy a list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()# if using mylist=thislist any change happen to thislist will effect the new list
print(mylist,"\n")
#or we can use
mylist = list(thislist)
print(mylist,"\n")

- - - - -

#join list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3,"\n")

- - - - -

for x in list2:
  list1.append(x)#Append list2 into list1

print(list1,"\n")

- - - - -

list1.extend(list2)#add list2 at the end of list1
print(list1,"\n")
