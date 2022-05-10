import requests
from bs4 import BeautifulSoup
import time

today = time.strftime("%Y-%m-%d", time.gmtime(time.time()+8*60*60))

bing_url = "https://www.bing.com"
html_class = requests.get(bing_url)

soup = BeautifulSoup(html_class.content, 'lxml')

img_loc_soup_1 = soup.select('#vs_cont > div.mc_caro > div.musCard > div.musCardCont > ul > li:nth-child(4) > a')
img_loc_soup_2 = soup.select('body > div.hpapp > div > div:nth-child(1) > div')
if img_loc_soup_1  != []:
    print('#1')
    img_loc = img_loc_soup_1[0]['href']   # 这里应该是列表结构，只有一个元素，元素内通过键值定位
    img_url = bing_url + img_loc
else :
    print('#2')
    img_loc = str(img_loc_soup_2[0]).split('(')[1].split(')')[0]
    img_url = img_loc

print('Downloading...'+img_url)
img_file = requests.get(img_url).content
open('./img/bing-'+today+'.jpg','wb').write(img_file)
