import json

import requests

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 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'}

data = {'prompt': '您的提示文本',
        'temperature': 0.5,  # 生成文本的创造性程度
        'max_tokens': 50,  # 最大生成的标记数
        }

response = requests.post('https://api.openai.com/v1/engines/davinci-codex/completions', headers=headers,
                         data=json.dumps(data))
print(response.json())
