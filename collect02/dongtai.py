# print("坚持就是胜利！")
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
import time
from selenium.webdriver.chrome.options import Options

#无头浏览器
# opt=Options()
# opt.add_argument('--headless')
# opt.add_argument('--disable-gpu')
#
# web=Chrome(options=opt)
web=Chrome()
web.get("http://www.lagou.com")

el=web.find_element(by=By.XPATH,value='//*[@id="changeCityBox"]/p[1]/a')
el.click()
time.sleep(1)

web.find_element(by=By.XPATH,value='//*[@id="search_input"]').send_keys('python',Keys.ENTER)
time.sleep(1)

# div_list=web.find_elements(by=By.XPATH,value='//div[@id="jobList"]/div[1]/div')
# for i in div_list:
#     job_name=i.find_element(by=By.XPATH,value='./div[1]/div[1]/div[1]/a').text
#     job_price=i.find_element(by=By.XPATH,value='./div[1]/div[1]/div[2]/span').text
#     job_condition=i.find_element(by=By.XPATH,value='./div[1]/div[1]/div[2]').text
#     print(job_name,job_price,job_condition)
