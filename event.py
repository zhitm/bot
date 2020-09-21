from time import localtime
class Event:
	def __init__(self, text, time):
		self.text = text
		self.time = time
		self.timer = None
		self.set_timer()
	def set_timer(self):
		hour = localtime().tm_mday*24 + localtime().tm_hour
		min = localtime().tm_min
		sec = localtime().tm_sec
		self.timer = ((self.time['day']*24 + self.time['hour']-hour)*60 + self.time['minute'] - min) * 60  - sec #я потом буду учитывать год и месяц, мне лень
		


