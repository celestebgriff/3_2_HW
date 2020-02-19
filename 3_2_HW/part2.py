import pandas as pd
import sqlite3

df = pd.read_csv('buddymove_holidayiq.csv')

connection = sqlite3.connect('buddymove_holidayiq.sqlite3')

df.to_sql('review', con=connection)

result = connection.execute("SELECT COUNT(*) FROM review;").fetchall()

print("TOTAL ROWS:", result[0][0])

query = """
    SELECT COUNT("User Id")
    FROM review
    WHERE Nature >= 100 AND Shopping >= 100
    """
result = connection.execute(query).fetchall()
print("Total number of users who reviewed")
print(result[0][0])

query = """
    SELECT ROUND(AVG(Sports),2) as Sports,
        ROUND(AVG(Religious),2) as Religious,
        ROUND(AVG(Nature),2) as Nature,
        ROUND(AVG(Theatre),2) as Theatre,
        ROUND(AVG(Shopping),2) as Shopping,
        ROUND(AVG(Picnic),2) as Picnic
    FROM review
    """
result = connection.execute(query).fetchall()
print("The average number of reviews for each category")
print(f'Sports: {result[0][0]}')
print(f'Religious: {result[0][1]}')
print(f'Nature: {result[0][2]}')
print(f'Theatre: {result[0][3]}')
print(f'Shopping: {result[0][4]}')
print(f'Picnic: {result[0][5]}')
