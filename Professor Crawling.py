# Author : Lee Sang hwa, Kang Ho Dong, Kim Yeong Hwa
# Date : 2020 - 08 - 04
# Title : Get Professor Information using Selenium, BeaultifulSoup
# Language : Python 3


import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

start = time.time()  # 시작 시간 저장
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
# 혹은 options.add_argument("—disable-gpu")

path = "./chromedriver"
driver = webdriver.Chrome(path, chrome_options=options)
# driver = webdriver.Chrome(path)

# 권오준 권순각 김성우 이종민 이중화 임영호 박유현 장희숙
pro_list = ['11100', '11258', '11504', '11505', '11506', '65953', '12923', '63819']
html_list = ['ojkwon.html','skkwon.html','libero.html','jongmin.html','junghwa.html','yhleem.html','yhpark.html','jang1052.html']

for i in range(len(pro_list)):
    print(pro_list[i],html_list[i])
    # 웹 접속
    driver.get("https://www.deu.ac.kr/www/dept/member/55/2")
    # 일정 시간 대기
    wait = WebDriverWait(driver, 20)
    try:
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add' + pro_list[i] + '"]')))
        driver.find_element_by_xpath('//*[@id="add' + pro_list[i] + '"]').send_keys(Keys.ENTER)
        time.sleep(5)
        # 일정 시간 대기
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        professor_container = soup.select('#iLayoutSubContent_deptmember_uppnl > div')
        print(str(*professor_container))

        f = open(html_list[i],'w',encoding='utf-8')
        f.write(str(*professor_container))
        f.close()
    except:
        print("페이지 로드 안됨")

# 크롬 드라이버 종료
driver.quit()
print("소요시간 :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
