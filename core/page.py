import importlib
import inspect


class PageFactory():
	def __init__(self, pages, app_name, device, **kwargs):
		self.page_classes = page_builder(pages)
		self.page_objects = {}
		self.app = app_name
		self.page = pages.HomePage
		self.pageVisited = [self.page.__name__]

	def goto(self, page_name, *args, **kwargs):
		if hasattr(self.pages, "goto_{}".format(page_name)):
			page_method = getattr(self.page, "goto_{}".format(page_name))
			page_method()
			self.pageVisited.append(self.page.__name__)
			new_page = self.page_objects[page_name] if page_name in page_objects else self.page_classes[page_name](*args, **kwargs)
			self.page = new_page
		else:
			raise Exception("Invalid page name provided to goto method")
		return self.page


	def page_builder(self, modules):
		page_classes = {}
		modules = import_page_modules(modules)
		for module in modules:
			


	def import_page_modules(self, modules):
		return {m[0].__name__: m[0] for m in inspect.getmembers(modulesm ismodule)}


	def page_classes(self, module):
		methods = [m[0] for m in inspect.getmembers(module, ismethod)]
		page_classes = {m[0].__name__: m[0] for m in inspect.getmembers(module, isclass)}
		page_class = type(module.__name__, () , {method.__name__:method for method in methods}) if module.__name__ is in page_classes else None
		if page_class and page_class.__class__.__name__ not in page_classes: 
			page_classes[page_class.__class__.__name__] = page_class
		return page_classes



	def set_page_objects(self, pages):
		page_objects = {key:page() for key,page in pages.items()}
		return page_objects



	def get_page_classes(self, page_name):
		methods = import_page_methods(page_name)
		page_classes = import_page_classes(page_name)
		if 

		page_class = type(page.__name__, object, {method.__name__:method for method in methods})
		return page_class



	def get_page_objects(page_classes):
		return {page.__class__.__name__: page for page in page_classes}


	"""
	Imports the pages correspending to the self.app name 
	"""
	def import_pages_from_location(self):
		imp_path = ".apps.{}.pages".format(self.app)
		page_modules = importlib.import_module(imp_path)
		page_names = [m[0] for m in inspect.getmembers(page_modules, isclass)]
		page_classes = [getattr(page_modules, page_name) for page_name in page_names]
		return page_classes

