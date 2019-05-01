import sys
import requests

class Appium():
	sessions_url = 'http://0.0.0.0:4723/wd/hub'
	def __init__(self, device_info = None):
		self.session_ids = self.confirm_sessions()
		self.device_info = self._get_device_info()

	def _get_session_ids(self):
		r  = requests.get(self.sessions_url + '/sessions')
		body = dict(r.json())
		values = body['value']
		ids = [value['id'] for value in values]
		return ids

	def confirm_sessions(self):
		ids = self._get_session_ids()
		if len(ids) == 0:
			raise Exception("No session ids found")
		else:
			def compare_sessions(session_ids):
				args_session_ids = sys.argv[1:]
				for args_session_id in args_session_ids:
					if args_session_id not in session_ids:
						raise Exception(f"Session id {args_session_id} could not be found")
				return args_session_ids
			return compare_sessions(ids)

	def _get_device_info(self):
		device_info = {}
		for session_id in self.session_ids:
			session_url = self.sessions_url + f'/session/{session_id}'
			session_info = dict(requests.get(session_url).json())
			device_infp[session_id] = session_info
		return device_info

			




example = Appium(5)
