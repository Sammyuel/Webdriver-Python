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


	def page_builder(self, mod):
		modules = self.module_to_dic(mod)

		pages = {}
		for module in modules:
			page_classes = self.get_page_classes(modules[module])
			modified_page_classes = self.modify_valid_classes(page_classes)
			ordered_pages = self.modify_inheritance_order(modified_page_classes)
			ordered_pages.append(self.include_classes_methods(module, modules[module]))
			base_class = self.create_base_class(module, ordered_pages)
			pages[base_class.__name__] = base_class
		self.pages = pages
		return pages



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



	def module_to_dic(self, module):
		modules = {name:page for name, page in inspect.getmembers(module, inspect.ismodule)}
		return modules

	def create_base_class(self, mod, page_classes):
		base_class = type(mod, tuple(page_classes) , {})
		return base_class

	def get_page_classes(self, mod):
		page_classes = {name:page for name, page in inspect.getmembers(mod, inspect.isclass)}	
		return page_classes

	def include_classes_methods(self, name, mod):
		methods = {name:method for name, method in inspect.getmembers(mod, inspect.isfunction)}
		main_class = type('Main', (), {key:methods[key] for key in methods})
		return main_class

	def get_class_name(self, class_name):
		name = str(re.search("[A-Za-z0-9]*(?=_)", class_name).group(0).replace("_", ""))
		return name

	def modify_valid_classes(self, page_classes):
		valid_names = [self.device.application_name, self.device.platform_name, self.device.vendor_name]
		valid_versions = [self.device.application_version, self.device.platform_version, self.device.vendor_version]
		valid_classes = {}
		index = 0 
		for page_class in page_classes:
			class_name = self.get_class_name(page_class)
			if class_name in valid_names:
				for i, names in enumerate(valid_names):
					if class_name in names:
						index = i 
						break
				if self.parse_version_value(page_class) <= valid_versions[index]:
					valid_classes[page_class] = page_classes[page_class]
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

