import mysql.connector as mysql

db_test = mysql.connect(
    host="localhost",
    user="root",
    passwd="123098555777q",
    database="test_db"
)

cursor = db_test.cursor()
# cursor.execute("DROP TABLE hw_salesman") # удаление таблицы
# cursor.execute("""CREATE TABLE hw_salesman (ord_no INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
#               purch_amt FLOAT(11), ord_date DATE, customer_id INT(11), salesman_id INT(11))""")

# cursor.execute("DESC hw_salesman")
# print(cursor.fetchall())
# query = "INSERT INTO hw_salesman (purch_amt, ord_date, customer_id, salesman_id) VALUES (%s, %s, %s, %s)"
# values = [
#     (150.5, "2012-10-05", 3005, 5002),
#     (270.65, "2012-09-10", 3001, 5005),
#     (65.26, "2012-10-05", 3002, 5001),
#     (110.5, "2012-08-17", 3009, 5003),
#     (948.5, "2012-09-10", 3005, 5002),
#     (2400.6, "2012-07-27", 3007, 5001),
#     (5760, "2012-09-10", 3002, 5001),
#     (1983.43, "2012-10-10", 3004, 5006),
#     (2480.4, "2012-10-10", 3009, 5003),
#     (250.45, "2012-06-27", 3008, 5002),
#     (75.29, "2012-08-17", 3003, 5007),
#     (3045.6, "2012-04-25", 3002, 5001)
# ]
#
# cursor.executemany(query, values)
# db_test.commit()

# cursor.execute("SELECT * FROM hw_salesman")
# print(cursor.fetchall())

query = "SELECT ord_no,ord_date,purch_amt FROM hw_salesman WHERE salesman_id = 5002"  # продавец 502
cursor.execute(query)
print(cursor.fetchall())

query = "SELECT DISTINCT salesman_id FROM hw_salesman"  # уникальные значения
cursor.execute(query)
print(cursor.fetchall())

query = "SELECT * FROM hw_salesman ORDER BY ord_date ASC"  # cортировка по дате по порядку возрастания
cursor.execute(query)
print(cursor.fetchall())

query = "SELECT * FROM hw_salesman ORDER BY salesman_id DESC"  # сортировка по ID продавца по порядку убывания
cursor.execute(query)
print(cursor.fetchall())

query = "SELECT * FROM hw_salesman WHERE ord_no>0 ORDER BY ord_no"  # сортировка по номеру заказа
cursor.execute(query)
print(cursor.fetchall())

query = "SELECT * FROM hw_salesman ORDER BY purch_amt"  # сортировка по количеству
cursor.execute(query)
print(cursor.fetchall())

query = "SELECT * FROM hw_salesman WHERE ord_no BETWEEN 2 AND 6"  # заказы между 1 и 7
cursor.execute(query)
print(cursor.fetchall())


db_test.close()
