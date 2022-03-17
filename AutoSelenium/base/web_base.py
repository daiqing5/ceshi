import time

from selenium.webdriver.common.by import By

from base.base import Base


class WebBase(Base):
    """以下为web专属方法"""

    # 根据显示文本指定元素
    def web_base_click_element(self, placeholder_text, click_text):
        # 1点击复选框
        loc = By.CSS_SELECTOR, "[placeholder='{}}']".format(placeholder_text)
        self.base_click(loc)
        # 2暂停
        time.sleep(1)
        # 3点击包含显示文本
        loc = By.XPATH, "//*[text()={}]".format(click_text)
        self.base_click(loc)
