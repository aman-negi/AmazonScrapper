
# import required modules
from selenium import webdriver 
from selenium.webdriver.common.by import By
import pandas as pd  
import random
import time  
import json
#  for feedback regarding how much time it took to scrape 100 urls  
from datetime import datetime

  
# Driver Code
if __name__ == '__main__':
  
    df = pd.read_csv("Amazon Scraping - Sheet1.csv",index_col="Unnamed: 0")

    size_of_df =df.shape[0]
    
# create driver object
#   Exaple_>
    # wd = webdriver.Edge(r"C:\Users\negia\Desktop\python\Credicxo python\assignment\msedgedriver.exe")
    wd = webdriver.Edge("PATH_TO_WBDRIVER")
#   To store the data for our scrapping  
    data={}
    dic= {}
    
#   To store the time it took to complete each round
    time_log = []
    now = datetime.now()
    time_log.append(f' start time -> {str(now.strftime("%d/%m/%Y %H:%M:%S"))} \n')
    
    
    for i in range(0,size_of_df):
        url = f"https://www.amazon.{df['country'][i]}/dp/{df['Asin'][i]}"
        wd.get(url)
        data[i]={}
        dic[i]={}
        dic[i]['url'] = url
# A variable for checking wether the website has some content or not - we are assuming that if it don't have any content it wil be 404 status
        flag = True

# for title
        try:
            try:
                x_path = '//*[@id="titleSection"]'
                dic[i]["title"] = wd.find_element(By.XPATH, x_path).text
                data[i]['title'] = wd.find_element(By.XPATH, x_path).text
                flag =False
            except:
                x_path = '//*[@id="title"]'     
                dic[i]["title"] = wd.find_element(By.XPATH, x_path).text
                data[i]['title'] = wd.find_element(By.XPATH, x_path).text
                flag =False
                
        except:
            pass
        
        print('done title section')
# for getting img link
        try:
            try:
                x_path = '//*[@id="landingImage"]'
                dic[i]["img_url"] = wd.find_element(By.XPATH, x_path).get_attribute('src')
                data[i]["img_url"] = wd.find_element(By.XPATH, x_path).get_attribute('src')
                flag =False
                
            except:
                x_path = '//*[@id="imgBlkFront"]'    
                dic[i]["img_url"] = wd.find_element(By.XPATH, x_path).get_attribute('src')
                data[i]["img_url"] = wd.find_element(By.XPATH, x_path).get_attribute('src')
                flag =False
                
        except:
            pass
        
        print('done link section')
          
# For price as there are multiple options so we implied a for loop so that if any fails no value is added and try next option
        price_tag_list = [
                '//*[@id="corePrice_desktop"]/div/table/tbody/tr[2]/td[2]/span[1]',
                '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]',
                '//*[@id="availability"]/span',
                '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]',
                '//*[@id="corePrice_desktop"]/div/table/tbody/tr[1]/td[2]/span[1]',
                '//*[@id="a-autoid-10-announce"]/span[2]/span',
                '//*[@id="a-autoid-7-announce"]/font/span/span/font'
        ]    
        for x_path in price_tag_list:    
            try:
                dic[i]["price"] = wd.find_element(By.XPATH, x_path).text
                data[i]["price"] = wd.find_element(By.XPATH, x_path).text
                flag =False    
                break
            except:
                pass  
                
        print('done price section')
            
# for description
        des_tag_list = [
            '//*[@id="bookDescription_feature_div"]/div/div[1]',
            '//*[@id="feature-bullets"]',
        ]        
        for x_path in des_tag_list:    
            try:
                dic[i]["descriptiom"] = wd.find_element(By.XPATH, x_path).text
                data[i]["description"] = wd.find_element(By.XPATH, x_path).text
                flag =False
                break
            except:
                pass   
        print('done description section')
        print(i)
        
#   If flag value is still the same that means that the website isn't available
        if flag == True :
            dic[i]["Error"] = "404"          

#   TO make it look like that our programm isn't a bot we make our bot wait for a unusual amount of time before moving to next url
        n = random.randint(0,3)
        time.sleep(n)
        
#   If we want to add bypass layer for handling we will be doing it here by checking wether the url is same as the url we were searching on or
#   is it the captcha error url
        dic[i]["urlTracker"] = wd.current_url
        
#   To make time log of the process
        if((i+1)%100==0):
            now = datetime.now()
            time_log.append(f'i -> {i} time -> {str(now.strftime("%d/%m/%Y %H:%M:%S"))} \n')
        
        
#   converting into json format file 
    with open("result.json", "w") as outfile:
        json.dump(dic, outfile)
    
    with open("runfiledata.json", "w") as outfile:
        json.dump(data, outfile)    
        
#   To store the time log we are entering the data into a file
    timefile = open('time_log.txt', 'w')
    timefile.writelines(time_log)
    timefile.close()