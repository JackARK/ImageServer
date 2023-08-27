import requests
import os
import time
import json

folder_path = "C:/Users/33225/Downloads/bing"

file_names = []
for file_name in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, file_name)):
        file_names.append(file_name)
i = 1
for files in file_names:
    url = "https://img.saltfish.club/upload/phone"
    file_path = folder_path + "/" + files

    with open(file_path, "rb") as file:
        files = {"image": file}
        response = requests.post(url, files=files)

    print(file_path + response.text + "当前第" + str(i) + "张")
    i=i+1
