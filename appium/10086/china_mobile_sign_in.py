from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

N = 30


class ChinaMobile:
    def __init__(self):
        self.desired_caps = {
            "platformName": "Android",
            "platformVersion": "6.0.1",
            "deviceName": "emulator-5554",
            "appPackage": "com.greenpoint.android.mc10086.activity",
            "appActivity": "com.mc10086.cmcc.base.StartPageActivity",
            "noReset": "True"
        }
        # 指定Appium Server
        self.server = 'http://localhost:4723/wd/hub'
        # 新建一个driver
        self.driver = webdriver.Remote(self.server, self.desired_caps)

    def run(self):
        # 点击广告弹窗
        time.sleep(N)
        self.driver.find_element_by_id("com.greenpoint.android.mc10086.activity:id/close_btn").click()
        # self.driver.find_element_by_xpath(
        #     "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageView").click()
        time.sleep(N)

        # 点击我的
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.RelativeLayout[5]/android.widget.ImageView").click()
        time.sleep(N)

        # 签到
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView[3]").click()
        time.sleep(N)
        print("签到成功")

    def run_by_coordinate(self):
        time.sleep(N)
        # 关闭弹窗
        print("关闭弹窗")
        TouchAction(self.driver).tap(x=581, y=1683).perform()
        time.sleep(N)
        # 点击我的
        print("点击我的")
        TouchAction(self.driver).tap(x=1045, y=1774).perform()
        time.sleep(N)
        # 签到
        print("签到")
        TouchAction(self.driver).tap(x=1087, y=370).perform()
        time.sleep(N)


if __name__ == '__main__':
    china_mobile = ChinaMobile()
    try:
        china_mobile.run_by_coordinate()
    except Exception as e:
        print(e)
    finally:
        china_mobile.driver.quit()
