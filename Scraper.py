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


def scrape(new_https):

    #   URL REQUEST
    url = requests.get(f'{new_https}', timeout=30)
    rezultat = ''
    interest = []

    #   Fetch the website data
    soup = BeautifulSoup(url.content, features = "html.parser", from_encoding = "UTF-8")
    soup.prettify()

    #   Scrape the website data
    if new_https.startswith('https://www.libertatea.ro'):
        title = soup.find('h1').text.replace('\t','\n\t')
        content = soup.find_all('p')
        for paragraph in content:
            format = paragraph.text.replace('\n','\n\t\n')
            interest.append(format)
            interest.append("\n\t")
        rezultat = listToString(title) + listToString(interest[:-2])
        interest.clear()

    elif new_https.startswith('https://www.digi24.ro'):
        title = soup.find('h1').text
        content = soup.find_all('p')
        for paragraph in content:
            format = paragraph.text
            interest.append("\n\n")
            interest.append(format)
        rezultat = listToString(title) + listToString(interest[:-1])
        interest.clear()

    elif new_https.startswith('https://www.realitatea.net'):
        title = soup.find('h2', {'class':'my-2'}).text
        content = soup.find_all('p')
        for paragraph in content:
            format = paragraph.text
            interest.append("\n\n")
            interest.append(format)
        rezultat = listToString(title) + listToString(interest[2:-14])
        interest.clear()

    elif new_https.startswith('https://adevarul.ro'):
        title = soup.find('h1').text.replace('\n',' ')
        header = soup.find('h2', {'class':'articleOpening'}).text.replace('\n',' ')
        content = soup.find('div', {'id':'article-body'}).text.replace('\t','\n\t')
        rezultat = listToString(title) + '\n\n\n' + listToString(header) + listToString(content)

    elif new_https.startswith('https://jurnalulnational.ro'):
        title = soup.find('h1', {'class':'single-post-title'}).text.replace('\t','\n\t')
        content = soup.find_all('p')
        for paragraph in content:
            format = paragraph.text
            interest.append("\n\n")
            interest.append(format)
        rezultat = listToString(title) + listToString(interest[2:-91])
        interest.clear()
        
    elif new_https.startswith('https://www.zf.ro'):
        title = soup.find('h1', {'class':'articleTitle h1'}).text.replace('\n','\n\t')
        content = soup.find_all('p')
        for paragraph in content:
            format = paragraph.text
            interest.append("\n\n")
            interest.append(format)
        rezultat = listToString(title) + listToString(interest[2:-23])
        interest.clear()
        
    elif new_https.startswith('https://evz.ro'):
        title = soup.find('h1', {'class':'post-title'}).text.replace('\n','\n\t')
        content = soup.find_all('p')
        for paragraph in content:
            format = paragraph.text
            interest.append("\n\n")
            interest.append(format)
        rezultat = listToString(title) + listToString(interest[2:-23])
        interest.clear()
        
    elif new_https.startswith('https://www.mediafax.ro'):
        title = soup.find('h1').text.replace('\n','\n\t')
        content = soup.find_all('p')
        for paragraph in content:
            format = paragraph.text
            interest.append("\n\n")
            interest.append(format)
        rezultat = listToString(title) + listToString(interest[:-30])
        interest.clear()

    print(rezultat)
    return rezultat

if __name__ == "__main__":
    new_https = scrape('https://www.mediafax.ro/economic/bnr-tine-cursul-stabil-moneda-europeana-ramane-in-preajma-maximului-istoric-19003665') 