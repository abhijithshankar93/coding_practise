
def recursive(num, max_dict):
	if num==1:
		max_dict['1']=1
		return 1
	if num ==0:
		max_dict['0']=0
		return 0
	try:
		return max_dict[str(num)]
	except KeyError:
		pass

	max_value = max(num, (recursive(int(num/2), max_dict)+
						  recursive(int(num/3), max_dict)+
						  recursive(int(num/4), max_dict))
					)
	max_dict[str(num)]=max_value
	return max_value


final=[]
for cnt in range (10):
	num=int(raw_input())
	max_dict={}
	max_val = recursive(num, max_dict)
	final.append(max_val)

for value in final:
	print value