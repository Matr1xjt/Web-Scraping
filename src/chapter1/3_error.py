import requests
if __name__ == "__main__":
    post_url = 	'https://fanyi.baidu.com/sug'
    data={
        'kw':'dog'
    }
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
    }

    response = requests.post(url=post_url,data=data,headers=headers)

    #json 返回对象
    dic_obj = response.json()
    print(dic_obj)