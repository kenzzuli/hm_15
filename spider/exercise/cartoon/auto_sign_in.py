from selenium import webdriver
from selenium.webdriver import ChromeOptions
import time

SLEEP_TIME = 10

# 实例化一个浏览器
opts = ChromeOptions()
# opts.add_argument("--headless")
driver1 = webdriver.Chrome(executable_path="./chromedriver", options=opts)
# 发送请求
url = "https://www.umr18.cn/login.html"
driver1.get(url)
time.sleep(SLEEP_TIME)
# 让百度搜索python
driver1.find_element_by_id("mobile").send_keys("zhuangzhuang")
driver1.find_element_by_id("pass").send_keys('qujzaD-hujre7-vydgib')
driver1.find_element_by_xpath("//li[@class='login-submit']/div").click()

time.sleep(SLEEP_TIME)

try:
    driver1.find_element_by_xpath("//a[@class='btn btn-sign']").click()
except:
    pass

time.sleep(SLEEP_TIME)
driver1.save_screenshot("./sign.png")
# 退出浏览器
driver1.quit()
