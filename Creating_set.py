languages = set()
print(type(languages),languages)

languages = {'Python','R','SAS','julia'}
print(type(languages),languages)

#set of mixed datatypes
mixed_set = {"Python",(2.7,3.4)}
print(type(mixed_set),languages)

#accesing set elements
print(list(languages)[0])
print(list(languages)[0:3])

#add an element
languages.add('Ruby')
print(languages)
#add multiple elements
languages.update(['Scala','C'])

print(languages)

#remove an elements
languages.remove('C')
print(languages)

#discard an element, although c has been removed discard will not throw an error
languages.discard('C')
print(languages)

#pop will remove a random item from set
print("removed:",(languages.pop()),"from",languages)

