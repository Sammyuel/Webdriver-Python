import importlib
import inspect
import re


class PageFactory():
	def __init__(self, device, pages, app_name, device, **kwargs):
		self.device = device
		self.page_classes = page_builder(pages)
		self.page_objects = {}
		self.app = app_name
		self.page = pages.HomePage
		self.pageVisited = [self.page.__name__]
		self.inheritance_order = [self.device.application_name, self.device.platform_name, self.device.vendor_name]

	def goto(self, page_name, *args, **kwargs):
		if hasattr(self.pages, "goto_{}".format(page_name)):
			page_method = getattr(self.page, "goto_{}".format(page_name))
			self.page_method()
			self.pageVisited.append(self.page.__name__)
			new_page = self.page_objects[page_name] if page_name in page_objects else self.page_classes[page_name](*args, **kwargs)
			self.page = new_page
		else:
			raise Exception("Invalid page name provided to goto method")
		return self.page


	def page_builder(self, modules):
		pages = {}
		modules = import_page_modules(modules)
		for module in modules:
			page = self.page_classes(module)
			ordered_page = inerheitance_chance(page)




	def inheritance_chain(self, class_names):
		order = [self.device.application_name, self.device.platform_name, self.device.vendor_name]
		result = []
		for class_name in class_names:
			index = 

	def modify_page_classes(self, page_classes):

		pass

	def max_range(self, class_name):
		pass

	def min_range(self, class_name):
		pass

	def parse_version_value(self, class_name):
		version = re.search("(?<=_)[0-9|_]*", class_name).group(0)
		version = int(version.replace('_', ''))
		return version 



	def inject_comparitors(self, class_name):
		def __eq__(self, other):
			order = self.inheritance_order
			for i, elem in enumerate(order):
				if class_name.lower() in elem:
					self.index = i
			return self.index == other.index

		def __gt__(self, other):
			pass


	def get_class_name(self, class_name):
		pass

	def get_class_version(self, class_name):
		pass



	def create_class_order(self, base, module):
		main_class = type(module.__name__, base, {})
		return main_class

			

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

