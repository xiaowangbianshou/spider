from pickletools import read_uint1
from tabnanny import filename_only
import requests
from lxml import etree
import os
import json
from tqdm import tqdm
from unrar import rarfile

filename = 'ppt模板_rar\\'
if not os.path.exists(filename):
    os.makedirs(filename)

filename_ppt = 'ppt模板\\'
if not os.path.exists(filename_ppt):
    os.makedirs(filename_ppt)


page_max = int(input('请输入要爬取的最大页:'))
page_list = []
for i in range(2, page_max+1):
    page_list.append(i)
page_list
for i in tqdm(page_list, 'ppt模板爬取进度'):
    page = int(i)
    url = 'https://sc.chinaz.com/ppt/free_{}.html'.format(page)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Mobile Safari/537.36'
    }
    page_text = requests.get(url=url, headers=headers).text
    # print(page_text)
    page_text_etree = etree.HTML(page_text)
    page_text_etree_list = page_text_etree.xpath(
        '//div[@class="bot-div"]/a/@href')
    # print(page_text_etree_list)
    for div in page_text_etree_list:
        #download_src = div.xpath('./a/@href')[0]
        download_title = 'https://sc.chinaz.com'
        download_url = download_title+div

        download_html = requests.get(url=download_url, headers=headers).text
        download_html_etree = etree.HTML(download_html)
        ppt_download_url = download_html_etree.xpath(
            '//div[@class="download-url"]/a/@href')
        ppt_name = download_html_etree.xpath(
            '//h1[@class="title"]/text()')
        ppt_name = "".join(ppt_name)

        ppt_name = ppt_name.encode('iso-8859-1').decode('utf-8', 'ignore')
        if len(ppt_download_url) > 0:
            ppt_content = requests.get(
                url=ppt_download_url[0], headers=headers).content
            with open(filename+ppt_name+'.rar', 'wb') as f:
                f.write(ppt_content)
            rar_filename = './ppt模板_rar/'+ppt_name+'.rar'
            ppt_filename = './ppt模板/'+ppt_name
            # print(rar_filename)
            # print(ppt_filename)
            rar = rarfile.RarFile(rar_filename)
            ppt_filename = './ppt模板'
            if not os.path.exists(ppt_filename):
                os.makedirs(ppt_filename)
            rar.extractall(ppt_filename)

            rar_list = rar.namelist()[0].split('\\')[0]
            oldname = os.path.join('./ppt模板', rar_list)
            newname = os.path.join('./ppt模板', ppt_name)
            os.rename(oldname, newname)
