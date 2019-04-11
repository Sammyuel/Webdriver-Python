import importlib

class PageFactory():
	def __init__(self, app_name, **kwargs):
		self.page = HomePage
		self.app = app_name

	"""
	Imports the pages correspending to the self.app name 
	"""
	def import_pages():
		imp_path = from f".apps.{self.app}.pages import * as pages"
		importlib.import_module(imp_path)

	def page(self):

