import pandas as pd
from bs4 import BeautifulSoup
import requests
import os

df = pd.read_csv('/Users/chawadesharvari17gmail.com/Desktop/webscrapping/web_scrapping_project/input.csv')

i = 37

for url in (df['URL']):

  #declares path
  path = '/Users/chawadesharvari17gmail.com/Desktop/webscrapping/web_scrapping_project/output'

  #requests html text, user agent is so that we dont get error 406
  html_text = requests.get(url,headers={"User-Agent": "XY"}).text
  soup = BeautifulSoup(html_text,'lxml')

  #extracting article title
  article_title = soup.find('h1',class_ = 'entry-title')
  
  if(article_title == None):
    
    #if there is no content then it wont proceed to the further part
    i+=1
    continue

  else:
    
    #if there is content in the web page the it will extract the content
    article_texts = soup.find_all('p')
    content = ''
    for article_text in article_texts:
      content = content + article_text.text +'\n'
    temp = f'id{i}.txt'
    path = os.path.join(path,temp)
    
    #create a new text file and write the content in it
    f = open(path, "w")
    f.write(f'{article_title.text}\n{content}')
    f.close()
    i+=1
