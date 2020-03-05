# This .py file contains all
# the functions that will be used
# for the Web Scraping.


from bs4 import BeautifulSoup
import urllib3
import requests


#   Function to convert list output to string.
def listToString(list):  
    
    # initialize an empty string 
    str1 = ""
    
    # traverse in the string   
    for element in list:
        str1 += str(element) 
    
    # return string   
    return str1


def scraper(new_https):
    #   URL REQUEST
    url = requests.get(f'{new_https}', timeout=30)
    rezultat = ''

    #   Fetch the website data
    soup = BeautifulSoup(url.content, features = "html.parser", from_encoding = "UTF-8")
    soup.prettify()
    #   Scrape the website data
    #cautare = soup.find("article").text.replace("\t", "").replace("\r", "").replace("\n", "")
    check = soup.find('a')['href']
    #check = ''
    if check.count('adevarul.ro/') >= 1:
        title = soup.find('h2', {'class':'articleOpening'}).text.replace('\t','\n\t')
        content = soup.find('div', {'id':'article-body'}).text.replace('\t','\n\t')
        rezultat = listToString(title) + listToString(content)
    if check.count('evz.ro/') >= 1: # TODO.
        title = soup.find('h2', {'class':'articleOpening'}).text.replace('\t','\n\t')
        content = soup.find('div', {'class':'post-content'}).text.replace('\t','\n\t')
        rezultat = listToString(title) + listToString(content)

    print(rezultat)
    #print(soup.prettify())
    return rezultat

if __name__ == "__main__":
    new_https = scraper('https://adevarul.ro/economie/stiri-economice/gigi-becali-suparat-bancile-nu-vor-sa-i-mai-tina-milioanele-euro-cont-1_5e4d089b5163ec42713b75a0/index.html') 
    # TESTING FOR ERRORS
    #print(soup)