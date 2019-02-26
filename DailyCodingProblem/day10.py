'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, 
and calls f after n milliseconds.
'''

import time
import datetime
from multiprocessing import Queue, Process
from Queue import Empty

def echo(*args):
	print args

def simple_scheduler(f, n, args=[], kwargs={}):
	'''
	Function takes in a simple function with args and just schedules the event
	after n milliseconds
	No parallel processing allowed. Will pick up next task only after one
	completes
	'''
	print 'Starting wait at: {}'.format(datetime.datetime.now())
	time.sleep(n/1000)
	print 'Executing function at: {}'.format(datetime.datetime.now())
	return f(*args,**kwargs)

class async_scheduler:
	def __init__(self):
		self.queue=Queue()
		timeout=20
		self.monitoring_process = Process(target=self._monitoring_deamon, 
										  args=(timeout,))
		self.monitoring_process.start()
		
	
	def joiner(self, processes):
		for process in processes:
			process.join()

	def finish(self):
		self.monitoring_process.join()


	def _monitoring_deamon(self, timeout):
		end = None
		proc = []
		while True:
			try:
				if not self.queue.empty():
					func = self.queue.get()
					end = None
					#start processes for each task
					proc.append(Process(target=simple_scheduler,
									args=(func[0],func[1],func[2])))
					proc[-1].start()
					#simple_scheduler(func[0],func[1],func[2])
				if end == None:
					end = datetime.datetime.now() + datetime.timedelta(
															seconds = timeout)
				if datetime.datetime.now() > end:
					self.joiner(proc)
					print 'Exiting at {} as size is Zero for {} sec'.format(
												datetime.datetime.now(),timeout
																	   )	
					break	
			except Empty:
				if end == None:
					end = datetime.datetime.now().second + timeout
				if datetime.datetime.now() > end:
					self.joiner(proc)
					print 'Exiting at {} as size is Zero for {} sec'.format(
												datetime.datetime.now(),timeout
																	   )
					break		

	def async_scheduler_process(self, f, n, args=[]):
		self.queue.put((f,n,args))

	


if __name__ == '__main__':
	#simple_scheduler(echo, 10000, [10, 15, 'a'])
	#simple_scheduler(echo, 5000, ['b', -1, 6])
	
	a = async_scheduler()
	a.async_scheduler_process(echo, 5000, [1,2])
	a.async_scheduler_process(echo, 7000, [3,4])
	a.async_scheduler_process(echo, 3000, [5,6])
	a.finish()
