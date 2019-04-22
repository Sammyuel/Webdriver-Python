import importlib
import inspect
import python_webdriver.apps.fibetv.pages as pages
import re


class PageFactory():
	def __init__(self, device, pages, app_name, **kwargs):
		self.device = device
		self.page_classes = pages
		self.page_objects = {}
		self.app = app_name
		self.page = 'Homepage'
		self.pageVisited = [self.page]
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


	def modify_inheritance_order(self, page_classes):
		order = [self.device.application_name, self.device.platform_name, self.device.vendor_name]
		class_names = list(page_classes.keys())
		start_ptr = 0
		end_ptr = len(class_names) - 1
		i = 0
		while i < len(class_names):
			class_name = str(re.search('[a-zA-Z0-9]*(?=_)',class_names[i]).group(0))
			if class_name == order[0] and start_ptr != i:
				class_names[start_ptr], class_names[i] = class_names[i], class_names[start_ptr]
				start_ptr += 1
			elif class_name == order[-1] and end_ptr != i:
				class_names[i], class_anmes[end_ptr] = class_names[end_ptr], class_names[i]
				end_ptr -= 1
				i -= 1
			i += 1
		return [page_classes[page_class] for page_class in class_names]

	def get_class_name(self, class_name):
		name = str(re.search("[a-z]*(?=_)", class_name).group(0).replace("_", ""))
		return name

	def module_to_class_list(self):
		pass


	def module_to_dic(self):
		modules = {name:page for name, page in inspect.getmembers(pages, inspect.ismodule)}
		return modules

	def create_base_class(self):
		pass

	def generate_page_classes(self, mod):
		methods = {name:method for name, method in inspect.getmembers(mod, inspect.isfunction)}
		page_classes = {name:page for name, page in inspect.getmembers(mod, inspect.isclass)}	
		return page_classes	
		main_class = type(re.search('(?=.)[[a-zA-Z0-9]]*$', mod.__name__).group(0), () , {key:methods[key] for key in methods})
		if main_class and main_class.__name__ not in page_classes: 
			page_classes[main_class.__name__] = main_class
		return page_classes

	def modify_valid_classes(self, page_classes):
		valid_names = [self.device.application_name, self.device.platform_name, self.device.vendor_name]
		valid_classes = [page_class for page_class in page_classes if get_class_name(page_class) in valid_names and parse_version_value(page_class.__class__.__name__) <= getattr(self.device, page_class.version)]
		return valid_classes


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





	def create_class_order(self, base, module):
		main_class = type(module.__name__, base, {})
		return main_class

			

	def import_page_modules(self, modules):
		return {m[0].__name__: m[0] for m in inspect.getmembers(modules, ismodule)}


	def set_page_objects(self, pages):
		page_objects = {key:page() for key,page in pages.items()}
		return page_objects



	def get_page_classes(self, page_name):
		methods = import_page_methods(page_name)
		page_classes = import_page_classes(page_name)

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

