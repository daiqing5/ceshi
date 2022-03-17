from base.web_base import WebBase
import page
from time import sleep


class PageMpArticle(WebBase):
    # 点击内容管理
    def page_click_content_mange(self):
        sleep(1)
        self.base_click(page.mp_content_manage)

    # 点击发布文章
    def page_click_publish_article(self):
        sleep(1)
        self.base_click(page.mp_publish_article)

    # 输入标题
    def page_input_title(self, title):
        sleep(1)
        self.base_input(page.mp_title, title)

    # 输入内容
    def page_input_content(self, content):
        # 切换iframe
        iframe = self.base_find(page.mp_iframe)
        self.driver.switch_to.frame(iframe)
        # 输入内容
        sleep(1)
        self.base_input(page.mp_content, content)

        # 回到默认目录
        self.driver.switch_to.default_content()

    # 选择封面
    def page_click_cover(self):
        sleep(1)
        self.base_click(page.mp_cover)

    # 选择频道
    def page_click_channel(self):
        # 调用web封装方法
        self.web_base_click_element(placeholder_text="请选择", click_text="数据库")

    # 点击发表
    def page_click_submit(self):
        self.base_click(page.mp_submit)

    # 获取发表提示信息
    def page_get_info(self):
        return self.base_get_text(page.mp_result)

    # 组合业务方法
    def page_mp_article(self, title, content):
        self.page_click_content_mange()
        self.page_click_publish_article()
        self.page_input_title(title)
        self.page_input_content(content)
        self.page_click_cover()
        self.page_click_channel()
        self.page_click_submit()
        self.page_get_info()
