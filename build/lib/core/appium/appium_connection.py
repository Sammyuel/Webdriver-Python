from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "8.0.0"
caps["udid"] = "988e163831454c3134"
caps["deviceName"] = "Galaxy S8"
caps["appPackage"] = "com.quickplay.android.bellmediaplayer.canary"
caps["appActivity"] = "ca.bell.fiberemote.boot.BootstrapActivity"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

el1 = driver.find_element_by_id("com.quickplay.android.bellmediaplayer.canary:id/dialog_rational_phone_button")
el1.click()
el2 = driver.find_element_by_id("com.quickplay.android.bellmediaplayer.canary:id/dialog_rational_location_button")
el2.click()

driver.quit()




class AppiumConnection(webdriver.Remote):
	""" Returns appium driver """