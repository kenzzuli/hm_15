from selenium import webdriver
import time
import requests

# 实例化
driver = webdriver.Chrome(executable_path="./chromedriver")

url = "https://www.douban.com/"
driver.get(url)

# 定位frame
iframe = driver.find_element_by_xpath("//div[@class='login']/iframe")

# 切换到frame
driver.switch_to.frame(iframe)

# 输入手机号
driver.find_element_by_xpath("//input[@name='phone']").send_keys("15713792607")
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
# {'push_noty_num': '0', 'ap_v': '0,6.0', '_pk_id.100001.8cb4': '990dc2d222ba7047.1626269043.1.1626269089.1626269043.', 'ck': 'qqZ5', 'dbcl2': '"241998854:e5EslO/oqKA"', 'push_doumail_num': '0', '__gads': 'ID=8f221d909a1208f2-22ce64e757ca00ef:T=1626269089:S=ALNI_MZvAHBrgl7y-H6zFglTPsza1OGOlg', '_pk_ses.100001.8cb4': '*', 'bid': 'QpodTPyUzsE', 'll': '"108296"'}

# 退出
driver.quit()

profile_url = "https://www.douban.com/people/241998854/"
# 添加headers
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}

r = requests.get(url, headers=headers, cookies=cookies)
print(r.request.url)
print(r.url)
print(r.content.decode())
# 使用cookie登录成功，看到个人信息✅
# <span>sky_yang的帐号</span><span class="arrow"></span>
