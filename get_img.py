import requests
from bs4 import BeautifulSoup
import time

today = time.strftime("%Y-%m-%d", time.gmtime(time.time()+8*60*60))

bing_url = "https://www.bing.com"
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
html_class = requests.get(bing_url, headers=header)

soup = BeautifulSoup(html_class.content, 'lxml')

img_loc_soup_1 = soup.select('#vs_cont > div.mc_caro > div.musCard > div.musCardCont > ul > li:nth-child(4) > a')
img_loc_soup_2 = soup.select('body > div.hpapp > div > div:nth-child(1) > div')

if img_loc_soup_1  != []:
    print('#1')
    img_loc = img_loc_soup_1[0]['href']   # 这里应该是列表结构，只有一个元素，元素内通过键值定位
    img_url = bing_url + img_loc
else :
    print('#2')
    print(img_loc_soup_2)
    img_loc = str(img_loc_soup_2[0]).split('(')[1].split(')')[0]
    temp_url = img_loc.split("net")[1]
    img_url = bing_url + temp_url

print('Downloading...'+img_url)
img_file = requests.get(img_url, headers=header, timeout=10).content
open('./img/bing-'+today+'.jpg','wb').write(img_file)
