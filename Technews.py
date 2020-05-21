import requests
from bs4 import BeautifulSoup

#url of the tech site
url = 'https://gadgets.ndtv.com/news'

#accessing the site with get function and reading with content function
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#seperating the headlines
cl = soup.findAll(class_='news_listing')

#creating list to store all the different news with some decoration to look good with \n and a globe emoji
List = []
for i in cl:
	List.append("\n\n🌐")
	List.append(i.text)

#inserting heading for top
List.insert(0,'☆☆☆☆☆💥 Tech News 💥☆☆☆☆☆')

#converting list to string
text = " ".join(List)
print(text)
