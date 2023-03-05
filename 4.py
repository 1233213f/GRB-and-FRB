from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window()  # 设置浏览器大小：全屏
browser.get('https://www.baidu.com')

# 定位输入框
input_box = browser.find_element_by_id('kw')
try:
    # 输入内容：selenium
    input_box.send_keys('selenium')
    print('搜索关键词：selenium')
except Exception as e:
    print('fail')
# 输出内容：搜索关键词：selenium

# 定位搜索按钮
button = browser.find_element_by_id('su')
try:
    # 点击搜索按钮
    button.click()
    print('成功搜索')
except Exception as e:
    print('fail搜索')
# 输出内容：成功搜索

# clear()：清空输入框
try:
    input_box.clear()
    print('成功清空输入框')
except Exception as e:
    print('fail清空输入框')
# 输出内容：成功清空输入框