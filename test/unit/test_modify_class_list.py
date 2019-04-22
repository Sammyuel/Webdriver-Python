from .module_examples import page_classes 
from python_webdriver.core.page import PageFactory 
import python_webdriver.apps.fibetv.pages as pages
import importlib
import inspect
import unittest
import pytest
import re


class TestPageClasses():
	@pytest.fixture
	def page_factory(self):
		device = Device()
		pages = page_classes
		page_factory = PageFactory(device, pages, "fibetv")
		return page_factory

	def convert_modules_to_classes(self, module):
		return module

	def test_generate_classes(self, page_factory):
		classes = page_factory.generate_page_classes(getattr(pages, 'samplePage'))
		assert(isinstance(classes, dict))
		classes = page_factory.modify_inheritance_order(classes)
		assert(isinstance(classes, list))
		assert((re.search('[a-zA-Z0-9]*(?=_)',classes[0].__name__).group(0)) == 'Fibetv')











class Device():
	def __init__(self):
		self.application_name = "Fibetv"
		self.application_version = "0"
		self.platform_name = "Android"
		self.platform_version = "0"
		self.vendor_name = "Samsung"
		self.vendor_Version = "0"