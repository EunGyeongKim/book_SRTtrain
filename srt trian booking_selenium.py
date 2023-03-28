# -*- coding: utf-8 -*-
# https://kminito.tistory.com/79
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("chromedriver")
driver.get('https://etk.srail.co.kr/cmc/01/selectLoginForm.do') # 로그인 화면으로 이동
driver.implicitly_wait(15) # 페이지 다 뜰 때 까지 기다림

driver.find_element(By.ID, 'srchDvNm01').send_keys('12345677234') # 회원번호
driver.find_element(By.ID, 'hmpgPwdCphd01').send_keys("1111111111") # 비밀번호

driver.find_element(By.XPATH, '//*[@id="login-form"]/fieldset/div[1]/div[1]/div[2]/div/div[2]/input').click()
driver.implicitly_wait(5)

# 기차 조회 페이지로 이동
driver.get('https://etk.srail.kr/hpg/hra/01/selectScheduleList.do')
driver.implicitly_wait(5)

# 출발지 입력
dep_stn = driver.find_element(By.ID, 'dptRsStnCdNm')
dep_stn.clear() 
dep_stn.send_keys("동탄")

# 도착지 입력
arr_stn = driver.find_element(By.ID, 'arvRsStnCdNm')
arr_stn.clear()
arr_stn.send_keys("수서")


# 날짜 드롭다운 리스트 보이게
elm_dptDt = driver.find_element(By.ID, "dptDt")
driver.execute_script("arguments[0].setAttribute('style','display: True;')", elm_dptDt)

from selenium.webdriver.support.select import Select

# 2021년 10월 01일 기차 선택
Select(driver.find_element(By.ID,"dptDt")).select_by_value("20211001")


# 출발 시간
elm_dptTm = driver.find_element(By.ID, "dptTm")
driver.execute_script("arguments[0].setAttribute('style','display: True;')", elm_dptTm)
Select(driver.find_element(By.ID, "dptTm")).select_by_visible_text("12")


driver.find_element(By.XPATH,"//input[@value='조회하기']").click()