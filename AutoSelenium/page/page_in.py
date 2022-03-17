from page.page_mp_login import PageMpLogin
from page.page_mp_article import PageMpArticle

class PageIn:
    # 初始化
    def __init__(self, driver):
        self.driver = driver

    # 获取PageMpLogin对象
    def page_get_pageMpLogin(self):
        return PageMpLogin(self.driver)

        # Page_get_PageMpArticle
    def page_get_PageMpArticle(self):
        return PageMpArticle(self.driver)

