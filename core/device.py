from .platforms.android import Android
from .platforms.android import * 
from .platforms.ios import *

class Device():
	def __init__(self, app_info):
		self.application_name = app_info['application_name']
		self.application_version = app_info['application_version']
		self.platform_name = app_info['platform_name']
		self.platform_version = app_info['platform_version']
		self.vendor_name = app_info['vendor_name']
		self.vendor_version = app_info['vendor_version']

	def start_device(self, devices_info):
		backend = devices_info['backend']
		platform = devices_info['platform_name']
		vendor = devices_info['vendor_name']
		device = self.create_device(backend, platform, vendor)
		return device


	def create_device(self, backend, platform, vendor):
		if backend == 'selenium':
			vendor += 'selenium'
		try:


	def default_device_class(self):
		def initializer(self, device_info):
			super(self.vendor_name, self).__init__(device_info)
		device_class = type(self.vendor_name, (Android), {'__init__': initializer})
		return device_class
