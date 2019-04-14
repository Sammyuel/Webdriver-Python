import importlib
import inspect


class PageFactory():
	def __init__(self, pages, app_name, device, **kwargs):
		self.pages = import_pages(pages)
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


	def import_page_modules(self, modules):
		return [m[0] for m in inspect.getmembers(modules, ismodule)]

	def import_page_classes(self, module):
		return [m[0] for m in inspect.getmembers(module, isclass)]

	def import_page_methods(self, module):
		return [m[0] for m in inspect.getmembers(module, ismethod)]


	def page_class_generator(self, page):
		page_classes = [m[0] for m in inspect.getmembers(page, isclass)]
		page_class = type(page.__name__, object, )
		pass





	def import_




	"""
	Imports the pages correspending to the self.app name 
	"""
	def import_pages_from_location(self):
		imp_path = ".apps.{}.pages".format(self.app)
		page_modules = importlib.import_module(imp_path)
		page_names = [m[0] for m in inspect.getmembers(page_modules, isclass)]
		page_classes = [getattr(page_modules, page_name) for page_name in page_names]
		return page_classes

