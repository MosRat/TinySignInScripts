import json
import pprint
from config import *

import requests

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
    'if-none-match': 'W/"15e326e54d8b1f6423dcfd141e2db58e2ff8c219"',
}

params = {
    'type': '4',
    'page': '1',
    'count': '10',
    'access_token': access_token,
    'tag': '0',
    'keyword': '',
}

response = requests.get('https://api-xcx-qunsou.weiyoubot.cn/xcx/checkin/v3/list', params=params, headers=headers,
                        verify=False)
pprint.pprint(response.json()['data'])
json.dump([{'cid': i['cid'], 'name': i['title']} for i in response.json()['data']], open('info.json', 'w',
                                                                                       encoding='utf8'), ensure_ascii = False)
