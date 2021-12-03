
try:
     from selenium import webdriver
     from selenium.webdriver.support.ui import Select
     from selenium.webdriver.common.keys import Keys
     import json
     import os
     import pydub
     import sys
     import time
     # import urllib.request as ur
     from urllib.request import Request , urlretrieve
     import pyautogui
except Exception as e:
     print(f"Something is Wrong with {e}")

try :
     json_file = open('system.json')
     content = json.load(json_file)['content']
except Exception as e:
     print(f'Something wrong with importing content file {2}')     


window = webdriver.Chrome("chromedriver.exe")
window.maximize_window()  
window.get(content['Url'])

while True: 
     ok_btn = window.find_element_by_xpath("/html/body/app-root/app-home/div[1]/app-header/p-dialog[2]/div/div/div[2]/div/form/div[2]/button")
     if (ok_btn):
          ok_btn.click()
          break


# ------------------------------------------------Login
Login_btn = "/html/body/app-root/app-home/div[1]/app-header/div[2]/div[2]/div[1]/a[1]"
username_path = "//*[@id=\"userId\"]" 
password_path = "//*[@id=\"pwd\"]"


window.find_element_by_xpath(Login_btn).click()
window.find_element_by_xpath(username_path).send_keys(content['username'])
window.find_element_by_xpath(password_path).send_keys(content['passwd'])


# time.sleep(2)

# captcha_input = "//*[@id=\"nlpAnswer\"]"
# window.find_element_by_xpath(captcha_input).send_keys('')

captcha_key_time = 15
time.sleep(captcha_key_time)


Login_btn = "//*[@id=\"login_header_disable\"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/span/button"
window.find_element_by_xpath(Login_btn).click()

# "//*[@id=\"login_header_disable\"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/span/button"


# break the captcha code throug audio to text


# # voice_btn_xpath = "//*[@id=\"nlpvoicerefresh\"]/div"
# # window.find_element_by_xpath(voice_btn_xpath).click()
# # window.execute_script("javascript:nlpAjaxCaptcha('voice');")
# window.execute_script("javascript:nlpAjaxCaptcha('voice');")
# time.sleep(1)

# # audio_id = 'play_captcha'
# audio_xpath = "//*[@id=\"play_captcha\"]"
# audio_source_xpath = "//*[@id=\"play_captcha\"]/source"
# src = window.find_element_by_xpath(audio_source_xpath).get_attribute('src')
# print(src)


# path_to_mp3 = os.path.normpath(os.path.join(os.getcwd(), "sample.mp3"))
# path_to_wav = os.path.normpath(os.path.join(os.getcwd(), "sample.wav"))

# # download the mp3 audio file from the source
# # ur.urlretrieve(src, path_to_mp3)
# req = Request(src)


#----------------------------------------------------------------------- Date Selection
date_input = window.find_element_by_xpath(content['date_input'])
content_date = content['date']
backslash = '\b'
date_input.send_keys(f"{backslash*10}{content_date}")
time.sleep(1)
date_input.send_keys(Keys.ENTER)
time.sleep(0.4)



# # -----------------------------------------------------------------------from input
window.find_element_by_xpath(content['from_input']).send_keys(content['from'])
first_input_opt = "//*[@id=\"pr_id_1_list\"]/li[1]"
time.sleep(0.5)
window.find_element_by_xpath(first_input_opt).click()

# time.sleep(1)

# # ------------------------------------------------------------------------to input 

window.find_element_by_xpath(content['To_input']).send_keys(content['To'])
time.sleep(0.5)
second_input_opt = "//*[@id=\"pr_id_2_list\"]/li[1]"
window.find_element_by_xpath(second_input_opt).click()


# # ----------------------------------------------------------------talkal selction
# dropdown = "//*[@id=\"journeyQuota\"]/div"
# window.find_element_by_xpath(dropdown).click()


# ladies = "//*[@id=\"journeyQuota\"]/div/div[4]/div/ul/p-dropdownitem[2]/li"
# Senior_citizen = "//*[@id=\"journeyQuota\"]/div/div[4]/div/ul/p-dropdownitem[3]/li"
# Divyang = "//*[@id=\"journeyQuota\"]/div/div[4]/div/ul/p-dropdownitem[4]/li"
# tatkal = "//*[@id=\"journeyQuota\"]/div/div[4]/div/ul/p-dropdownitem[5]/li"
# tatkal = "//*[@id=\"journeyQuota\"]/div/div[4]/div/ul/p-dropdownitem[5]/li"
# premium_tatkal = "//*[@id=\"journeyQuota\"]/div/div[4]/div/ul/p-dropdownitem[6]/li"


# window.find_element_by_xpath(tatkal).click()
time.sleep(2)





# # Search button
search_btn = "//*[@id=\"divMain\"]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[5]/div/button"
window.find_element_by_xpath(search_btn).click()


time.sleep(50)
window.close()



# # ----------------------------------------------Seat Book
# seat = "//*[@id=\"divMain\"]/div/app-train-list/div[4]/div/div[5]/div[2]/div[1]/app-train-avl-enq/div[1]/div[5]/div/table/tr/td[1]/div"
# while True:
#      print("not")
#      if(seat):
#           print("find")
#           window.find_element_by_xpath(seat).click()
#           break

# time.sleep(0.4)
# book = "//*[@id=\"divMain\"]/div/app-train-list/div[4]/div/div[5]/div[2]/div[1]/app-train-avl-enq/div[2]/div/span/span/button[1]"
# window.find_element_by_xpath/(book).click()









# # window.close() 



