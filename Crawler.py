from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

#   Chrome Options 
chrome_options = Options()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080") 

#   Driver Setup
driver = webdriver.Chrome(r"browsers/chromedriver.exe", options = chrome_options)
driver.set_page_load_timeout(30)


#   Main crawling function
def crawl(https, search):
    driver.get(f"{https}")
    sleep(10)

    if https.startswith('https://www.libertatea.ro'):
        try: # WORKS 20.03.2020
            driver.find_element_by_css_selector(".qc-cmp-button").click()
            driver.find_element_by_css_selector("#search-box").send_keys(f'{search}')
            driver.find_element_by_xpath("//button[@type='submit']").click()
            sleep(5)
            driver.find_element_by_xpath("//h2").click()
        except Exception as e:
            with open("Logs.txt","w") as f:
                f.write(str(e))

    elif https.startswith('https://www.digi24.ro'):
        try: # WORKS 20.03.2020
            driver.find_element_by_css_selector(".gdpr-button:nth-child(3)").click()
            sleep(5)
            driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
            driver.find_element_by_xpath("//input[@id='search-input']").send_keys(f'{search}')
            driver.find_element_by_xpath("//input[@id='search-input']").send_keys(Keys.ENTER)
            sleep(5)
            driver.find_element_by_xpath("/html/body/main/section/div[2]/div/div/article[1]/div/h4/a").click()
        except Exception as e:
            with open("Logs.txt","w") as f:
                f.write(str(e))

    elif https.startswith('https://www.realitatea.net'):
        try: # WORKS 21.03.2020
            driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div[1]/a").click()
            driver.find_element_by_id("top-search-box").send_keys(f'{search}')
            driver.find_element_by_xpath("//button[@id='search-top']/i").click()
            driver.find_element_by_css_selector(".article:nth-child(1) > .two > a").click()
        except Exception as e:
            with open("Logs.txt","w") as f:
                f.write(str(e))

    elif https.startswith('https://adevarul.ro/'):
        try: # WORKS 21.03.2020
            driver.find_element_by_css_selector(".accept-cookie-container").click()
            driver.find_element_by_css_selector(".accept-cookies-button").click()
            sleep(5)
            driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/input").send_keys(f'{search}')
            driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/button").click()
            sleep(5)
            driver.find_element_by_xpath("//div[@id='tab-mrarticle']/div/ul/li/article/div/h2/a").click()
        except Exception as e:
            with open("Logs.txt","w") as f:
                f.write(str(e))

    elif https.startswith('https://jurnalulnational.ro/'):
        try: # WORKS 21.03.2020
            driver.find_element_by_css_selector(".fa-search").click()
            driver.find_element_by_xpath("//input[@name='s']").send_keys(f'{search}')
            driver.find_element_by_xpath("//input[@name='s']").send_keys(Keys.ENTER)
            sleep(5)
            driver.find_element_by_xpath("//main[@id='content']/div/div/div/div[2]/article/div/h2/a").click()
        except Exception as e:
            with open("Logs.txt","w") as f:
                f.write(str(e))

    elif https.startswith('https://www.zf.ro'):
        try: # WORKS 21.03.2020
            driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[12]/iframe"))
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/button[2]").click()
            sleep(5)
            driver.switch_to.default_content()
            driver.find_element_by_css_selector(".form-control").send_keys(f'{search}')
            driver.find_element_by_xpath("//button[@type='button']").click()
            sleep(5)
            driver.find_element_by_css_selector("img:nth-child(2)").click()
        except Exception as e:
            with open("Logs.txt","w") as f:
                f.write(str(e))

    elif https.startswith('https://evz.ro'):
        try: # WORKS 21.03.2020
            driver.find_element_by_css_selector(".searchtrigger").click()
            sleep(5)
            driver.find_element_by_id("s").send_keys(f'{search}')
            driver.find_element_by_id("s").send_keys(Keys.ENTER)
            sleep(5)
            driver.find_element_by_css_selector(".search-post:nth-child(1) > .content a").click()
        except Exception as e:
            with open("Logs.txt", "w") as f:
                f.write(str(e))

    elif https.startswith('https://www.mediafax.ro'):
        try: # WORKS 21.03.2020
            driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[6]/iframe"))
            driver.find_element_by_css_selector(".btn-success").click()
            driver.switch_to.default_content()
            driver.find_element_by_xpath("//input[@id='searchQuery']").send_keys(f'{search}')
            driver.find_element_by_xpath("//form[@id='searchform']/fieldset/input[2]").click()
            sleep(5)
            driver.find_element_by_css_selector("li:nth-child(1) .thumb img").click()
        except Exception as e:
            with open("Logs.txt","w") as f:
                f.write(str(e))


    driver.get_screenshot_as_file("capture1.png")
    new_https = driver.current_url
    return new_https


if __name__ == "__main__":
    crawl('https://www.mediafax.ro/','moneda')