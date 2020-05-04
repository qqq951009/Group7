from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os
import datetime
def composit(path_list):
    toImage = Image.new('RGB', (128,64),(255,255,255))
    img1 = Image.open(path_list[0])
    img12 = Image.open(path_list[1])
    img1 = img1.resize((64, 64),Image.ANTIALIAS)
    img12 = img12.resize((64, 64),Image.ANTIALIAS)
    toImage.paste(img1, (0, 0))
    toImage.paste(img12, (64, 0, 64 + img1.size[0], 0 + img1.size[1]))

    #函式描述：toImage:背景圖片,paste()函式四個變數分別為：起始橫軸座標，起始縱軸座標，橫軸結束座標，縱軸結束座標；
    plt.imshow(toImage)
    plt.title("level")
    plt.show()

    theTime = datetime.datetime.now()
    str_time=str(theTime).replace(".","_")
    str_time=str_time.replace(":","_")

    
    folder_path="./composite_image/"+str_time

    if(os.path.exists(folder_path)== False):
        os.makedirs(folder_path)

    image_path=folder_path+"/merge.jpg"
    toImage.save(image_path)
    return image_path
