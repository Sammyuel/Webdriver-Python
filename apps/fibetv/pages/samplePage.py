
def pageMethod1():
	pass

def pageMethod2():
	pass

def pageMethod3():
	pass

def pageMethod4():
	pass

def pageMethod5():
	pass

def fibetv():
	pass

def pageMethod6():
	pass

def goto_home():
	print("home")

class PageFactory():
	pass

class TestPage():
	def __dir__(self):
		return ["one","two","three"]
	def testMethodOne():
		print("1")
	def testMethodTwo():
		print("2")
	def testMethodThree():
		print("3")
	class SubClass():
		pass

class TestPageAppName():
	def testMethodOne():
		print("11")
	def testMethodTwo():
		print("22")
	def testMethodThree():
		print("33")
class Abc():
	pass


def pageFactory():
	return TestPageAppName(TestPage(PageFactory))


