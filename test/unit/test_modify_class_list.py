from .module_examples import page_classes 
from python_webdriver.core.page import PageFactory 
from python_webdriver.apps.fibetv.pages import samplePage as page
import importlib
import inspect
import unittest
import pytest


class TestPageClasses():
	@pytest.fixture
	def page_factory(self):
		device = Device()
		pages = page_classes
		page_factory = PageFactory(device, pages, "fibetv")
		return page_factory

	def test_page_classes(self, page_factory):
		print(page_classes)
		assert True 
















class Device():
	def __init__(self):
		self.application_name = "fibe"
		self.application_version = "0"
		self.platform_name = "android"
		self.platform_version = "0"
		self.vendor_name = "samsung"
		self.vendor_Version = "0"