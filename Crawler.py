import base64
import requests
from bs4 import BeautifulSoup
from urllib import parse


class PcStoreCrawler():
    def fetchIt(self, inputText):
        searchText = base64.b64encode(
            str.encode(parse.quote(inputText))
        #既然都斷行了就乾脆點再斷一個
        ).decode()
        
        #這邊用format的方式寫，在維護上比較不會那麼亂
        #url = "https://www.pcstore.com.tw/adm/psearch.htm?store_k_word={}&slt_k_option=1".format(searchText)
        url = "https://www.pcstore.com.tw/adm/psearch.htm?store_k_word=" + \
            searchText + "&slt_k_option=1"
        #get要習慣插上header，對然常常會卡死
        res = requests.get(url)
        res.encoding = 'big5'
        soup = BeautifulSoup(res.text, 'html.parser')
        item = soup.select("div.pic2t_bg > a")
        titleArray = []
        #除非確定就是任意數 不然盡量別用i做為迴圈變數
        for i in item:
            #可以的話這樣寫 比較好維護，至少三個月後的你會看的懂
            #r_data = i.get_text()
            #titleArray.append(r_data)
            titleArray.append(i.get_text())
        return titleArray


print("This is example")
inputText = input("請輸入關鍵字: ")
crawlerOne = PcStoreCrawler()
print(crawlerOne.fetchIt(inputText))
