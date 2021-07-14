from selenium import webdriver
import time

# 实例化一个浏览器
driver1 = webdriver.Chrome(executable_path="./chromedriver")
# driver2 = webdriver.Firefox(executable_path="./geckodriver_mac")

# 发送请求
url = "http://www.baidu.com"
driver1.get(url)
# driver2.get(url)

# 让百度搜索python
driver1.find_element_by_id("kw").send_keys("python")
driver1.find_element_by_id("su").click()

time.sleep(10)
# 退出浏览器
driver1.quit()
# driver2.quit()
