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

	def test_module_to_dic(self, page_factory):
		assert(page_factory.module_to_dic(pages))


	def test_generate_classes(self, page_factory):
		classes = page_factory.get_page_classes(getattr(pages, 'samplePage'))
		assert(isinstance(classes, dict))
		classes = page_factory.modify_inheritance_order(classes)

		assert(isinstance(classes, list))
		assert((re.search('[a-zA-Z0-9]*(?=_)',classes[0].__name__).group(0)) == 'Fibetv')

	def test_modify_classes(self, page_factory):
		classes = page_factory.get_page_classes(getattr(pages, 'samplePage'))
		modified_classes = page_factory.modify_valid_classes(classes)
		assert('Android_6' in classes)
		assert('Android_6' not in modified_classes)


	def test_get_submodules(self, page_factory):
		submodules = page_factory.module_to_dic(pages)
		assert('samplePage' in submodules)
		assert('sample_page_two' in submodules)


	def test_page_builder(self, page_factory):
		page_classes = page_factory.page_builder(pages)
		assert('samplePage' in page_classes)

	def test_goto(self, page_factory):
		class_modules = page_factory.page_builder(pages)
		page_factory.current_page = class_modules['samplePage']()
		page_factory.goto('sample_page_two')
		assert('sample_page_two' in page_factory.page_objects)



class Device():
	def __init__(self):
		self.application_name = "Fibetv"
		self.application_version = 5
		self.platform_name = "Android"
		self.platform_version = 5
		self.vendor_name = "Samsung"
		self.vendor_version = 5