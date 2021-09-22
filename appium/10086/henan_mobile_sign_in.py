from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

N = 20


class ChinaMobile:
    def __init__(self):
        self.desired_caps = {
            "platformName": "Android",
            "platformVersion": "6.0.1",
            "deviceName": "emulator-5554",
            "appPackage": "com.xinhang.mobileclient",
            "appActivity": ".ui.activity.HomeActivity",
            "noReset": "True"
        }
        # 指定Appium Server
        self.server = 'http://localhost:4723/wd/hub'
        # 新建一个driver
        self.driver = webdriver.Remote(self.server, self.desired_caps)

    def run_by_coordinate(self):
        time.sleep(N)

        # 关闭广告
        print("点击关闭广告")
        TouchAction(self.driver).tap(x=957, y=400).perform()
        time.sleep(N)

        # 不升级
        print("点击不升级")
        TouchAction(self.driver).tap(x=1011, y=411).perform()
        time.sleep(N)

        # 我的
        print("点击我的")
        TouchAction(self.driver).tap(x=1045, y=1800).perform()
        time.sleep(N)

        # 签到有礼
        print("点击签到有礼")
        TouchAction(self.driver).tap(x=159, y=796).perform()
        time.sleep(N)

        # 立即签到
        print("点击立即签到")
        TouchAction(self.driver).tap(x=577, y=1045).perform()
        time.sleep(N)


if __name__ == '__main__':
    china_mobile = ChinaMobile()
    try:
        china_mobile.run_by_coordinate()
    except Exception as e:
        print(e)
    finally:
        china_mobile.driver.quit()
