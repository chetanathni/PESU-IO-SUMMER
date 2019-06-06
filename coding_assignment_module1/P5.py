print("Hi there")
a=input("Enter a string ")
print("The entered string is :", a)
check=a.isnumeric()
check2=a.isalnum()
if check:
	print("The string is numeric.")
else:
	if check2:
		print("The string is alphanumeric.")
	else:
		print("The string is non-numeric.")