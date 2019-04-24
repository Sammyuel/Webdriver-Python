
import requests

class Appium():
	sessions_url = 'http://0.0.0.0:4723/wd/hub/sessions'
	def __init__(self, device_info):
		pass


	def get_session_ids(self):
		r  = requests.get(self.sessions_url)
		body = dict(r.json())
		return body


example = Appium(5)

body = example.get_session_ids()

print(type(body))

