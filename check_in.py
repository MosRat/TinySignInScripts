from pprint import pprint
from config import *

import requests


def check(cid):
    headers = {
        'Host': 'api-xcx-qunsou.weiyoubot.cn',
        'xweb_xhr': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309080f)XWEB/8461',
        'content-type': 'application/json',
        'accept': '*/*',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://servicewechat.com/wxee55405953922c86/720/page-frame.html',
        'accept-language': 'zh-CN,zh;q=0.9',
    }

    json_data = {
        'cid': cid,
        'access_token': access_token,
        # 'fill_params': [
        #     {
        #         'key': 1,
        #         'val': '11111',
        #     },
        # ],
        "wifi_location_info": {
            "latitude": 39.960768625482984,
            "longitude": 116.36689916253091,
            "wifi": ""
        },
        'wifi_match': 0,
    }

    response = requests.post('https://api-xcx-qunsou.weiyoubot.cn/xcx/checkin/v3/doit', headers=headers, json=json_data,
                             verify=False)
    pprint(response.json())


# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
# data = '{"cid":"655b7ffa19554f1e9f2061fa","access_token":"1639a8a9e6f3456fb37732effa092a21","fill_params":[{"key":1,"val":"11111"}],"wifi_match":0}'
# response = requests.post('https://api-xcx-qunsou.weiyoubot.cn/xcx/checkin/v3/doit', headers=headers, data=data)

if __name__ == '__main__':
    check("655b85ad63426d4c8c1db840")
