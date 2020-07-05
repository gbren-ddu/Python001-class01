# -*- coding: utf-8 -*-

from selenium import webdriver
import time

def weibo_login(username, password):
    # 打开登录页
    browser = webdriver.Chrome()
    browser.get('https://shimo.im/login?from=home')
    browser.implicitly_wait(5)
    time.sleep(1)
    # 填写登录信息：用户名、密码
    browser.find_element_by_xpath('//input[@name="mobileOrEmail"]').send_keys(username)
    browser.find_element_by_xpath('//input[@name="password"]').send_keys(password)
    time.sleep(1)
    # 点击登录
    browser.find_element_by_xpath('//button[@class="sm-button submit sc-1n784rm-0 bcuuIb"]').click()
    time.sleep(1)

if __name__ == "__main__":
    #使用绝对路径也可以，但从项目开发角度来说这个方式不好，还是放到虚拟环境当中合适
    #browser = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver')
    # 设置用户名、密码
    shimo_user_info = {
        "username": "624984128@qq.com",
        "password": "******"
    }
    username = shimo_user_info["username"]
    password = shimo_user_info["password"]
    weibo_login(username, password)