"""
{
  "platformName": "android",
  "appium:appActivity": "com.atg.world.activity.SplashActivity",
  "appium:appWaitDuration": "5000",
  "appium:appExecTimeout": "50000",
  "appium:appPackage": "com.ATG.World",
  "appium:deviceName": "emulator-5554",
  "appium:driver": "http://localhost:4723/wd/hub"
}
"""

import time
from appium import webdriver

desire_cap = {
    "platformName": "android",
    "appium:appActivity": "com.atg.world.activity.SplashActivity",
    "appium:appWaitDuration": "5000",
    "appium:appExecTimeout": "50000",
    "appium:appPackage": "com.ATG.World",
    "appium:deviceName": "emulator-5554",
    "appium:driver": "http://localhost:4723/wd/hub"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities=desire_cap)
time.sleep(2)
driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button").click()
time.sleep(2)

driver.find_element_by_id("com.ATG.World:id/getStartedTv").click()
time.sleep(2)

driver.find_element_by_id("com.ATG.World:id/login_email").click()
time.sleep(2)

# login via email
driver.find_element_by_id("com.ATG.World:id/email_phone_login").send_keys("shreyas89572@gmail.com")
driver.find_element_by_id("com.ATG.World:id/signinbutton").click()
time.sleep(2)
driver.find_element_by_id("com.ATG.World:id/password").send_keys("Pass@123")

time.sleep(2)
driver.find_element_by_id("com.ATG.World:id/passwordloginbutton").click()
time.sleep(3)

# got it click
driver.find_element_by_id("com.ATG.World:id/btnGotit").click()
time.sleep(5)
driver.find_element_by_id("com.ATG.World:id/fab").click()
time.sleep(3)
driver.find_element_by_id("com.ATG.World:id/image_fab_clicked").click()
time.sleep(3)

driver.find_element_by_id("com.ATG.World:id/image_cell").click()
driver.implicitly_wait(5)


driver.find_element_by_id("com.ATG.World:id/toolbar_post_action").click()
driver.implicitly_wait(5)


driver.find_element_by_id("com.ATG.World:id/caption_edit_text").send_keys("First Post via Appium")
driver.implicitly_wait(2)

driver.find_element_by_id("com.ATG.World:id/toolbar_post_action").click()
driver.implicitly_wait(5)

driver.find_element_by_id("com.ATG.World:id/selection_done_btn").click()
time.sleep(3)

driver.back()
time.sleep(2)

driver.find_element_by_id("com.ATG.World:id/homeBottomSheetFragment").click()
driver.implicitly_wait(5)

driver.find_element_by_id("com.ATG.World:id/myPostsLabelTextView").click()

print("posted successfull")
time.sleep(10)

driver.quit()