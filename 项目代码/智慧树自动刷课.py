
from importlib.metadata import distribution
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

s = Service("D:\python\爬虫项目\项目代码\chromedriver.exe")
option = webdriver.ChromeOptions()
# 防止打印一些无用的日志
option.add_experimental_option(
    "excludeSwitches", ['enable-automation', 'enable-logging'])
driver = webdriver.Chrome(service=s, chrome_options=option)


def load(user_name, password):  # 登录
    log = driver.find_element(
        By.XPATH, '//*[@id="lUsername"]').send_keys(user_name)
    time.sleep(1)
    password = driver.find_element(
        By.XPATH, '//*[@id="lPassword"]').send_keys(password)
    time.sleep(1)
    # 输入验证码
    driver.find_element(By.XPATH, '//*[@id="f_sign_up"]/div[1]/span').click()
    time.sleep(5)


def open_needlearn(url):  # 打开课程中的未完成
    driver.get(url)
    print('打开课程')
    driver.find_element(
        By.XPATH, '/html/body/div[1]/div/div/div/div[4]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/div/div[1]/div[3]').click()
    print('打开未完成')
    try:
        driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div/div/div[4]/div[1]/div[2]/div[2]/div[1]').click()
    except:
        return False


def move_to_veido():  # 移动到视频窗口
    time.sleep(3)
    handles = driver.window_handles  # 获取所有的窗口
    driver.switch_to.window(handles[1])  # 切换到下标为1的窗口
    controlsBar = driver.find_element(
        By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div/div/div/video')
    ActionChains(driver).move_to_element(controlsBar).perform()


def play():  # 播放
    move_to_veido()
    time.sleep(3)
    start_status = driver.find_element(
        By.XPATH, '//*[@id="playButton"]').get_attribute('class')
    start_button = driver.find_element(By.XPATH, '//*[@id="playButton"]')
    if start_status.find('playButton') != -1:
        print('当前静止')
        move_to_veido()
        time.sleep(3)
        start_button.click()
        print('点击播放成功\t\t√')


def get_nowtime():  # 获取当前播放时间
    move_to_veido()
    now_time = driver.find_element(
        By.XPATH, '//*[@id="vjs_mediaPlayer"]/div[10]/div[4]/span[1]').text
    return now_time


def get_overtime():  # 获取视频长度
    move_to_veido()
    over_time = driver.find_element(
        By.XPATH, '//*[@id="vjs_mediaPlayer"]/div[10]/div[4]/span[2]').text
    print(over_time)
    return over_time


def fasterPlay():  # 倍速播放
    try:
        move_to_veido()
        speed = driver.find_element(
            By.XPATH, ' //div[@class="speedBox"]/div/div[1]')
        speedbox = driver.find_element(By.XPATH, '//div[@class="speedBox"]')
        time.sleep(2)
        move_to_veido()
        ActionChains(driver).move_to_element(speedbox).perform()
        speed.click()
        print('成功切换成'+speed.text+'倍速\t√')
    except:
        print('切换成' + speed.text + '倍速失败，稍后将重试\t✘')


def noVoice():  # 静音
    try:
        voice_status = driver.find_element(
            By.XPATH, '//*[@id="vjs_mediaPlayer"]/div[10]/div[8]/div[1]').get_attribute('class')
        voice_buttton = driver.find_element(
            By.XPATH, '//*[@id="vjs_mediaPlayer"]/div[10]/div[8]/div[1]')
        print(voice_status)
        if voice_status.find('volumeNone') == -1:
            print('此时非静音')
            time.sleep(2)
            move_to_veido()
            voice_buttton.click()
            print('静音成功\t\t\t√')
    except:
        print('静音失败，稍后将重试\t\t✘')


if __name__ == "__main__":
    url = 'https://passport.zhihuishu.com/login'
    driver.get(url)
    time.sleep(1)
    # user_name = input("input your user name:")
    user_name = '15167690003'
    # password = input("input your password:")
    password = 'Wzq1208738104'
    load(user_name, password)  # 登录
    print('登录成功')
    time.sleep(3)
    course_url = 'https://wenda.zhihuishu.com/stu/courseInfo/studyResource?courseId=10240073'  # 课程网址
    while(True):
        handles = driver.window_handles  # 获取所有的窗口
        driver.switch_to.window(handles[0])
        open_needlearn(course_url)
        time.sleep(1)
        try:  # 如果是视频进行下列操作
            play()
            fasterPlay()
            noVoice()
            time.sleep(1)
            over_time = get_overtime()
            while (True):
                now_time = get_nowtime()
                if now_time == over_time:
                    handles = driver.window_handles  # 获取所有的窗口
                    driver.switch_to.window(handles[1])
                    driver.close()
                    print('播放完成')
                    break
                time.sleep(5)
        except:  # 如果不是则关闭
            handles = driver.window_handles  # 获取所有的窗口
            driver.switch_to.window(handles[1])
            driver.close()
            continue
