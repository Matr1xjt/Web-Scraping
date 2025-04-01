import requests
if __name__ == "__main__":
    #Step 1  指定url
    url = 'https://www.sogou.com/'
    #Step 2  发起请求
    #get 返回响应对象
    response = requests.get(url=url)
    #Step 3  获取响应数据
    page_text = response.text
    print(page_text)
    #Step 4  持久化存储
    with open('./sougou.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
    print("over")