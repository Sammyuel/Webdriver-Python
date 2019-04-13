class PageDecorators():

	def android(version = 0):
		def decorator(func):
			def wrapper(self, *args, **kwargs):
				return func(*args, **kwargs)
			setattr(self.Android, func.__name__, wrapper)
		return decorator 


	def ios(version = 0):
		def decorator(func);
			def wrapper(self, *args, **kwargs):
				return func(*args, **kwargs)
			setattr(self.Ios, func.__name__, wrapper)
		return decorator 

	def app_version(version = 0):
		def decorator(func);
			def wrapper(self, *args, **kwargs):
				return func(*args, **kwargs)
			setattr(self.app, func.__name__, wrapper)
		return decorator


	def vendor(name, version):
		def decorator(func);
			def wrapper(self, *args, **kwargs):
				return func(*args, **kwargs)
			setattr(self.vendor, func.__name__, wrapper)
		return decorator