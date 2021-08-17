from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import urllib.request
import time
import os
from twilio.rest import Client

def sendMsg(info):
    account_sid = "AC65097362c9153bacdcc26bb248f6f34b"
    auth_token = "41cad08970ac44e7adb5399083f9ec9f"
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body=info,
                        from_='+13479336923',
                        to='+821027751331'
                    )

id = "1792870631"
pw = "pwpwpwpw"

#id = input("SRT ID : ")
#pw = input("SRT Password : ")

driver = webdriver.Chrome()
driver.get("https://etk.srail.kr/cmc/01/selectLoginForm.do?pageId=TK0701000000")

elem = driver.find_element_by_name("srchDvNm")
elem.send_keys(id)
elem = driver.find_element_by_name("hmpgPwdCphd")
elem.send_keys(pw)
time.sleep(1)
elem.submit()

print("> 로그인중..")

time.sleep(2)

driver.find_element_by_partial_link_text("간편조회하기").click()

time.sleep(2)


elem = driver.find_element_by_name('dptRsStnCd')
driver.execute_script('''
    var elem = arguments[0];
    var value = arguments[1];
    elem.value = value;
''', elem, '0551')

elem = driver.find_element_by_name('arvRsStnCd')
driver.execute_script('''
    var elem = arguments[0];
    var value = arguments[1];
    elem.value = value;
''', elem, '0507')

time.sleep(2)

driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_UP)
driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_UP)

time.sleep(2)

driver.find_element_by_css_selector("#search-form > fieldset > div.box1 > div > div > div.mgl10.val_m.dpib > div.wx150.dpib.dropdown_type1").click()
driver.find_element_by_partial_link_text("2021/02/11(목)").click()

driver.find_element_by_css_selector("#search-form > fieldset > div.box1 > div > div > div.mgl10.val_m.dpib > div.wx60.dpib.dropdown_type1 > a").click()
driver.find_element_by_partial_link_text("00").click()

driver.find_element_by_css_selector("#search-form > fieldset > div.box1 > div > ul > li:nth-child(2) > div.pic_mid_r > div:nth-child(1) > a").click()
driver.find_element_by_partial_link_text("어른(만 13세 이상) 2명").click()

elem.submit()

time.sleep(2)

while True:
    for i in range(1,9):
        seat1 = driver.find_element_by_css_selector("#result-form > fieldset > div.tbl_wrap.th_thead > table > tbody > tr:nth-child(" + str(i) + ") > td:nth-child(6) > a > span").text
        if seat1 == '예약하기':
            driver.find_element_by_css_selector("#result-form > fieldset > div.tbl_wrap.th_thead > table > tbody > tr:nth-child(" + str(i) + ") > td:nth-child(6) > a > span").click()
            time.sleep(1)
            driver.find_element_by_css_selector("body > div.ui-dialog.ui-corner-all.ui-widget.ui-widget-content.ui-front.ui-dialog-buttons.ui-draggable.ui-resizable > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button").click()
            sendMsg("특실 예약 신청")
            time.sleep(600)
            driver.close()
            break
        
        seat2 = driver.find_element_by_css_selector("#result-form > fieldset > div.tbl_wrap.th_thead > table > tbody > tr:nth-child(" + str(i) + ") > td:nth-child(7) > a > span").text
        if seat2 == '예약하기':
            driver.find_element_by_css_selector("#result-form > fieldset > div.tbl_wrap.th_thead > table > tbody > tr:nth-child(" + str(i) + ") > td:nth-child(7) > a > span").click()
            time.sleep(1)
            driver.find_element_by_css_selector("body > div.ui-dialog.ui-corner-all.ui-widget.ui-widget-content.ui-front.ui-dialog-buttons.ui-draggable.ui-resizable > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button").click()
            sendMsg("일반식 예약 신청")
            time.sleep(600)
            driver.close()
            break
            
        seatReady = driver.find_element_by_css_selector("#result-form > fieldset > div.tbl_wrap.th_thead > table > tbody > tr:nth-child(" + str(i) + ") > td:nth-child(8) > a > span").text
        if seatReady == '신청하기':
            driver.find_element_by_css_selector("#result-form > fieldset > div.tbl_wrap.th_thead > table > tbody > tr:nth-child(" + str(i) + ") > td:nth-child(8) > a > span").click()
            sendMsg("예약대기 신청")
            time.sleep(600)
            driver.close()
            break

    time.sleep(10)

    driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_UP)
    driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_UP)

    time.sleep(10)

    driver.find_element_by_css_selector("#search_top_tag > input").click()

    time.sleep(3)


