def Search(a,ele,beg,end):
	if(ele>a[end]):
		return -1
	else:
		mid=int((beg+end)/2)
		if a[mid]==ele:
			return mid
		elif a[mid]>ele:
			end=mid-1
			return Search(a,ele,beg,end)
		else:
			beg=mid+1
			return Search(a,ele,beg,end)
	

print ("Hi there")
a=input("Enter a list of ordered numbers, separated by a comma. Press enter when done\n").split(",")
for i in range(0,len(a)):
	a[i]=int(a[i])
ele=int(input("Enter the number to be found : "))
beg=0
end=len(a)-1
pos = int(Search(a,ele,beg,end))
if pos!=-1:
	print("The number ",ele," has been found at position ",pos)
else:
	print("Element not found")