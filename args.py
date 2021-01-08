#simple function to loop through arguments and print them

#def sample_function(*args):
#	for a in args:
#		print(a)
#call the function
#sample_function(1,2,3)

def sample_function(**kwargs):
	for a in kwargs:
		print(a,kwargs[a])
sample_function(name='common',number=22312)		

