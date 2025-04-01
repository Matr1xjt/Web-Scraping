import requests
import json
if __name__ == '__main__':
    pageindex = 1
    url ='https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    param = {
            'cname':'杭州',
             'pid':'',
             'pageindex':pageindex,
             'pageSize':'10'}
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0'
    }
    while(pageindex!=50):
        responce = requests.get(url=url,params=param,headers=headers)

        page_text = responce.text

        print(page_text)
        with open('./kfc.csv','a',encoding='utf-8') as fp:
            fp.write(page_text)
        pageindex+=1   
    print('over')
    


