from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

N = 10


class Shisu_Health_Sign_In:
    def __init__(self):
        # 初始化配置，设置Desired Capabilities参数
        self.desired_caps = {
            "platformName": "Android",
            "platformVersion": "6.0.1",
            "deviceName": "emulator-5554",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "noReset": "True"
        }
        # 指定Appium Server
        self.server = 'http://localhost:4723/wd/hub'
        # 新建一个driver
        self.driver = webdriver.Remote(self.server, self.desired_caps)

    def run(self):
        # 工作台
        el1 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[3]/android.widget.RelativeLayout/android.widget.TextView")
        el1.click()
        time.sleep(N)
        # 学生健康打卡
        el2 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView")
        el2.click()
        time.sleep(N)

        # 地理位置授权
        try:
            self.driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[3]/android.widget.TextView[2]").click()
        except Exception:
            print("地理位置授权设置失败¬")
        time.sleep(N)

        # 上报列表
        el3 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.ListView/android.view.View[2]/android.view.View")
        el3.click()
        time.sleep(N)

        # 修改打卡
        print("滑动中...")
        TouchAction(self.driver).press(x=434, y=1842).move_to(x=479, y=359).release().perform()

        TouchAction(self.driver).press(x=423, y=1819).move_to(x=464, y=370).release().perform()

        TouchAction(self.driver).press(x=577, y=1713).move_to(x=902, y=664).release().perform()

        TouchAction(self.driver).press(x=536, y=1789).move_to(x=638, y=902).release().perform()

        TouchAction(self.driver).press(x=796, y=1736).move_to(x=819, y=525).release().perform()

        TouchAction(self.driver).press(x=868, y=1812).move_to(x=913, y=498).release().perform()
        try:
            el0 = self.driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[73]")
            el0.click()
            time.sleep(N)
        except Exception:
            print("修改打卡")

        # 腋下体温
        el4 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.widget.EditText[1]")
        el4.send_keys('36.0')
        print("设置腋下温度")
        time.sleep(N)
        # 今天是否有发烧咳嗽乏力
        el5 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[14]/android.view.View[1]")
        el5.click()
        print("设置今天是否有发烧乏力")
        time.sleep(N)

        try:
            # 今日是否在校
            el6 = self.driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[42]/android.view.View[1]")
            el6.click()
            print("设置今天是否在校")
            time.sleep(N)
        except Exception as e:
            print("今日是否在校设置失败")

        # 当前所在位置
        el7 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.widget.EditText[4]")
        el7.send_keys("上海市松江区广富林街道上外小别墅10号上海外国语大学松江校区")
        print("设置当前所在位置")
        time.sleep(N)
        # 提交打卡
        el8 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[73]")
        el8.click()

        print("打卡成功")

        time.sleep(300)

    def run_with_coordinate(self):
        time.sleep(N)
        # 工作台
        print("点击工作台")
        TouchAction(self.driver).tap(x=736, y=1778).perform()
        time.sleep(N)

        # 学生健康打卡
        print("学生健康打卡")
        TouchAction(self.driver).tap(x=211, y=419).perform()
        time.sleep(N)

        # 获取地理位置
        print("允许获取地理位置")
        TouchAction(self.driver).tap(x=819, y=1110).perform()
        time.sleep(N)

        # 点击每日健康打卡
        print("点击学生每日健康打卡上报列表")
        TouchAction(self.driver).tap(x=898, y=355).perform()
        time.sleep(N)

        # 滑动窗口
        print("滑动窗口...")
        TouchAction(self.driver).press(x=611, y=1223).move_to(x=1000, y=132).release().perform()
        time.sleep(N)

        # 腋下温度
        print("设置腋下温度")
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.FrameLayout/com.tencent.tbs.core.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.widget.EditText").send_keys(
            "36.1")
        time.sleep(N)

        # 滑动窗口
        print("滑动窗口...")
        TouchAction(self.driver).press(x=589, y=1797).move_to(x=627, y=959).release().perform()
        time.sleep(N)

        # 今日是否发烧
        print("设置今天是否发烧")
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[14]/android.view.View[1]").click()
        time.sleep(N)

        # 滑动窗口
        print("滑动窗口...")
        TouchAction(self.driver).press(x=823, y=1827).move_to(x=1098, y=751).release().perform()
        time.sleep(N)

        # 年级
        print("设置年级")
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[31]/android.view.View[1]").click()
        time.sleep(N)

        # 滑动窗口
        print("滑动窗口...")
        TouchAction(self.driver).press(x=879, y=1778).move_to(x=917, y=630).release().perform()
        time.sleep(N)

        # 今日是否在校
        print("设置今日是否在校")
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[41]/android.view.View[1]").click()
        time.sleep(N)

        # 滑动
        print("滑动窗口...")
        TouchAction(self.driver).press(x=615, y=1804).move_to(x=921, y=619).release().perform()
        time.sleep(N)

        print("滑动窗口...")
        TouchAction(self.driver).press(x=849, y=1830).move_to(x=532, y=653).release().perform()
        time.sleep(N)

        print("滑动窗口...")
        TouchAction(self.driver).press(x=755, y=1295).move_to(x=770, y=377).release().perform()
        time.sleep(N)

        print("滑动窗口...")
        TouchAction(self.driver).press(x=838, y=1272).move_to(x=868, y=355).release().perform()
        time.sleep(N)

        # 当前所在位置
        print("设置当前所在位置")
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.widget.EditText[4]").send_keys(
            "上海市松江区广富林街道上外小别墅10号上海外国语大学松江校区")
        time.sleep(N)

        # 提交打卡
        print("提交打卡")
        TouchAction(self.driver).tap(x=562, y=1797).perform()
        time.sleep(N)


if __name__ == '__main__':
    sign = Shisu_Health_Sign_In()
    try:
        sign.run_with_coordinate()
    except Exception as e:
        print(e)
    finally:
        sign.driver.quit()
