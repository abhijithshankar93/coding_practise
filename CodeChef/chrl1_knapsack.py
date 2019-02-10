def knapsack(k, cost, weight, n, K=None):
	if n == 0 or k == 0:
		return 0
	if cost[n-1] > k:
		return knapsack(k, cost, weight, n-1)
	max_weight = max(weight[n-1]+knapsack(k-cost[n-1], cost, weight, n-1),
					knapsack(k, cost, weight, n-1))

	return max_weight


test_cases = int(raw_input())
final_results = []
for count1 in range (test_cases):
	n, k = [int(i) for i in raw_input().split()]
	max_weight = 0

	cost, weight = [], []
	for count2 in range (n):
		cost_val, weight_val = [int(i) for i in raw_input().split()]
		cost.append(cost_val)
		weight.append(weight_val)
	max_weight = knapsack(k, cost, weight, len(cost))

	final_results.append(max_weight)

for val in final_results:
	print val