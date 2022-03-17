import time
import page

from base.web_base import WebBase
from tools.log import GetLog

log = GetLog.get_logger()


# 操作步骤单独封装，实现组合业务方法，方便在脚本层实现调用
class PageMpLogin(WebBase):
    # 用户名
    def page_input_username(self, username):
        # 调用父类中输入方法
        self.base_find(page.mp_username, username)

    # 密码
    def page_input_code(self, code):
        self.base_input(page.mp_code, code)

    # 点击按钮
    def page_click_login_btn(self):
        time.sleep(1)
        self.base_click(page.mp_login_btn)

    # 获取昵称--》测试脚本层调用
    def page_get_nickname(self):
        return self.base_get_text(page.mp_nickname)

    # 组合业务-->发布文章依赖使用
    def page_mp_login_success(self, username='13800000002', code='123456'):
        log.info("正在调用用户名：{} 密码：{}".format(username, code))
        self.page_input_username(username)
        time.sleep(3)
        self.page_input_code(code)
        self.page_click_login_btn()
