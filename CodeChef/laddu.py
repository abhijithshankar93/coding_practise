test_cases = raw_input()
results=[]

for count in range (int(test_cases)):
	activities, origin = raw_input().split()
	activities = int(activities)
	total_points = 0

	for count in range (activities):
		activity = raw_input()
		if 'CONTEST_WON' in activity:
			if int(activity.split()[1]) < 20:
				rank=int(activity.split()[1])
			else:
				rank=int(20)
			total_points+=300+20-rank
		elif 'BUG_FOUND' in activity:
			total_points+=int(activity.split()[1])
		elif 'CONTEST_HOSTED' in activity:
			total_points+=50
		elif 'TOP_CONTRIBUTOR' in activity:
			total_points+=300

	if origin == 'INDIAN':
		results.append(int(total_points/200))
	else:
		results.append(int(total_points/400))

for result in results: print result