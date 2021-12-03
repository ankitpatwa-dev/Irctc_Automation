import requests
from bs4 import BeautifulSoup
from lxml import etree

url = "https://messages.google.com/web/conversations/73"

# data = requests.get(url)
# htmlContent = data.content
# print(htmlData)

# soup = BeautifulSoup(htmlContent, 'html.parser')
# dom = etree.HTML(str(soup))
# print(dom.xpath('/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-main-nav/mws-conversations-list/nav/div[1]/mws-conversation-list-item[1]/')[0].text)





# rough work
# /html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-main-nav/mws-conversations-list/nav/div[1]/mws-conversation-list-item[1]/
# /html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-conversation-container/div/div[1]/div/mws-messages-list/mws-bottom-anchored/div/div/div/mws-message-wrapper[3]/div/div/div