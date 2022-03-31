# to download from insta pages
from selenium import webdriver
import time
import urllib.request
import creds


def downloader(link_user, filename):
    driver = webdriver.Edge(
        executable_path=creds.selenuim_path)
    reel_link = link_user
    link = "https://www.isave.cc/post/"+reel_link[28:-1]
    print(link)
    driver.get(link)
    time.sleep(2)
    button = driver.find_element_by_class_name("card_download__OkDCX")
    button.click()
    # print(driver.current_url)
    urllib.request.urlretrieve(
        driver.current_url, f"{creds.path_to_download}/{filename}")
