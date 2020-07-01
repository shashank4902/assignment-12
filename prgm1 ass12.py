1#sum all the items in a dictionary
def returnSum(mydict):
	sum=0
	for i in mydict:
		sum=sum+mydict[i]
	return sum
dict={'a':100,'b':200,'c':300}
print("sum:",returnSum(dict))