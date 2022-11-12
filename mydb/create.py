import sqlite3

DB_PATH = 'test.db'

conn = sqlite3.connect(DB_PATH)
# 创建表
# cur = conn.execute(f'CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)')

# 插入数据
data = [('aaa', 'bbb', 'ccc', "", "")]
for x in data:
	conn.execute('INSERT INTO stocks (date, trans, symbol, qty, price) VALUES (?, ?, ?, ?, ?)', x)

# # 查询方式一：获取表中所有列的数据
cur = conn.execute('SELECT * FROM stocks')
print(cur)
# # 查询方式二：获取表中某几列的数据
# cur = conn.execute('SELECT name,age FROM "table_name"')
# # 查询方式三：根据一个查询条件获取表中某几列的数据
# query = (10,)
# cur = conn.execute('SELECT name,age FROM "table_name" WHERE age > ?',query)
# # 查询方式三：根据多个查询条件获取表中某几列的数据
# query = (10,'张三')
# cur = conn.execute('SELECT name,age FROM "table_name" WHERE age > ? and name = ?',query)

# 获取查询到的数据
values = cur.fetchall()
print(values)
cur.close()
conn.close()
