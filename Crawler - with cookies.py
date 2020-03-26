from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import pickle, json, base64

#   Chrome Options 
chrome_options = Options()
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080") 

#   Driver Setup
driver = webdriver.Chrome(r"browsers/chromedriver.exe", options = chrome_options)
driver.set_page_load_timeout(30)


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
  with open(file_path, 'w') as file:
    json.dump(cookies, file, indent=2)

def load_cookies(driver, file_path):
  with open(file_path, 'r') as file :
    cookies = json.load(file)
    send_devtools(driver, "Network.setCookies", cookies)





#   Main crawling function
def crawl(https, search):
    global new_https
    driver.get(f"{https}")
    sleep(10)


    if https.startswith('https://www.libertatea.ro'):
        try:
            load_cookies(driver,r"Libertatea.json")
            driver.find_element_by_css_selector(".qc-cmp-button").click()
            driver.find_element_by_css_selector("#search-box").send_keys(f'{search}')
            driver.find_element_by_xpath("//button[@type='submit']").click()
            sleep(5)
            driver.find_element_by_xpath("//h2").click()
        except Exception as e:
            with open("Logs.txt","w") as f:
                f.write(str(e))
        finally:
            save_cookies(driver,r"Libertatea.json")

    elif https.startswith('https://www.zf.ro'):
        try: # TODO : FIX THIS SHIT FRAME 23.
            #load_cookies(driver,r"Financiar.json")
            #driver.switch_to.frame(23)
            #driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/button").click()
            sleep(2)
            driver.find_element_by_xpath("//input[@name='q']").send_keys(f'{search}')
            driver.find_element_by_xpath("//div[@id='sidebarTop']/div/form/div/button").click()
            sleep(3)
            driver.find_element_by_css_selector("img:nth-child(2)").click()
            sleep(3)
            driver.get_screenshot_as_file("capture5.png")
        except Exception as e:
            with open("Logs.txt","w") as f:
                f.write(str(e))
        finally:
            save_cookies(driver,r"Financiar.json")
        
    elif https.startswith('https://www.digi24.ro'):
        try:
            #load_cookies(driver,r"Digi24.json")
            driver.find_element_by_css_selector(".gdpr-button:nth-child(3)").click()
            sleep(2)
            driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
            driver.find_element_by_xpath("//input[@id='search-input']").send_keys(f'{search}')
            driver.find_element_by_xpath("//input[@id='search-input']").send_keys(Keys.ENTER)
            sleep(3)
            driver.find_element_by_xpath("/html/body/main/section/div[2]/div/div/article[1]/div/h4/a").click()
        except Exception as e:
            with open("Logs.txt","w") as f:
                f.write(str(e))
        finally:
            save_cookies(driver,r"Digi24.json")
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
    crawl('https://www.libertatea.ro/','moneda')   # TESTING FOR ERRORS