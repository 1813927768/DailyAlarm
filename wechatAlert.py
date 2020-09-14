import requests
import json
from urllib.parse import urlencode,quote
from config import templateCode,appCode,secretKey

# wechat alert is implemented by https://manage.wangfengta.com/
def alarm_wechat(warningLevel="4",xmstartTime="2021",mzstartTime="2020"):
    settings = {'templateCode':templateCode,'appCode':appCode,'secretKey':secretKey}
    params = {"warningLevel":str(warningLevel),"xmstartTime":xmstartTime,"mzstartTime":mzstartTime}
    params = quote(json.dumps(params))
    res = requests.get("https://api.wangfengta.com/api/alarm",{**settings,"params":params})
    return res

if __name__=="__main__":
    alarm_wechat()