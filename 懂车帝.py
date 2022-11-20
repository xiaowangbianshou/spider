import requests
import pandas as pd
url = 'https://www.dongchedi.com/motor/pc/car/series/car_list?series_id=4865&city_name=%E6%B9%96%E5%B7%9E'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}
data = {'series_id': 4865, 'city_name': '湖州'}
response = requests.get(url, headers=headers, data=data).json()
car_id_list = []  # 查找汽车id
car_name_list = []  # 查找汽车名字
car_list = response['data']['tab_list'][0]['data']
for i in range(1, len(car_list)):
    try:
        car_id = car_list[i]['info']['id']
        car_name = car_list[i]['info']['name']
        car_id_list.append(car_id)
        car_name_list.append(car_name)
    except:
        continue

buyer_car_list = []
buyer_city_list = []  # 买家城市
naked_price_list = []  # 车主价格
full_price_list = []  # 购买总价

for i in car_id_list:
    buyer_car_name = car_name_list[car_id_list.index(i)]
    for page in range(1, 20):
        try:
            detail_url = 'https://www.dongchedi.com/motor/pc/car/series/car_price_list?car_id={}&city_name=%E6%B9%96%E5%B7%9E&selected_city_name=%E5%85%A8%E5%9B%BD&page=1&pageSize=10'.format(
                i, page)  # car_id用car_id_list拼接page拼接页数进行网址拼接
            response = requests.get(detail_url, headers=headers).json()
            buyer_list = response['data']['car_price_data_list']
            for j in range(0, len(buyer_list)):
                buyer_city = buyer_list[j]['bought_city_name']
                naked_price = buyer_list[j]['naked_price']
                full_price = buyer_list[j]['full_price']
                buyer_city_list.append(buyer_city)
                naked_price_list.append(naked_price)
                full_price_list.append(full_price)
                buyer_car_list.append(buyer_car_name)
        except:
            break

infrom = {'购买车辆': buyer_car_list, '购买城市': buyer_city_list,
          '车主价格': naked_price_list, '购买总价': full_price_list}
df1 = pd.DataFrame(infrom)
df1.to_excel('')
