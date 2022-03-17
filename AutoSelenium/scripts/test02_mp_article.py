import page
from page.page_in import PageIn
from tools.get_driver import GetDriver


class TestMpArticle:
    # 初始化
    def setup_class(self):
        # 1获取driver
        driver = GetDriver.get_web_driver(page.url_mp)
        # 2获取统一入口类对象
        self.page_in = PageIn(driver)
        # 3获取antiparticle对象并调用登录成功方法
        self.page_in.page_get_pageMpLogin().page_mp_login_success()
        # 4获取antiparticle页面对象
        self.article = self.page_in.page_get_PageMpArticle()

    # 结束
    def teardown_class(self):
        GetDriver.quit_web_driver()

    # 测试发布文章方法
    def test_mp_article(self, title='111', content="今晚顿火锅"):
        # 调用发布文章方法
        self.article.page_mp_article(title, content)
        # 查看断言信息
        print("发布文章结果为：", self.article.page_get_info())
