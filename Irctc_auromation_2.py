try:
     import selenium
     from selenium import webdriver
     import time
     import json
except Exception as e:
     print(f"Something is Wrong with {e}")

json_data = open('system.json')
content = json.load(json_data)["Content_2"]

window = webdriver.Chrome("chromedriver.exe")
window.maximize_window()       
window.get(content['Url'])


ps_name_xpath = "//*[@id=\"ui-panel-31-content\"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[1]/p-autocomplete/span/input"

# "//*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[1]/p-autocomplete/span/input"
# //*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[2]/input 
# //*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[1]/p-autocomplete/span/input
# //*[@id="ui-panel-12-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[1]/p-autocomplete/span/input
# //*[@id="ui-panel-31-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[1]/p-autocomplete/span/input
# //*[@id="ui-panel-50-content"]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[1]/p-autocomplete/span/input
# //*[@id="divMain"]/div/app-train-list/div[4]/div/div[5]/div[2]/div[1]/app-train-avl-enq/div[1]/div[5]/div/table/tr/td[1]/div

