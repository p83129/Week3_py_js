#連線上網址
import urllib.request as request
import json
src="https://data.taipei/api/v1/dataset/36847f3f-deff-4183-a5bb-800737591de5?scope=resourceAquire"
with request.urlopen(src) as response:
    data=json.load(response)

#找出json裡所需要的值，並開始資料處理
lst=data["result"]["results"] 
#打開(建立)新的txt檔，並寫入資料進去，編碼為"utf-8"
with open("data.txt","w",encoding="utf-8") as file:
    for data in lst:
        str=data["file"]

        #找出第一張圖片的網址。搜尋網址裡第二個"http"的位置，從而得知第二個http以前的網址為題目所要求的。
        int=str[1:].find("http")
        int = int+1 
        
        if(int>0):
            file.write(data["stitle"]+","+data["longitude"]+","+data["latitude"]+","+(str[0:int])+"\n")  
        else: #如果照片網址只有一個，那int回傳就會是-1，那我就直接從第0個到此字串全長來取完整的網址
             file.write(data["stitle"]+","+data["longitude"]+","+data["latitude"]+","+(str[0:len(str)])+"\n")  