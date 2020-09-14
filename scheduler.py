from mailAlert import alarm_email
from wechatAlert import alarm_wechat
from getDataReport import hourly_report
from config import switch, mail_alert, wechat_alert

if switch:
    warningLevel,mzstartTime,xmstartTime = hourly_report()
    if warningLevel > 1:
        if mail_alert:
            alarm_email(warningLevel,mzstartTime,xmstartTime)
        if wechat_alert:
            alarm_wechat(warningLevel,mzstartTime,xmstartTime)