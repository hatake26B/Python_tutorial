import operator
#list accessing
list_1 = ['Statistics','programming',2019,2020,2021];
list_2 = ['a','b',1,2,3,4,5,6,7];
#adding new value to list
print("list_1[0]:",list_1[0])
print("list_2[1:5]:",list_2[1:5])
#Adding new values to the list
list_1.append(2022)
print("list_1 values post append:",list_1)
#updating existing values in the list
print("Index 2 value:",list_1[2])
list_1[2]=2018;
print("Index 1's new value:",list_1[2])
# deleting list elements
del list_1[5];
print("After deleting value at index 2:",list_1)

#Basic operation in the list
print("Length:",len(list_1))
print("concatenation:",[1,2])
print("Repetition:",['hello']*4)
print("membership:",3 in [1,2,3])
print("Intertuion:",)
for x in [1,2,3]:
	print(x)
#Negative sign will count from right
print ("slicing:", list_1[1:])
#comparing elements	of lists
a=[1,2,3,4]
b=[1,2,3]
print(operator.eq(set(a),set(b)))
print("max of list:",max([1,2,3,4,5]))
print("min of list:",min([1,2,3,4,5]))
print("Count number of 1 in list:",[1,2,3,4,5,].count(1))
list_1.extend(list_2)
print("extend:",list_1)
print("index for programming:",list_1.index('programming'))
print(list_1)
print("pop last item in list:",list_1.pop())
print("pop the intem with index 2:",list_1.pop(2))
list_1.remove('b')
print("removed b from list:",list_1)
list_1.reverse()
print("reverse:",list_1)
list_1.sort()
print("sort ascending:",list_1)
list_1.sort(reverse=True)
print("sort descending:",list_1)




