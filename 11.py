
import random
ips = [('36.6.149.154:xxx'),('114.233.125.55:xxxxx'),('117.26.229.24:xxx'),('122.241.27.24:xxxxx'),('61.132.171.215:xxx'),]
url = 'http://httpbin.org/ip'
for i in range(5):
    try:
        ip = random.choice(ips)
        res = requests.get(url, proxies={'http':ip}, timeout=1)
        print(res.text)
    except Exception as e:
        print('出现异常', e)
