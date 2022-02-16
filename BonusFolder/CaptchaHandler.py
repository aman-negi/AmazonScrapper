# for handling or filling the captcha we can use ocr to get the text of the image
import easyocr

# For scrapping I am using selenium to time the requests and be able to handle the data set
from selenium import webdriver 
from selenium.webdriver.common.by import By


wd = webdriver.Edge(r"C:\Users\negia\Desktop\python\Credicxo python\assignment\msedgedriver.exe")

def captchaTextExtractor(img_url):
  IMAGE_PATH = img_url
  reader = easyocr.Reader(['en'],gpu=True)
  result = reader.readtext(IMAGE_PATH)
  return result[0][1]

def getCaptchaImgLink(site_url):
  img_tag =  '/html/body/div/div[1]/div[3]/div/div/form/div[1]/div/div/div[1]/img'
  wd.get(site_url)
  element = wd.find_element(By.XPATH, img_tag)
  link = element.get_attribute('src')
  return link

def fillTheCaptcha(text):
    captcha_tag = '//*[@id="captchacharacters"]'
    wd.find_element(By.XPATH, captcha_tag).send_keys(text)
    submit_tag = '/html/body/div/div[1]/div[3]/div/div/form/div[2]/div/span/span/button'
    wd.find_element(By.XPATH, submit_tag).click()
    
def handleCaptcha(url):
    while(1):
        # site_url = "https://www.amazon.com/errors/validateCaptcha"
        site_url = url
        img_url = getCaptchaImgLink(site_url)
        captcha = captchaTextExtractor(img_url)
        fillTheCaptcha(captcha)
        n =  len(site_url)
        url_now = wd.current_url
        print(f"url_now -> {url_now} ")
        print(f"starting url -> {site_url}")
        if(site_url[:n] != url_now[:n] ):
            break
