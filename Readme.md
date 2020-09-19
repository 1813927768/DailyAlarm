DailyAlarm is a system to remind you of trivial things.

## Current Status

- send you an email to take your clothes back in rainy days
- send you an alert in wechat to take your clothes back in rainy days

## todo

- daily report 
- multiple user config files
- more usable config change

## Notice

- This program need a file `config.py` for configuration to start up.
- `crontab -e` to edit the cron file to custom the report time(`30 7-22 * * * /usr/local/bin/python3 /root/repos/DailyAlarm/scheduler.py > /root/repos/DailyAlarm/output.log 2>/dev/null`)

