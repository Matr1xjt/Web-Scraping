import requests
import json
if __name__ == '__main__':
    url ='https://movie.douban.com/j/chart/top_list'
    param = {
        'type':'24',
        'interval_id':'100:90',
        'action':'',
        'start':'40',
        'limit':'20'
    }
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0'
    }
    responce = requests.get(url=url,params=param,headers=headers)

    list_data = responce.json()

    print(list_data)
    fp = open('./douban.json','w',encoding='utf-8')

    json.dump(list_data,fp=fp,ensure_ascii=False)
    print('over')
    


