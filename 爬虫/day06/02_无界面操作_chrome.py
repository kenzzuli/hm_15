from selenium import webdriver
from selenium.webdriver import ChromeOptions
import time

# 实例化一个浏览器
opts = ChromeOptions()
opts.add_argument("--headless")
driver1 = webdriver.Chrome(executable_path="./chromedriver", options=opts)

# 发送请求
url = "http://www.baidu.com"
driver1.get(url)

# 让百度搜索python
driver1.find_element_by_id("kw").send_keys("python")
driver1.find_element_by_id("su").click()
time.sleep(10)
driver1.save_screenshot("./baidu.png")

print(driver1.current_url)

# time.sleep(3)
# 退出浏览器
driver1.quit()
