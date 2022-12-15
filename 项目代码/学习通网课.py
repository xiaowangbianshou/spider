from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# 设置引擎为Chrome，真实地打开一个Chrome浏览器（把Chrome浏览器设置为引擎，然后赋值给变量driver。driver是实例化的浏览器）
s = Service("D:\python\爬虫项目\项目代码\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('https://passport2.chaoxing.com/login?fid=&refer=https://www.baidu.com/link?url=ZncGI00TDDZOjhcCNl1SaYkk6CkLiVYN57yZrAD8FJgppa4-x3kay4TyG8f7wBne&wd=&eqid=ffff44150013411c0000000463974882')  # 打开网页
# driver.maximize_window()  # 浏览器最大化
time.sleep(1)

user = '15167690003'
pwd = '1208738104.wzq'
log = driver.find_element(By.ID, "phone").send_keys(user)
time.sleep(1)
password = driver.find_element(By.ID, 'pwd').send_keys(pwd)
time.sleep(1)

# 输入验证码
driver.find_element(By.ID, "loginBtn").click()
