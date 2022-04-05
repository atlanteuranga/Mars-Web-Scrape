


from bs4 import BeautifulSoup as bs
import splinter
from splinter import Browser
import requests
from pprint import pprint
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape():
    mars_dict = {}

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)



    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    titles = soup.find('div', class_ = 'list_text')
    news_title = titles.a.text
    news_body = soup.find('div', class_ = 'article_teaser_body').text
    mars_dict.update({"news_title":news_title, "news_body":news_body})



    url = "https://spaceimages-mars.com/"
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    img = soup.find('img', class_ = 'headerimage fade-in')
    img_url = url + img['src']
    mars_dict.update({"img_url":img_url})




    url = "https://galaxyfacts-mars.com/"
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    table_headers = soup.find_all('th')
    table_data = soup.find_all('span', class_='orange')
    table_data
    headers = []
    datas = []
    for i in range(6):
        headers.append(table_headers[i+1].text)
        datas.append(table_data[i+3].text)
    print(headers)
    print(datas)




    dict = {"Description": headers, "Values": datas}
    mars_df = pd.DataFrame(dict)
    mars_df.to_html('mars_df.html', index = False)




    url_ = "https://marshemispheres.com/"
    browser.visit(url_)

    hemispheres = ['Cerberus', 'Schiaparelli', 'Syrtis', "Valles"]
    hemi_dict = {}
    hemi_list = []
    for hemi in hemispheres:
        
        browser.links.find_by_partial_text(hemi).click()
        html = browser.html
        soup = bs(html, 'html.parser')
        img_url = url_ + soup.find('img', class_='wide-image')['src']

        
        title = soup.find('h2', class_='title')
        hemi_dict = {title.text:img_url}
        hemi_list.append(hemi_dict)
        hemi_dict = {}
        browser.visit(url_)
    mars_dict.update({"hemi_list":hemi_list})
    
    browser.quit()
    return mars_dict







