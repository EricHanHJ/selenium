from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import urllib.request
import time

print("인스타그램 나를 팔로우하고 있는 사람들의 게시물의 사진을 다운받는 프로그램입니다.")
print("해당 CMD창은 닫으시면 크롤링이 중단되며 현황 확인용으로 켜놓으시면 됩니다.")
print("자동실행되는 크롬 브라우저는 윈도우창 [최소화] 시켜도 상관없습니다.\n")
id = input("Instagram ID : ")
pw = input("Instagram Password : ")

print("> 드라이버 실행중...")
print("\n> USB Checking....\n")
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)
elem = driver.find_element_by_name("username")
elem.send_keys(id)
elem = driver.find_element_by_name("password")
elem.send_keys(pw)
time.sleep(1)
elem.submit()
print("> 로그인중..")

time.sleep(5)
driver.get("https://www.instagram.com/" + id + "/")
time.sleep(5)
print("> 팔로워 인원 체크중...")
driver.find_element_by_partial_link_text("팔로워").click()
time.sleep(5)

followers = driver.find_elements_by_css_selector(".FPmhX.notranslate._0imsa") # 팔로워 대상
print("> 총 팔로워 : " + str(len(followers)) + " 명")
f_cnt = 0
for follower in followers:
    print(">>> " + str(f_cnt + 1) + "/" + str(len(followers)) + " 진행중..")
    driver.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")[f_cnt].click()

    time.sleep(5)

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(3)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


    imgElems = driver.find_elements_by_css_selector(".v1Nh3.kIKUG._bz0w > a > div > .KL4Bh > img") # 이미지 element들 저장
    
    time.sleep(2) # 이미지 로딩(5초)
    i_cnt = 1
    for imgElem in imgElems:
        time.sleep(1) # 이미지 로딩(5초)
        imgUrl = imgElem.get_attribute("src")  # 이미지 태그로 url 조회
        urllib.request.urlretrieve(imgUrl, str(f_cnt + 1) + "_" + str(i_cnt) + ".jpg") # 파일다운
        print(">>> FileName : " + str(f_cnt + 1) + "_" + str(i_cnt) + ".jpg [저장]")
        i_cnt = i_cnt + 1
    
    driver.get("https://www.instagram.com/" + id + "/")

    time.sleep(5)

    driver.find_element_by_partial_link_text("팔로워").click()

    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(2)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    f_cnt = f_cnt + 1
print("\n>>> 크롤링 완료")
time.sleep(1)
print("종료 5초전")
time.sleep(1)
print("종료 4초전")
time.sleep(1)
print("종료 3초전")
time.sleep(1)
print("종료 2초전")
time.sleep(1)
print("종료 1초전")
time.sleep(1)
print("프로그램이 종료 됩니다.")
time.sleep(1)
driver.close()
