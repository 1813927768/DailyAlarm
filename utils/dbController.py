import sqlite3

conn = sqlite3.connect("../data/xiaomi_weather.db")
cursor = conn.cursor()
sql = """select name from citys where city_num = 101020500"""
cursor.execute(sql)
result = cursor.fetchall()
conn.close()