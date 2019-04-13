from python_webdriver.core.page import PageFactory 
from python_webdriver.apps.fibetv.pages import samplePage as page
from python_webdriver.apps.fibetv import fibetv_test

import importlib
import inspect
import unittest
import pytest



class TestPageFactory():


	@pytest.fixture
	def sample_page(self):
		return page

	@pytest.fixture
	def page_name(self, page = 'home'):
		return page

	def goto(self, module, page_name):
		visited = []
		if hasattr(module, "goto_{}".format(page_name)):
			page_method = getattr(module, "goto_{}".format(page_name))
			page_method()
			visited.append(module.__name__)
			return visited, page_method
		else:
			return False

	def test_goto(self, sample_page, page_name):
		print(dir(fibetv_test))
		print("see above")
		visited, page = self.goto(sample_page, page_name)
		#print(visited[0])
		#print("see above")

		assert page.__name__ == "goto_home"
		assert callable(page)


	def import_pages(self):
		imp_path = ".apps.{}.pages".format(self.app)
		page_modules = importlib.import_module(imp_path)
		page_names = [m[0] for m in inspect.getmembers(page_modules, isclass)]
		page_classes = [getattr(page_modules, page_name) for page_name in page_names]
		return page_classes

	def teardown_method(self):
		pass




class PageModule():
	def module(self):
		pass
	def goto(module, page_name):
		visited = []

