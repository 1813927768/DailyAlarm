from mailAlert import alarm_email
from wechatAlert import alarm_wechat
from getDataReport import hourly_report

warningLevel,mzstartTime,xmstartTime = hourly_report()
if warningLevel > 1:
    alarm_email(warningLevel,mzstartTime,xmstartTime)
    alarm_wechat(warningLevel,mzstartTime,xmstartTime)