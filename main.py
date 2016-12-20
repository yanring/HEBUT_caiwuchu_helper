# -*- coding:utf-8 -*-
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from splinter import Browser
import time

chromedriver_loc = '/home/yanzijie/bin/chromedriver'
driver = webdriver.Chrome(executable_path=chromedriver_loc)
browser = Browser('chrome')
timeout = 5


def splinter(url):
    while (1):

        browser.visit(url)

        start_time = time.clock()
        wait_until_visible_btn_visible(start_time, 1200)
        try:
            browser.find_by_css('.btns')[0].find_by_css('.nextDate')[0].click()
        except Exception, e:
            print('2' + e.__str__())
            # browser.reload()
            continue
        start_time = time.clock()
        wait_until_visible_by_id('dialog-message', start_time, 1200)
        wait_until_visible_by_id('UserID', start_time, 1200)
        time.sleep(2)
        try:
            print(browser.find_by_id('UserID')[0].fill('142317'))
            print(browser.find_by_id('Password')[0].fill('142317'))
            print(browser.find_by_text(u'确定')[0].click())
            time.sleep(3)
        except Exception, e:
            print('已跳过登录')
            print (e.__str__())
        wait_until_visible_qupiao(start_time, 1200)
        time.sleep(1)
        while browser.find_by_id('detailsInfo').find_by_tag('a')[0] == False :
            time.sleep(1)
            print ('detailsinfo not visible')
        time.sleep(3)
        try:
            print(browser.find_by_id('detailsInfo').find_by_tag('a')[0].click())
        except Exception, e:
            wait_until_visible_qupiao(start_time, 1200)
            time.sleep(1)
            print browser.is_element_present_by_tag('img')
            #browser.find_by_id('detailsInfo').find_by_tag('img')[0].click()
            print('4 已刷新')
            print e.__str__()
            time.sleep(2)
            continue

        start_time = time.clock()
        wait_until_visible_alert(start_time, 1200)
        try:
            alert = browser.get_alert()
            alert.accept()
        except Exception, e:
            print('5' + e.__str__())
            time.sleep(2)
            try:
                alert = browser.get_alert()
                print ('2333'+alert.text)
                alert.accept()
                print ('alert accpeted')
            except Exception:
                try:
                    alert = browser.get_alert()
                except Exception, e:
                    alert = browser.get_alert()
                    # print (type(alert.text().encode('utf-8')))
                    alert.accept()
                    print ('alert accpeted')


def wait_until_visible_btn_visible(start_time, delay):
    try:
        print("finding button")
        browser.find_by_css('.btns')[0].find_by_css('.nextDate')[0]
        print ('已找到button')
    except Exception, e:
        time.sleep(1)
        print (e.__str__())
        if time.clock() - start_time <= delay:
            wait_until_visible_btn_visible(start_time, delay)
        else:
            print ("timeout")


def wait_until_visible_by_id(id, start_time, delay):
    try:
        print("finding " + id)
        browser.find_by_id(id)
        print ("已找到"+id)
    except Exception, e:
        time.sleep(1)
        print (e.__str__())
        if time.clock() - start_time <= delay:
            wait_until_visible_by_id(id, start_time, delay)
        else:
            print ("timeout")


def wait_until_visible_qupiao(start_time, delay):
    try:
        print("finding 取票")
        browser.find_by_id('detailsInfo').find_by_tag('img')[0]
        print("已找到取票")
    except Exception, e:
        time.sleep(1)
        print ("still finding 取票")
        if time.clock() - start_time <= delay:
            wait_until_visible_qupiao(start_time, delay)
        else:
            print ("timeout")


def wait_until_visible_alert(start_time, delay):
    try:
        print (browser.get_alert())
        print("finding alert")

    except Exception, e:
        time.sleep(1)
        print ("still finding alert")
        if time.clock() - start_time <= delay:
            wait_until_visible_alert(start_time, delay)
        else:
            print ("timeout")


if __name__ == '__main__':
    websize3 = 'http://115.24.170.106:8081/default.aspx'
    # while 1:
    #     try:
    #         splinter(websize3)
    #     except Exception, e:
    #         try:
    #             alert = browser.get_alert()
    #             alert.accept()
    #         except Exception:
    #             pass
    #         print ("main : " + e.__str__())
    splinter(websize3)