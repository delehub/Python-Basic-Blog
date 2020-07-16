
import requests
import re
import os


url = 'http://douyin.bm8.com.cn/day.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
}

response = requests.get(url=url,headers=headers)
data_text = response.text
# print(html_data)

# 数据解析


# 正则表达式
pattern = re.compile('open1\(\'(.*?)\',\'(.*?)\',\'\'\)')
result = pattern.findall(data_text)
# print(result)

for title,film_url in result:
    print(title,film_url)
    film_data = requests.get(url=film_url,headers=headers).content

    with open('video\\' + title + '.mp4',mode='wb') as f:
        f.write(film_data)
        print('保存完成：',title)



