#  先安裝第三方函式庫--requests
#  先安裝第三方函式庫--BeautifulSoup

import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/Gossiping/index.html"  # PPT 八卦版
res = requests.get(url, cookies={'over18': '1'})

# 吃兩個參數，第一個放html文本，第二個放parser
Soup = BeautifulSoup(res.text, 'html.parser')

# print(Soup.title)  # 可以讀取的網頁的title
# print(Soup.title.text)  # 顯示文字就好，不用顯示<tag>

"""
find有兩個常用的用法：
1. 直接接標籤名稱
- Soup.find(‘a’) 可以直接找到第一個a標籤的元素
- Soup.find(‘p’) 可以直接找到第一個p標籤的元素

2. 屬性名稱用鍵值方式對應
- Soup.find(class_=’demo1’) 可以找到第一個class為’demo1’的元素
！要注意的是因為python中class是保留字，所以要用class_才能表達
- Soup.find(id=’demo2’) 可以找到第一個id為’demo2’的元素
- Soup.find(type=’demo3’) 可以找到第一個type為’demo3’的元素
"""
# step1 = Soup.find(class_='r-ent') find可以找到第一個class為'r-ent'的元素
# step2 = step1.find(class_='title') 標題是在class = r-ent下層的 class = title的a標籤，所以我們可以再find一次來找到我們的第二層
# step3 = step2.find("a") 再用find找到a標籤
a = Soup.find(class_='r-ent').find(class_='title').find("a")
print(a.text)

# 可以用get這個方式來把屬性內的資料讀出來，或是像是字典一樣，用[‘屬性名稱’]來讀取
# a.get('href') || a['href']
print(a.get('href'))

# 把該頁每一篇的文章都做一樣的事情，這時候我們要用find_all的方式
# find_all的用法基本上跟find一模一樣，只是他會回傳一個list
for i in Soup.find_all(class_='r-ent'):
    print(i.find(class_='title').a.text)  # 印出標題
    print('https://www.ptt.cc', end='')  # 因為href中的網址不完整，要補上
    print(i.find(class_='title').a['href'])  # 然後跟上面的接在一起
