test_cases = int(raw_input())
final_results = []
for count1 in range (test_cases):
	n, k = [int(i) for i in raw_input().split()]
	max_weight = 0

	for count2 in range (n):
		cost, weight = [int(i) for i in raw_input().split()]
		if cost <= k and weight >= max_weight:
			max_weight=weight

	final_results.append(max_weight)

for val in final_results: print val
