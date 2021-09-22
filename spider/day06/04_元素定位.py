from selenium import webdriver
import time

# 实例化一个浏览器
driver = webdriver.Chrome(executable_path="./chromedriver")

# 发送请求
url = "https://www.qiushibaike.com/text/"
driver.get(url)

# 查找多个元素
ret1 = driver.find_elements_by_xpath("//div[@class='content']/span")
print(ret1)
for span in ret1:
    # 获取元素中的文本
    print(span.text)

ret2 = driver.find_elements_by_class_name("contentHerf")
for a in ret2:
    # 获取元素中的href属性
    print(a.get_attribute("href"))

driver.quit()
