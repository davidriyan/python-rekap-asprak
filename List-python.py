#list (similar to array) is used to store a multiple value, so its like a variable but has a multiple value

mylist = ["apple", "mango", "pineapple", 5, 8.5]
print(mylist)

#it can contain any type of data type

list1 = ["abc", 34, True, 4.0,[35,76],("this is tupple",56,79,True)]
print(list1)

#list is sorted by index and the index in python is start from 0
#we can call a specific index of a list by calling its index

list2 = [65, "pineapple", "pizza"]
print(list2[2])

#we can adding a new value to a list by using append, and insert

list3 = [1,2,3,4]

#append will adding a new value in the last index
list3.append(5)

#insert will take the index we want it to be placed and the value
list3.insert(5,6)

#here 5 is the index
