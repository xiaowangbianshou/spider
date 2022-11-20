import requests
from lxml import etree
import re
import pprint
import json
import os

print('ok')
filename = '梨视频-video\\'
if not os.path.exists(filename):
    os.mkdir(filename)

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Mobile Safari/537.36'
}
url = 'https://www.pearvideo.com/category_5'
pagetext = requests.get(url, headers=headers).text
tree = etree.HTML(pagetext)
li_list = tree.xpath('//*[@id="listvideoListUl"]/li')
for li in li_list:
    href = li.xpath('./div/a/@href')[0]
    name = li.xpath('./div/a/div[2]/text()')[0]
    id = re.findall("\d+", href)[0]
    video_url = 'https://www.pearvideo.com/videoStatus.jsp?contId={}'.format(
        id)
    headers_video = {
        'Referer': 'https://www.pearvideo.com/{}'.format(href),
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Mobile Safari/537.36'
    }
    video_url_pagetext = requests.get(
        url=video_url, headers=headers_video).json()
    # pprint.pprint(video_url_pagetext)
    srcurl = video_url_pagetext['videoInfo']['videos']['srcUrl']
    #print(srcurl, name)
    # method 1
    now_time = video_url_pagetext['systemTime']
    true_video_url = srcurl.replace(now_time, 'cont-{}'.format(id))

    # method 2
    # strings1 = '/'.join(srcurl.split('/')[:-1])
    #strings2 = '-'.join(srcurl.split('-')[1:])
    #true_video_url = strings1+'/cont-'+id+'-'+strings2

    print(name, true_video_url)

    '''video_content = requests.get(url=true_video_url, headers=headers).content
    print('Is loading video')
    with open(filename+name+'.mp4', 'ab') as f:
        f.write(video_content)
    print('ok')'''
