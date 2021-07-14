from selenium import webdriver
import time

# 实例化
driver = webdriver.Chrome(executable_path="./chromedriver")

url = "https://www.douban.com/"
driver.get(url)

# 定位iframe
# iframe里面的内容和外面的内容属于不同的网页，默认是定位不到的，需要切换到iframe里面才可以
iframe = driver.find_element_by_xpath("//div[@class='login']/iframe")

# 切换到iframe中
driver.switch_to.frame(iframe)

# 输入手机号
driver.find_element_by_xpath("//input[@name='phone']").send_keys("15890075005")
# 获取验证码
driver.find_element_by_link_text("获取验证码").click()

# 暂停几秒，手动输入验证码
time.sleep(20)

# 登录
driver.find_element_by_link_text("登录豆瓣").click()

# 等待进入登录后的界面
time.sleep(10)

# 获取cookies
cookies = {i['name']: i['value'] for i in driver.get_cookies()}
print(cookies)

# 退出
driver.quit()
