import requests


class BaiDuFanYi(object):
    def getfanyi(self, word):
        url = 'https://fanyi.baidu.com/sug'
        # 进行UA伪装
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36'
        }
        # post请求参数处理
        data = {
            'kw': word
        }
        # 发送请求
        response = requests.post(url=url, data=data, headers=headers)
        # 只有响应数据类型为json, 才能使用response.json
        text = response.json()
        # print(text['data'])
        res_text = ''
        for one in text['data']:
            # print(one['k'], one['v'])
            res_text += one['k'] + ":" + one['v'] + "\r\n"

        # 以json的格式保存字典形式的数据
        # filename = data['kw'] + '.json'
        # with open(filename, 'w', encoding='utf-8') as df:
        #     json.dump(response.json(), fp=df, ensure_ascii=False)  # 因为我们拿到的这个dic_obj是中文的，中文是不能用ascii的
        # return res_text


if __name__ == '__main__':
    word = "hello"
    res_text = BaiDuFanYi().getfanyi(word)
    print(res_text)
