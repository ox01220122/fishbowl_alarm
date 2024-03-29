from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

def crawling_img(name):
    
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options) # 드라이버랑 실행되는 해당 파이썬 파일이 같은 경로에 있으면 생략가능

    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
    elem = driver.find_element("name", "q")
    elem.send_keys(name)
    elem.send_keys(Keys.RETURN)

    #
    SCROLL_PAUSE_TIME = 1
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")  # 브라우저의 높이를 자바스크립트로 찾음
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 브라우저 끝까지 스크롤을 내림
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element("css selector",".mye4qd").click()
            except:
                break
        last_height = new_height

    imgs = driver.find_elements("css selector",".rg_i.Q4LuWd")

    count = 1
    for img in imgs:
        try:
            img.click()
            time.sleep(2)
            imgUrl = driver.find_element("xpath",
                '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img').get_attribute("src")
            
            path = "C:\\Users\\UserK\\Desktop\\test\\" # 저장할 경로
            urllib.request.urlretrieve(imgUrl, path + name + str(count) + ".jpg")
            count = count + 1
            if count >= 260:
                break
        except:
            pass
    driver.close()
fishs = ["금붕어 사진"]

for fish in fishs:
    crawling_img(fish)
