from selenium import webdriver

import time

driver = webdriver.Chrome(executable_path="./chromedriver")
url = "https://www.bilibili.com/v/dance/otaku/#/"
driver.get(url)

# selenium会等待第一个页面完全加载后，再从页面找元素
print(driver.find_element_by_xpath("//div[@id='videolist_box']//div[@class='l-item']//a").get_attribute("href"))

# 翻页
driver.find_element_by_xpath("//button[@class='nav-btn iconfont icon-arrowdown3']").click()

# 点击翻页后，从下一页找相同的元素，页面还没加载完就直接找，大概率会报错，所以，等几秒
time.sleep(5)  # ✅
print(driver.find_element_by_xpath("//div[@id='videolist_box']//div[@class='l-item']//a").get_attribute("href"))

# 退出
driver.quit()
