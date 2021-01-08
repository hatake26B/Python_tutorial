none = None #singleton null object
boolean = bool(True)
integer = 1
Long = 3.14

#float
Float = 3.14
Float_inf = float('inf')
Float_nan = float('nan')

#complex onject type, note ussage of letter j
Complex = 2+8j

#String can be enclosed in single or double quotes
string = 'this is a string'
me_also_string = 'also string'

List = [1,True,'AI'] #Values can be Changed

Tuple = (1, True, 'AI') # values can not be changed

Set = set([1,2,2,3,4,5,5]) #duplicated will not be stored

#use a directory when you have a set of unique keys that map to values
Dictionary = {'a':'A',2:'AA',True:1,False:0}

print (type(none)), none
print (type(boolean)) boolean
print (type(integer)), integer
print (type(Long)) ,Long
print (type(Float)) , Float
print (type(Float_inf)), Float_inf
print (type(Float_nan)), Float_nan
print (type(Complex)) , Complex
print (type(string)) , string
print (type(me_also_string)) , me_also_string
print (type(Tuple)) , Tuple
print (type(List)), List
print (type(Set)) , Set
print (type(Dictionary)) , Dictionary


