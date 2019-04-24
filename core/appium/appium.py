
import requests

class Appium():
	sessions_url = 'http://0.0.0.0:4723/wd/hub/sessions'
	def __init__(self, device_info):
		pass


	def _get_session_ids(self):
		r  = requests.get(self.sessions_url)
		body = dict(r.json())
		#values = body['value']
		#ids = [value['id'] for value in values]
		return body

	def confirm_sessions(self):
		ids = self._get_session_ids()
		if len(ids) == 0:
			raise Exception("No session ids found")
		else:
			return ids


example = Appium(5)

body = example.get_session_ids()

print(body)

