import importlib
import inspect


print("bye")



def importer():
	print("what")
	print("byfefefe")
	return importlib.import_module('test')



testfile = importer()





gg = [m[0] for m in inspect.getmembers(testfile, inspect.isclass)]

print(gg)


#print(getattr(testfile, gg))

"""
print("".join(filter(lambda x: eval(x).isclass, dir(testfile))))
"""