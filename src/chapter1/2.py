
#UA伪装 - 反爬
import requests
if __name__ == "__main__":
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0'
    }
    #url = 'https://www.sogou.com/web?query=%E6%B3%A2%E6%99%93%E5%BC%A0'
    url = 'https://www.sogou.com/web'
    #处理url携带的参数：封装至字典中
    kw = input('enter a word:')
    param = {
        'query':kw
    }
    #带参数的请求
    responce = requests.get(url=url,params=param,headers=headers)

    #获取响应数据
    page_text = responce.text

    #存储
    filename = kw+'.html'
    with open(filename,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(filename,"over")