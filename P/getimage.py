import requests
import urllib.request
from bs4 import BeautifulSoup
import os
import time
import json
import datetime
from googletrans import Translator

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

translator=Translator();

cn_key=input("key: ")

key=translator.translate(cn_key).text

url="https://www.flaticon.com/search?word="+key
photo_limit=5


headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36","upgrade-insecure-requests":"1"}
response = requests.get(url,headers = headers)
soup = BeautifulSoup(response.content,"html.parser")


items = soup.find_all("img",attrs={"class":"lzy"})

theTime = datetime.datetime.now()
str_time=str(theTime).replace(".","_")
str_time=str_time.replace(":","_")

print(str_time)

folder_path="./image/"+str_time+"/"+key+"/"

if(os.path.exists(folder_path)== False):
    os.makedirs(folder_path)

img_arr=[]

for index , item in enumerate(items):
    if(item and index < photo_limit):
         html = requests.get(item.get("data-src"))
         img_name = folder_path + str(index+1)+".png"

         img_arr.append(img_name);

         print("finish",index+1)
    else:
        break

    with open(img_name,"wb") as file:
        file.write(html.content)
        file.flush()
    file.close()

    

    time.sleep(1)
print("done")        

#顯示圖片

toImage = Image.new('RGB', (128,64),(255,255,255))
img1 = Image.open(img_arr[0])
img12 = Image.open(img_arr[1])
img1 = img1.resize((64, 64),Image.ANTIALIAS)
img12 = img12.resize((64, 64),Image.ANTIALIAS)
toImage.paste(img1, (0, 0))
toImage.paste(img12, (64, 0, 64 + img1.size[0], 0 + img1.size[1]))

#函式描述：toImage:背景圖片,paste()函式四個變數分別為：起始橫軸座標，起始縱軸座標，橫軸結束座標，縱軸結束座標；
toImage.save("merged.png")
plt.imshow(toImage)
plt.title("level")
plt.show()