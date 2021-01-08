try:
	x=1
	y=1
	print("result of x/y",x/y)
except(ZeroDivisionError):
	print("can not divide by zero")
except(TypeError):
	print("wrong datatype,division is allowed on nuberic data type only")
except:
	print("unexpected error occured",'\n',"Error Type:",sys.exc_info()[0],'\n',"Error msg:",sys.exc_info()[1])



