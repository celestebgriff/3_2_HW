
import psycopg2
import sqlite3
import pandas as pd
import os

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")


pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()


df = pd.read_csv('titanic.csv')


df['Name'] = df['Name'].str.replace(r"[\"\',]", '')


sl_conn = sqlite3.connect('titanic.sqlite3')


df.to_sql('titanic', con=sl_conn, if_exists='replace')


sl_curs = sl_conn.cursor()


query = """SELECT *
FROM titanic
"""
titanic_sql = sl_curs.execute(query).fetchall()


create_passengers_table = """
CREATE TABLE titanic (
    index SERIAL PRIMARY KEY,
    survived INT,
    pclass INT,
    name VARCHAR(81),
    sex VARCHAR(10),
    age INT,
    siblings_spouses_aboard INT,
    parents_children_aboard INT,
    fare REAL
)
"""
pg_curs.execute(create_passengers_table)



for person in titanic_sql:
    insert_person = """
    INSERT INTO titanic
    (survived, pclass, name, sex, age,
    siblings_spouses_aboard, parents_children_aboard, fare)
    VALUES """ + str(person[1:]) + ";"
    pg_curs.execute(insert_person)

pg_conn.commit()
