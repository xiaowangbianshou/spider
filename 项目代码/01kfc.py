from ast import keyword
import json
from urllib import response
import requests
import pprint
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
cityname = input('enter a cityname:')
for i in range(1, 4):
    data = {
        'cname': '',
        'pid': '',
        'keyword': cityname,
        'pageIndex': i,
        'pageSize': '10'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Mobile Safari/537.36'
    }

    response = requests.post(url, data, headers)

    text = response.text

    #fileName = cityname + '第'+str(i)+'页KFC.txt'
    # with open(fileName, 'w', encoding='utf-8') as fp:
    #   fp.write(text)
    pprint.pprint(text)
print('over!')
