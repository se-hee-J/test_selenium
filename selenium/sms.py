from selenium import webdriver
import time

#시스템에 부착된 장치가 작동하지 않습니다. (0x1F) 에러 나올때
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)
#창 최대화
driver.maximize_window()

#SMS 발송 페이지 접속
driver.get("https://console.toast.com/project/ItOF3kKJ/notification/sms#deliver-sms")

#아이디/비밀번호 입력
driver.find_element_by_name('id').send_keys('본인정보입력')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('본인정보입력')

#로그인 버튼 클릭 ---해당 부분까지 실행됨**
driver.find_element_by_css_selector('#login > div.content.login_content > div > form > fieldset > div.btn_area > button').click()

#SMS발송 페이지는 iframe으로 되어있는 것 확인
#ㄴ현재 페이지에서 iframe이 몇개 있는지 변수에 넣고 확인해보기
iframes = driver.find_elements_by_tag_name('iframe')
print('현재 페이지에 iframe은 %d개가 있습니다.' % len(iframes))

#iframe 변수를 하나씩 확인해보기
for i, iframe in enumerate(iframes): #배열 순번 확인
    try:
        print('%d번째 iframe 입니다.'%i)

        driver.switch_to_frame(iframes[i]) #i번째 iframe으로 변경
        print(driver.page_source)

        driver.switch_to_default_content() #원래 frame로 돌아오기
    except:
        driver.switch_to_default_content()
        print('pass by except : iframes[%d]'%i)
        pass

driver.switch_to_frame(iframes[1]) #iframe으로 전환

#전환 후 MMS 라디오 버튼 xpath에 접근
elem = driver.find_element_by_xpath('//*[@id="orgProjectList"]/div[4]/div/div/li/div/a')

#MMS 라디오 버튼이 선택 안되어 있으면 선택하기
if elem.is_selected() == False:
    print("선택함")
    elem.click()

else:
   print("선택되어있음")

#발신 번호 선택하기
driver.find_element_by_class_name('select2-results__option select2-results__option--highlighted').click()

#내용 작성
text = driver.find_element_by_class_name('body')
text.send_keys('안녕하세요.메시지 테스트입니다.')

#보내기 버튼 클릭
driver.find_element_by_id('sendBtn').click()

#iframe에서 원래 frame으로 돌아옴
driver.switch_to_default_content()


