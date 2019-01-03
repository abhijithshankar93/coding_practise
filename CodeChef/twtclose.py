n, k = [int(i) for i in raw_input().split()]

twt_hist={}
final_res=[]
count=0
for i in range (k):
	action = raw_input()
	if 'CLICK' in action:
		try:
			twt_hist.pop(str(action.strip().split()[1]))
			count -= 1
		except KeyError:
			twt_hist[str(str(action.strip().split()[1]))]=1
			count += 1
	else:
		twt_hist={}
		count=0

	final_res.append(count)

for val in final_res: print val





