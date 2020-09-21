import telepot
from time import sleep
from event import Event
from app import App
token = '1275431928:AAETNlOvfxbVUnneHmM-ON87tZuV2PF5v1Q'
TelegramBot = telepot.Bot(token)
global chat_id
print(TelegramBot.getMe())
app = App()

def answer(msg):
	global chat_id
	content_type, chat_type, chat_id = telepot.glance(msg)
	print(content_type, chat_type, chat_id)
	if content_type == 'text':
		#TelegramBot.sendMessage(chat_id, "You said '{}'".format(msg["text"]))
		print(msg["text"])
		parse(msg['text'])

def parse_time(time):
	day_mnth_year, hour_min = time.split(' ')[1:]
	day, mnth, year = day_mnth_year.split('.')
	hour, min = hour_min.split(':')
	return day, mnth, year, hour, min
def is_time_correct(day, mnth, year, hour, min):
	if all((day.isdigit(), mnth.isdigit(), year.isdigit(), hour.isdigit(), min.isdigit())):
		day = int(day)
		mnth = int(mnth)
		year = int(year)
		hour = int(hour)
		min = int(min)
	else:
		return False
	if all(
		(day > 0, day <= 31, mnth > 0, mnth <= 12, year >= 2020, year < 2030, hour >= 0, hour <= 23, min > 0, min < 60)):
		pass
	else:
		return False
	return True

def parse(str):
	global chat_id
	str = str.split(';')
	if len(str) >= 2:
		msg = str[0]
		time_to_send = str[1]
		day, mnth, year, hour, min = parse_time(time_to_send)
		if is_time_correct(day, mnth, year, hour, min):
			event = Event(msg, {'day': int(day), 'mounth': int(mnth), 'year': int(year), 'hour': int(hour), 'minute': int(min)})
			app.events.append(event)
			TelegramBot.sendMessage(chat_id, 'at '+ time_to_send+ ' i will text you: ' + msg)

		else:
			TelegramBot.sendMessage(chat_id, 'wrong format')

TelegramBot.message_loop(answer)

while True:
	for event in app.events:
		if event.timer == 0:
			TelegramBot.sendMessage(chat_id, event.text)
			app.events.remove(event)
		else:
			event.timer -=1
	sleep(1)
