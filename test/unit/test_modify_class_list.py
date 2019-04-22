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

	def test_page_classes(self, page_factory):
		print("see below")
		print(page_factory.generate_page_classes(getattr(pages, 'samplePage')))
		print("see above")











class Device():
	def __init__(self):
		self.application_name = "fibe"
		self.application_version = "0"
		self.platform_name = "android"
		self.platform_version = "0"
		self.vendor_name = "samsung"
		self.vendor_Version = "0"