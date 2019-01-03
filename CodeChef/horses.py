test_cases = int(raw_input())
res = []
for cnt in range (test_cases):
	n = raw_input()
	s = [int(i) for i in raw_input().split()]

	s.sort()
	min_diff=float('inf')
	for index in range(1,len(s)):
		diff=abs(s[index]-s[index-1])
		if diff < min_diff:
			min_diff = diff
	res.append(min_diff)

for diff in res:
	print diff