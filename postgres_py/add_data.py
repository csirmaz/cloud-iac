
# Connect to posrges database
# https://www.psycopg.org/docs/


import psycopg2
import os
import time
import random

conn = psycopg2.connect(
    dbname=os.getenv('DATABASE_NAME'),
    user=os.getenv('DATABASE_USER'),
    password=os.getenv('DATABASE_PASSWORD'),
    host=os.getenv('DATABASE_HOST')
)

cur = conn.cursor()

cur.execute("create table if not exists dbt_sample.bronze_data (unixtime int, personid int, productid int, price int)")

now = time.time()
for i in range(1000):
    cur.execute("insert into dbt_sample.bronze_data (unixtime, personid, productid, price) values (%s,%s,%s,%s)",
                [now, random.randint(100, 199), random.randint(500,599), random.randint(1,100)])

cur.close()

conn.commit()
