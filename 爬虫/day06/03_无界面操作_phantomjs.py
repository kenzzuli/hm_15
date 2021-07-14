# UserWarning: Selenium support for PhantomJS has been deprecated,
# please use headless versions of Chrome or Firefox instead
from selenium import webdriver
import time

# 实例化一个浏览器
driver = webdriver.PhantomJS(executable_path="./phantomjs")

# 设置窗口大小
# driver.set_window_size(1920, 1080)

# 最大化窗口
driver.maximize_window()

# 发送请求
url = "http://www.baidu.com"
driver.get(url)
time.sleep(3)

# 元素定位
# driver.find_element_by_id("kw").send_keys("python")
# driver.find_element_by_id("su").click()

# # 页面截屏
# driver.save_screenshot("./baidu2.png")

# 获取cookie
cookies = driver.get_cookies()
# print(cookies)
# print("*" * 50)
# [{'domain': '.baidu.com', 'expires': 'Wed, 14 Jul 2021 03:35:51 GMT', 'expiry': 1626233751, 'httponly': False, 'name': 'BA_HECTOR', 'path': '/', 'secure': False, 'value': 'a4282g0h0g2g2h25n51gesjc70r'}, {'domain': 'www.baidu.com', 'expires': 'Sat, 24 Jul 2021 02:35:51 GMT', 'expiry': 1627094151, 'httponly': False, 'name': 'BD_UPN', 'path': '/', 'secure': False, 'value': '143254'}, {'domain': '.baidu.com', 'expires': 'Sun, 06 Jul 2053 02:35:50 GMT', 'expiry': 2635382150, 'httponly': False, 'name': 'BIDUPSID', 'path': '/', 'secure': False, 'value': '56EB7D02E774B9D5B7A2A0444CDAB846'}, {'domain': '.baidu.com', 'httponly': False, 'name': 'H_PS_PSSID', 'path': '/', 'secure': False, 'value': '34268_33764_34224_34004_34073_34106'}, {'domain': 'www.baidu.com', 'httponly': False, 'name': 'BD_HOME', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.baidu.com', 'expires': 'Thu, 14 Jul 2022 02:35:49 GMT', 'expiry': 1657766149, 'httponly': False, 'name': 'BAIDUID', 'path': '/', 'secure': False, 'value': '96D96D39F4ED02CD5FC6D214BC96DF8D:FG=1'}, {'domain': '.baidu.com', 'expires': 'Mon, 01 Aug 2089 05:49:55 GMT', 'expiry': 3773713795, 'httponly': False, 'name': 'PSTM', 'path': '/', 'secure': False, 'value': '1626230149'}]
# 列表中包含多个字典，每个字典是一条cookie，我们只需要里面的name和value对应的值构成键值对
cookies = {i['name']: i['value'] for i in cookies}
print(cookies)
# {'BA_HECTOR': 'a40c852gaga40h25oe1getoel0q', 'BIDUPSID': '56EB7D02E774B9D5B7A2A0444CDAB846', 'BD_UPN': '143254', 'H_PS_PSSID': '34269_34099_33970_34223_31254_34004_34094_26350_34242', 'BD_HOME': '1', 'BAIDUID': '14F95F9ADCF5DBAA8310CDDDFB1A5FAF:FG=1', 'PSTM': '1626268092'}

# 获取html字符串
# print(driver.page_source)  # 是浏览器中elements的内容（包含多次请求的结果），不仅是单个请求对应的响应。✅

# 获取当前url（前面通过元素定位的方式操作了浏览器，浏览器从百度首页跳转到了搜索结果页，当前url就是搜索结果页的url）
# print(driver.current_url)
# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=python&fenlei=256&rsv_pq=9961ca1200055629&rsv_t=d44eLWHMvZvZHjpA4SitB%2FuLd5zH5Ev7Jkh9ANpP792d5CnLxblBKFUOBtg&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_sug3=6&rsv_btype=i&inputT=78&rsv_sug4=78

# time.sleep(3)
# 退出浏览器
driver.quit()
