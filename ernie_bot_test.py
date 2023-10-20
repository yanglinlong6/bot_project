# 填充API Key与Secret Key
import json

import requests


def main():
    url = "https://aip.baidubce.com/oauth/2.0/token?client_id=m1TnMkvM2TDNfiTXyphAHMmM&client_secret=k2tLraba4cO4P4Moxuh6zKnQtDFU5RtA&grant_type=client_credentials"

    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json().get("access_token")


if __name__ == '__main__':
    access_token = main()
    print(access_token)
