import allure
from selenium.webdriver.support.wait import WebDriverWait

from tools.log import GetLog

log = GetLog.get_logger()


class Base:
    def __init__(self, driver):
        log.info("正在获取driver：{}".format(driver))
        self.driver = driver

    def base_find(self, loc, timeout=30, poll=0.5):
        log.info("正在查找元素：{}".format(loc))
        return WebDriverWait(self.driver, timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*loc))

    def base_input(self, loc, value):
        el = self.base_find(loc)
        log.info("正在对：{}元素执行情空操作！".format(loc))
        el.clear()
        log.info("正在对：{}元素执行输入！".format(loc, value))
        el.send_keys(value)

    def base_click(self, loc):
        log.info("正在对：{}元素执行点击操作！".format(loc))
        self.base_find(loc).click()

    def base_get_text(self, loc):
        log.info("正在对：{}元素执行获取文本操作！,获取文本的值：{}".format(loc, self.base_find(loc).text))
        return self.base_find(loc).text

    def base_get_img(self):
        log.error("断言出错，正在执行截图操作！")
        # 调用截图方法
        self.driver.get_screenshot_as_file("./image/err.png")
        log.error("断言出错，正在将错误图片写入allure报告！")
        # 调用图片写入报告方法
        self.__base_write_img()

    # 将图片写入报告方法（私有）
    def __base_write_img(self):
        # 获取图片文件流
        with open("./image/err.png", "rb") as f:
            # 调用allure.attch附加方法
            allure.attach("错误原因:", f.read(), allure.attachment_type.PNG)
