import json

import openai


# 目前需要设置代理才可以访问 api
# os.environ["HTTP_PROXY"] = "自己的代理地址"
# os.environ["HTTPS_PROXY"] = "自己的代理地址"


def get_api_key():
    # 可以自己根据自己实际情况实现
    # 以我为例子，我是存在一个 openai_key 文件里，json 格式
    '''
    {"api": "你的 api keys"}
    '''
    openai_key_file = './envs/openai_key'
    with open(openai_key_file, 'r', encoding='utf-8') as f:
        openai_key = json.loads(f.read())
    print(openai_key)
    return openai_key['api']


openai.api_key = get_api_key()

q = "用python实现：提示手动输入3个不同的3位数区间，输入结束后计算这3个区间的交集，并输出结果区间"
print(q)
rsp = openai.ChatCompletion.create(
    model="whisper-1",
    messages=[
        {"role": "system", "content": "一个有10年Python开发经验的资深算法工程师"},
        # {"role": "user", "content": q}
    ]
)

print(q)
