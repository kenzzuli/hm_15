from selenium import webdriver
import time

# 实例化
driver = webdriver.Chrome(executable_path="./chromedriver")

# 发送请求
url = "https://mail.qq.com/"
driver.get(url)

# 定位iframe
iframe = driver.find_element_by_id("login_frame")
# 切换到iframe
driver.switch_to.frame(iframe)
# 定位用户名，密码输入框和登录按钮
driver.find_element_by_id("u").send_keys("username")
driver.find_element_by_id("p").send_keys("password")
driver.find_element_by_id("login_button").click()

time.sleep(10)
driver.quit()
