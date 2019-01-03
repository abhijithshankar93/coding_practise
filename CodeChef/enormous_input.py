n, k = [int(i) for i in raw_input().split()]

counter=0
for i in range (0,n):
	t = int(raw_input())
	if t % k == 0:
		counter += 1

print counter