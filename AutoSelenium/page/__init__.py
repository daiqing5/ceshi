
from selenium.webdriver.common.by import By

'''后台链接'''
url_mp = 'http://ihrm-test.itheima.net/#/login'

'''
以下数据为模块配置数据
'''
# 用户名
mp_username = (By.CSS_SELECTOR, "[placeholder='username']")
# 验证码
mp_code = (By.CSS_SELECTOR, "[placeholder='password']")
# 登录按钮
mp_login_btn = (By.XPATH, "//*[@id='app']/div/form/button[1]")
# 昵称
mp_nickname = (By.XPATH, "//*[@id='app']/div/div[2]/ul/div[3]/div[5]/span")

# 内容管理
mp_content_manage = By.XPATH, " //span[text()='内容管理']/.."
# 发布文章
mp_publish_article = By.XPATH, "//*[ contains (text( )，'发布文章')]"
# 文章title
mp_title = By.CSS_SELECTOR, " [placeholder='文章名称' ]"
# iframe
mp_iframe = By.CSS_SELECTOR, "#publishTinymce_ifr"
# 文章内容定位body，勿定位到p标题
mp_content = By.CSS_SELECTOR, "#tinymce"
# 封面
mp_cover = By.XPATH, "//*[text()='自动']"
mp_submit = By.XPATH, "//*[text()='发表']/.."
mp_result = By.XPATH, "//*[contains(text(),'新增文章成功')]"
