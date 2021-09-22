import time
from appium import webdriver
from tqdm import tqdm


class DouyinAction():
    """自动滑动，并获取抖音短视频发布者的id"""

    def __init__(self, nums: int = None):
        # 初始化配置，设置Desired Capabilities参数
        self.desired_caps = {
            'platformName': 'Android',
            'deviceName': 'SM-G955F',
            'appPackage': 'com.ss.android.ugc.aweme',
            'appActivity': '.main.MainActivity'
        }
        # 指定Appium Server
        self.server = 'http://localhost:4723/wd/hub'
        # 新建一个driver
        self.driver = webdriver.Remote(self.server, self.desired_caps)
        # 获取模拟器/手机的分辨率(px)
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        print(width, height)
        # 设置滑动初始坐标和滑动距离
        self.start_x = width // 2  # 屏幕宽度中心点
        self.start_y = height // 3 * 2  # 屏幕高度从上开始到下三分之二处
        self.distance = height // 2  # 滑动距离：屏幕高度一半的距离
        # 设置滑动次数
        self.nums = nums

    def comments(self):
        # 同意个人隐私保护
        time.sleep(10)
        self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/beo').click()

        # 同意拨打电话和管理电话
        time.sleep(10)
        self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()

        # 同意使用位置
        time.sleep(10)
        self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        time.sleep(10)

    def scroll(self):
        # 无限滑动
        i = 0
        while True:
            # 模拟滑动
            print('滑动ing...')
            print('-' * 50)
            self.driver.swipe(self.start_x, self.start_y,
                              self.start_x, self.start_y - self.distance)
            time.sleep(5)
            self.get_infos()  # 获取视频发布者的名字
            print('-' * 50)
            # 设置延时等待
            time.sleep(5)
            # 判断是否退出
            if self.nums is not None and self.nums == i:
                break
            i += 1

    def get_infos(self):
        # 获取视频的各种信息：使用appium desktop定位元素
        print(self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/title').text)  # 发布者名字
        print(self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/bvh').text)  # 点赞数
        print(self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/b92').text)  # 留言数
        print(self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/a9_').text)  # 视频名字，可能不存在，报错

    def main(self):
        self.comments()  # 点击一次屏幕，确保页面的展示
        # 用来等待用户搜索感兴趣的内容
        # for i in tqdm(range(60)):
        #     time.sleep(1)
        self.scroll()  # 滑动
        self.driver.quit()  # 关闭


if __name__ == '__main__':
    action = DouyinAction(nums=5)
    action.main()
