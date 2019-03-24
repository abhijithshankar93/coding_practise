'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures 
(possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''

def find_min_classrooms(intervals):
	'''
	Solution creates two seperate lists. One for the start times and the other
	for the end times. 
	We then continue to sort the two lists seperately.
	Now as long as the start time < end time we know we need another class room
	when the class ends the start time >= end time and we know the class has
	ended and we can reduse the num of class rooms req.

	As every step, we check if the number of class rooms required now is more
	than the min required till before. If yes, we update the value of min
	classrooms.
	'''
	start = [val[0] for val in intervals]
	end = [val[1] for val in intervals]
	start.sort()
	end.sort()

	i = 0
	j = 0
	temp_min = 0
	final_min = 0
	while i<len(intervals) and j<len(intervals):
		if start[i] < end[j]:
			temp_min += 1
			if temp_min > final_min:
				final_min = temp_min
			i += 1
		else:
			temp_min -= 1
			j += 1

	return final_min

if __name__ == '__main__':
	intervals = [(30, 75), (0, 50), (60, 150)]
	print find_min_classrooms(intervals)

	intervals = [
				 (900,910), (940,1200), (950,1120), 
				 (1100,1130), (1500,1900), (1800,2000)
				]
	print find_min_classrooms(intervals)