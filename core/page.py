import importlib

class PageFactory():
	def __init__(self, app_name, device, **kwargs):
		self.pages = import_pages
		self.app = app_name
		self.page = pages.HomePage
		self.pageVisted = [self.page]

	"""
	Imports the pages correspending to the self.app name 
	"""
	def import_pages(self):
		imp_path = from f".apps.{self.app}.pages import * as pages"
		page_modules = importlib.import_module(imp_path)
		page_names = [m[0] for m in inspect.getmembers(page_modules, isclass)]
		page_classes = [getattr(page_modules, page_name) for page_name in page_names]
		return page_classes



	def page_builder(self):

		for page in self.pages:





