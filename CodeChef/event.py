days_list = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

test_cases=int(raw_input())

result = []
for cnt in range (0, test_cases):
	start_day, end_day, range_start, range_end = raw_input().split()
	range_start, range_end = [int(i) for i in (range_start,range_end)]

	start_index = days_list.index(start_day.lower())
	end_index = days_list.index(end_day.lower())

	if end_index < start_index:
		end_index += 7

	total_days = end_index - start_index + 1
	solution = 'impossible'

	while True:
		if total_days < range_start:
			total_days += 7
			continue
		if total_days >= range_start and total_days <= range_end:
			if solution == 'impossible':
				solution = 'one'
			elif solution == 'one':
				solution = 'many'
				break
			total_days += 7
		if total_days > range_end:
			break

	if solution == 'one':
		result.append(total_days-7)
	else:
		result.append(solution)

for i in result: print i
