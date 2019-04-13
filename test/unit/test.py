from python_webdriver.core.page import PageFactory 
from python_webdriver.apps.fibetv.pages import samplePage as page
import importlib
import inspect
import unittest
import pytest

class TestPageFactory():


	@pytest.fixture
	def sample_page(self):
		return page

	@pytest.fixture
	def page_name(page = 'home'):
		return page

	def goto(self, module, page_name):
		pageVisted = []
		if hasattr(module, "goto_{}".format(page_name)):
			page_method = getattr(module, "goto_{}".format(page_name))
			page_method()
			pageVisited.append(module.__name__)
			page = getattr(module, page_name)
			assert page.__name__ = "HomePage"
		else:
			assert False

	def test_example(self, samplePage):

		assert 5==5



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




class PageModule():
	def module(self):
