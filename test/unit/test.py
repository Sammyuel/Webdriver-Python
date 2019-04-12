from python_webdriver.core.page import PageFactory 
from python_webdriver.apps.fibetv.pages import samplePage
import importlib
import inspect
import unittest

class TestPageFactory():


	def setup_method(self):
		print(dir(samplePage))
		print("see above")


	def test_example(self):
		assert 5==5

	def goto(self, page_name, pages):
		if hasattr(pages, "goto_{}".format(page_name)):
			page_method = getattr()
	def test_goto(self):
		print("hello")
		assert 1==1

	def import_pages(self):
		imp_path = ".apps.{}.pages".format(self.app)
		page_modules = importlib.import_module(imp_path)
		page_names = [m[0] for m in inspect.getmembers(page_modules, isclass)]
		page_classes = [getattr(page_modules, page_name) for page_name in page_names]
		return page_classes

	def teardown_method(self):
		print("look above")

"""

	def goto(self, page_name):
		if hasattr(self.pages, "goto_{}".format(page_name)):
			page_method = getattr(self.page, "goto_{}".format(page_name))
			page_method()
			self.pageVisited.append(self.page.__name__)
			self.page = getattr(self.pages, page_name)
		else:
			raise Exception("Invalid page name provided to goto method")
"""



