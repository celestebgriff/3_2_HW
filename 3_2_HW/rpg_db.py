
import sqlite3

sqlite_file = '/Users/celes/Downloads/rpg_db.sqlite3'
conn = sqlite3.connect(sqlite_file)
curs = conn.cursor()
query1 = """
SELECT count(*)
FROM charactercreator_character
"""
result1 = curs.execute(query1).fetchall()
print('How many total Characters are there?')
print(result1)



query2 = """
SELECT
    COUNT(DISTINCT charactercreator_mage.character_ptr_id) AS MageCount,
    COUNT(DISTINCT charactercreator_thief.character_ptr_id) AS ThiefCount,
    COUNT(DISTINCT charactercreator_cleric.character_ptr_id) AS ClericCount,
    COUNT(DISTINCT charactercreator_fighter.character_ptr_id) AS FighterCount
FROM
    charactercreator_mage,
    charactercreator_thief,
    charactercreator_cleric,
    charactercreator_fighter
"""
result2 = curs.execute(query2).fetchall()
print('How many of each specific subclass?')
print(result2)



query3 = """
SELECT count(*)
FROM armory_item
"""
result3 = curs.execute(query3).fetchall()
print('How many total Items?')
print(result3)



query4 = """
SELECT 
	count(DISTINCT item_ptr_id) as weapons,
	count(DISTINCT item_id) - count(DISTINCT item_ptr_id) as non_weapon
FROM armory_item
LEFT JOIN armory_weapon ON armory_item.item_id = armory_weapon.item_ptr_id
"""
result4 = curs.execute(query4).fetchall()
print('How many of the Items are weapons? How many are not?')
print(result4)



query5 = """
SELECT count(item_id) as count 
FROM charactercreator_character_inventory as cci 
GROUP BY character_id
LIMIT 20
"""
result5 = curs.execute(query5).fetchall()
print('How many Items does each character have? (Return first 20 rows)')
print(result5)



query6 = """
SELECT count(item_ptr_id) 
FROM armory_weapon as aw, armory_item as ai, charactercreator_character_inventory as ci 
WHERE ai.item_id = ci.item_id AND ai.item_id = aw.item_ptr_id group by character_id 
LIMIT 20;
"""
result6 = curs.execute(query6).fetchall()
print('How many Weapons does each character have? (Return first 20 rows)')
print(result6)



query7 = """
SELECT avg(count) 
FROM (SELECT count(item_id) as count 
FROM charactercreator_character_inventory as cci 
GROUP BY character_id)
"""
result7 = curs.execute(query7).fetchall()
print('On average, how many Items does each Character have?')
print(result7)



query8 = """
SELECT avg(count) 
FROM (SELECT count(item_ptr_id) as count 
FROM armory_weapon as aw, armory_item as ai, charactercreator_character_inventory as ci 
WHERE ai.item_id = ci.item_id AND ai.item_id = aw.item_ptr_id 
GROUP BY character_id)
"""
result8 = curs.execute(query8).fetchall()
print('On average, how many Weapons does each character have?')
print(result8)
