import os
import urllib.request
import random

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from urllib3.exceptions import MaxRetryError


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        print("---  new folder...  ---")
        print("---  OK  ---")
    else:
        print("---  There is this folder!  ---")


def get_pic_by_url(folder_path, picurl, filename):
        print("Try downloading file: {}".format(picurl))
        filepath = folder_path + '/' + filename + '.png'
        if os.path.exists(filepath):
            print("File have already exist. skip")
        else:
            try:
                urllib.request.urlretrieve(picurl, filename=filepath)
            except Exception as e:
                print("Error occurred when downloading file, error message:")
                print(e)


if __name__ == '__main__':
    file = "E:\\pic_download"
    mkdir(file)
    ch_options = Options()
    ch_options.add_argument('--headless')
    driver = webdriver.Chrome(options=ch_options)
    for page in range(0, 5):
        driver.get("https://so.toutiao.com/search?keyword=%E7%BE%8E%E5%A5%B3&pd=atlas&source=search_subtab_switch&dvpf=pc&aid=4916&page_num=" + str(page))
        time.sleep(3)
        print(driver.title)
        pics = driver.find_elements_by_xpath("//div[@class='abs-fill']/img")
        title = driver.find_elements_by_xpath("//div[@class='abs-fill']/img/../../../../div[2]/div/div")
        for i in range(0, len(pics)):
            attribute = pics[i].get_attribute("src")
            url = str(attribute).split("~")[0].replace("img", "obj")
            name = title[i].get_attribute("title")
            print(url, name)
            get_pic_by_url(file, url, name)
        time.sleep(random.randint(0, 5))
    driver.quit()