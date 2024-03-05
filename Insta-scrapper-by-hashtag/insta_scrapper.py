import json
import time
import pandas as pd


# def to_json(data_list):
#     hash_obj = json.dumps(data_list,indent=4)
#     with open("json/instagram_data.json", "w") as ts:
#         ts.write(hash_obj)

def to_csv_file(data_list):
  # Convert the DataFrame to a CSV file
  df = pd.json_normalize(data_list)
  df.to_csv(f'Instagram_hashtag_data.csv', index=False)

def get_soup(url):
    from bs4 import BeautifulSoup as bs
    import requests
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405'}
    #     headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    with requests.get(url, headers=headers, stream=True) as res:
        soup = bs(res.text, 'html.parser')
    return soup



def slow_scrolling(_time,scrolling_count,driver):
    # Importing necessary libraies
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight/{scrolling_count});")
    time.sleep(_time)
    for i in range(1,scrolling_count):
        driver.execute_script(f"window.scrollTo(document.body.scrollHeight*{i}/{scrolling_count}, document.body.scrollHeight*{i+1}/{scrolling_count});")
        time.sleep(_time)
    driver.execute_script(f"window.scrollTo(0, -document.body.scrollHeight);")
    time.sleep(_time)

def get_data(hashtag):
    import re
    import time
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.action_chains import ActionChains
    url = f"https://www.instagram.com/explore/tags/{hashtag}"
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')  
    options.add_argument("start-maximized") 
    driver = webdriver.Chrome (options=options)
    data_list = []
    try :
      driver.get(url)
      time.sleep(5)


      #scroll the page to the bottom so all the entities will appear
      slow_scrolling(.3,25,driver)
      time.sleep(2)


      #get the link of all post
      post_links = driver.find_elements(By.XPATH,'//div[@class="_aabd _aa8k  _al3l"]/a')
      post_links = [i.get_attribute('href') for i in post_links]

      print(f"{len(post_links)} record found out..")

      
      for li in post_links :
          driver.get(li)
          time.sleep(5)
          my_dict = {}
          final_image = ''
          image = ''
          vid = ''
          caption = ''
          try :
            for j in range(1,9) :
                driver.find_element(By.XPATH,'//button[@class=" _afxw _al46 _al47"]').click()
                time.sleep(1)
          except:
              pass
          try :
              image = driver.find_elements(By.XPATH,'//div[@class="x1qjc9v5 x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x78zum5 xdt5ytf x2lah0s xk390pu xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 xggy1nq x11njtxf"]//img')
          except Exception as e:
              # print(e)
              image = ''
              pass
          try :
              vid = driver.find_elements(By.XPATH,'//div[@class="x1qjc9v5 x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x78zum5 xdt5ytf x2lah0s xk390pu xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 xggy1nq x11njtxf"]//video').get_attribute('src')
          except Exception as e:
              # print(e)
              vid = ''
              pass
          soup_caption = get_soup(li)
          caption = soup_caption.text.replace("\n",'')
          if image :
            if len(image) > 1 :
                image_list = list(set([x.get_attribute('src') for x in image]))
                image = " ;".join([x for x in image_list])

            else :
                image = image[0].get_attribute('src')
            final_image = image
          if vid :
              if len(vid) > 1 :
                  vid_list = list(set([x.get_attribute('src') for x in vid]))
                  vid = " ;".join([x for x in vid])
              else :
                  vid = vid[0].get_attribute('src')
              final_image = vid
          my_dict['post url'] = li
          if final_image :
              my_dict['post image'] = final_image.strip(";")
          if caption :
              caption = caption.split("Instagram:")[1].strip()
              my_dict['post caption'] = caption.replace('\"','').replace("#"," #").strip()

          data_list.append(my_dict)
    except Exception as e :
        return f"Error:{e}"

    finally:
        driver.quit()
    return data_list


if __name__ =="__main__":
    hastag = input("Enter The Hastag value : ")
    print(f"Fetching data...")
    data_list = get_data(hashtag=hastag)
    to_csv_file(data_list)
    # to_json(data_list)
    print("data extracted successfully")
	



