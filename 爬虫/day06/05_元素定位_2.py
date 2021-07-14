from selenium import webdriver

driver = webdriver.Chrome(executable_path="./chromedriver")

url = "https://www.baidu.com/s?ie=utf-8&wd=python"

driver.get(url)

# 查找 下一页 的链接
# 完整文本
ret = driver.find_element_by_link_text("下一页 >")
print(ret.get_attribute("href"))  # 获取到的url地址是自动补全后的

# 部分文本
ret2 = driver.find_element_by_partial_link_text("下一页")
print(ret2.get_attribute("href"))


driver.quit()
