

class Cranberry(object):

	def __init__(self):
		self.x = me
		self.y = lyh
		self.encounter_times = 0

	def encounter(self):
		return True

	def scheme(self, status_of_lyh=True):
		x = self.x
		y = self.y

		while status_of_lyh:
			
			if self.encounter_times == 2:
				import logging
				logging.info('x try means to date y')
				break
			elif self.encounter():
				self.encounter_times += 1
			else:
				import time, random
				some_time = random.random()
				time.sleep(some_time)

		return 'Triumph'


if __name__ == '__main__':

	the_cranberry = Cranberry()
	the_cranberry.scheme()