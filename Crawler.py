from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import pickle, json, base64

#   Chrome Options 
chrome_options = Options()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.cookies": 2})
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080") 

#   Driver Setup
driver = webdriver.Chrome(r"browsers/chromedriver.exe", options = chrome_options)
driver.set_page_load_timeout(30)



#class Ads(https):
#    def __init__(self,https):
#        self.https = https
#        pass
#TODO : Attempt a Cookies Class if the below 3 methods dont work... Hope they will :<



def send_devtools(driver, cmd, params={}):
  resource = "/session/%s/chromium/send_command_and_get_result" % driver.session_id
  url = driver.command_executor._url + resource
  body = json.dumps({'cmd': cmd, 'params': params})
  response = driver.command_executor._request('POST', url, body)
  #if response['status']:
    #raise Exception(response.get('value'))
  return response.get('value')

def save_cookies(driver, file_path):
  cookies = send_devtools(driver, "Network.getAllCookies", {})  
  with open(file_path, 'a') as file:
    json.dump(cookies, file, indent=2)

def load_cookies(driver, file_path):
  with open(file_path, 'r') as file :
    cookies = json.load(file)
    send_devtools(driver, "Network.setCookies", cookies)





#   Main crawling function
def crawl(https, search):
    global new_https
    driver.get(f"{https}")
    #cookies = pickle.load(open("cookies.pkl", "rb"))
    #for cookie in cookies:
    #    driver.add_cookie(cookie)
    load_cookies(driver, r"Cookies.json")
    sleep(10)


    if https.startswith('https://www.adevarul.ro'):
        # Merge cu cookies.json si e simplu si fara.
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/input').send_keys(f'{search}')
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/button').click()
        sleep(2.5)
        driver.find_element_by_xpath('//*[@id="tab-mrarticle"]/div/ul/li[1]/article/div/h2/a').click()
        

    elif https.startswith('https://www.protv.ro'):
        # Nu merge cu cookies.json dar e simplu fara.
        driver.find_element_by_xpath('/html/body/section[1]/div[2]/nav/div[7]/button').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="searchInputMobile"]').send_keys(f'{search}')
        sleep(2.5)
        driver.find_element_by_xpath('/html/body/section[1]/div[2]/nav/div[3]').click()
        
        
        
    elif https.startswith('https://www.zf.ro'):
        # Merge cu cookies.json 
        #TODO : FIX THIS SHIT.
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/button[2]').click()
        driver.find_element_by_xpath('//*[@id="onesignal-popover-cancel-button"]').click()
        driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[1]/form/div/input[1]').send_keys(f'{search}')
        driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[1]/form/div/button').click()
        sleep(3)
        driver.find_element_by_xpath('//*[@id="contentTop"]/div/div[2]/div/a/img').click()
        #save_cookies(driver, r"Cookies.json");
    
    elif https.startswith('https://www.mediafax.ro'):
        # Nu merge cu cookies.json.
        #driver.find_element_by_class_name("btn btn-success").click()
        #driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/button[2]').click()
        #sleep(3)
        driver.find_element_by_xpath('//*[@id="searchQuery"]').send_keys(f'{search}')
        driver.find_element_by_xpath('//*[@id="searchform"]/fieldset/input[2]').click()
        sleep(3)
        driver.find_element_by_xpath('//*[@id="content"]/div[2]/ul/li[1]/a').click()
        save_cookies(driver, r"Cookies.json")

    driver.get_screenshot_as_file("capture1.png")
    new_https = driver.current_url
    return new_https

    #TODO: MAKE IT WORK !!
      



if __name__ == "__main__":
    crawl('https://www.zf.ro','marius florea')   # TESTING FOR ERRORS