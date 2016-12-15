# -*- coding:utf-8 -*-
import os
from selenium import webdriver
from splinter import Browser
import time

chromedriver_loc = '/home/yanzijie/bin/chromedriver'
driver = webdriver.Chrome(executable_path=chromedriver_loc)
browser = Browser('chrome')


def splinter(url):
    while (1):

        # login 126 email websize
        try:
            browser.visit(url)
        except Exception, e:
            print('1' + e.__str__())
            # browser.reload()
            continue
        # wait web element loading
        time.sleep(2)
        try:
            browser.find_by_css('.btns')[0].find_by_css('.nextDate')[0].click()
        except Exception, e:
            print('2' + e.__str__())
            # browser.reload()
            continue

        time.sleep(4)
        try:
            print(browser.find_by_id('UserID')[0].fill('131827'))
            print(browser.find_by_id('Password')[0].fill('131827'))
            print(browser.find_by_text(u'确定')[0].click())
            time.sleep(3)
        except Exception, e:
            print('已跳过登录')
            # browser.reload()
        #
        # try:
        #     print(browser.find_by_id('Password')[0].fill('142317'))
        # except Exception,e:
        #     print('4'+e.__str__())
        #     #browser.reload()

        # try:
        #     print(browser.find_by_text(u'确定')[0].click())
        # except Exception,e:
        #     print('4'+e.str)
        #     #browser.reload()


        # print(browser.find_by_id('UserID')[0].fill('142317'))
        # print(browser.find_by_id('Password')[0].fill('142317'))
        # print(browser.find_by_text(u'确定')[0].click())
        # time.sleep(2)
        try:
            print(browser.find_by_id('detailsInfo').find_by_tag('a')[0].click())
        except Exception, e:
            print('4' + e.__str__())
            time.sleep(2)
            # print(browser.find_by_id('detailsInfo').find_by_tag('a')[0].click())
            # browser.reload()
            continue
        time.sleep(3)
        # while browser.get_alert() ==None:
        #     time.sleep(0.5)
        try:
            alert = browser.get_alert()
            print (type(alert.text().encode('utf-8')))
            alert.accept()
        except Exception, e:
            print('5' + e.__str__())
            time.sleep(2)
            try:
                alert = browser.get_alert()
                print (type(alert.text().encode('utf-8')))
                alert.accept()
            except Exception:
                try:
                    browser.reload()
                except Exception,e:
                    alert = browser.get_alert()
                    #print (type(alert.text().encode('utf-8')))
                    alert.accept()
        # if browser.get_alert()!=None:
        #     with browser.get_alert() as alert:
        #         alert.accept()
        # try:
        #     browser.reload()
        # except:
        #     time.sleep(2)
            # browser.reload()
            # close the window of brower
            # browser.quit()


if __name__ == '__main__':
    websize3 = 'http://115.24.170.106:8081/default.aspx'
    splinter(websize3)
