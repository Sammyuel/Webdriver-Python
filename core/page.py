import importlib
import inspect


class PageFactory():
	def __init__(self, app_name, device, **kwargs):
		self.pages = import_pages
		self.app = app_name
		self.page = pages.HomePage
		self.pageVisited = [self.page.__name__]

	def goto(self, page_name):
		if hasattr(self.pages, "goto_{}".format(page_name)):
			page_method = getattr(self.page, "goto_{}".format(page_name))
			page_method()
			self.pageVisited.append(self.page.__name__)
			self.page = getattr(self.pages, page_name)
		else:
			raise Exception("Invalid page name provided to goto method")


	def page_builder(self):

		for page in self.pages:
			pass

	def class_generator(self):
		pass




	"""
	Imports the pages correspending to the self.app name 
	"""
	def import_pages(self):
		imp_path = ".apps.{}.pages".format(self.app)
		page_modules = importlib.import_module(imp_path)
		page_names = [m[0] for m in inspect.getmembers(page_modules, isclass)]
		page_classes = [getattr(page_modules, page_name) for page_name in page_names]
		return page_classes

