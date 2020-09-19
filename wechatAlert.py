import requests
import json
import traceback
from urllib.parse import urlencode,quote
from config import templateCode,appCode,secretKey

# wechat alert is implemented by https://manage.wangfengta.com/
def alarm_wechat(warningLevel="4",xmstartTime="2021",mzstartTime="2020"):
    try:
        settings = {'templateCode':templateCode,'appCode':appCode,'secretKey':secretKey}
        params = {"warningLevel":str(warningLevel),"xmstartTime":xmstartTime,"mzstartTime":mzstartTime}
        params = quote(json.dumps(params))
        res = requests.get("https://api.wangfengta.com/api/alarm",{**settings,"params":params})
        print("Wechat Alert has been sent")
    except:
        print("Error: wechat alert api failed")
        print(traceback.format_exc())

if __name__=="__main__":
    alarm_wechat()