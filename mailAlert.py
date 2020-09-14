#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import datetime
import time
import smtplib
import traceback
from email.mime.text import MIMEText
from email.header import Header
from config import from_addr,password,to_addr

def alarm_email(warningLevel=0,xmstartTime="2020",mzstartTime="2020"):
    smtp_server = 'smtp.163.com'
    contents = """
        风险等级: %d
        开始时间：小米天气 %s， 魅族天气 %s
    """%(warningLevel,xmstartTime,mzstartTime)
    msg = MIMEText(contents, 'plain', 'utf-8')
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header('该收衣服了')
    try:
        server = smtplib.SMTP_SSL()
        server.connect(smtp_server, 465)
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addr, msg.as_string())
        server.quit()
        print('mails have been sent')
    except smtplib.SMTPException:
        print("Error: mails can't be sent")
        print(traceback.format_exc())
        return False
    return True

if __name__=="__main__":
    alarm_email()