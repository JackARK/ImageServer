import os
import time

import requests
from bs4 import BeautifulSoup

# 默认种子
randomSeed = 'iKunJs'
download_page_num = 30;


def download_a_page(input_url: str, num: int):
    input_url = input_url + str(num)
    res = requests.get(input_url)
    soup = BeautifulSoup(res.text, "html.parser")
    preview_tags = soup.select(".preview")
    view_urls = []
    for element in preview_tags:
        view_urls.append(str(element['href']))

    image_urls = []

    for urls in view_urls:
        time.sleep(1)
        view_page = requests.get(urls)
        view_page_soup = BeautifulSoup(view_page.text, "html.parser")
        image_tags = view_page_soup.select("#wallpaper")
        print("The URL of the details page is: " + urls)
        if len(image_tags) != 0:
            for imageTag in image_tags:
                image_urls.append(str(imageTag['src']))
                print("The URL of the image is:" + str(imageTag['src']))
    print("OK，I have get the urls in this page.Let's download them.")

    for input_url in image_urls:
        time.sleep(1)
        print("Downloading url: " + input_url)
        down = requests.get(input_url)
        file_name = os.path.basename(input_url)
        save_path = './images/' + file_name
        if down.status_code == 200:
            image_content = down.content
            with open(save_path, 'wb') as file:
                file.write(image_content)
                print("A image has been stored :" + save_path)
        else:
            print('Something went wrong')


print("Do not download too much times,or the website load will be high")
url = "https://wallhaven.cc/toplist?page="

for i in range(9, download_page_num, 1):
    print("We don't want to bother this website ,so let's take a breathe,wait for 3 seconds.")
    print("We are downloading page: " + str(i))
    download_a_page(url, i)

    time.sleep(3)
