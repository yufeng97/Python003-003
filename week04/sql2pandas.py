import pandas as pd
import pymysql


conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='',
    db='geekbang',
)

sql = 'SELECT * FROM data'

# SELECT * FROM data;
df = pd.read_sql(sql, conn)

# SELECT * FROM data LIMIT 10;
df.head(10)
   

# SELECT id FROM data;  //id 是 data 表的特定一列
df['id']
   

# SELECT COUNT(id) FROM data;
df['id'].count()
   

# SELECT * FROM data WHERE id<1000 AND age>30;
df[(df['id'] < 1000) & (df['age'] > 30)]
   


sql1 = 'SELECT * FROM table1;'
sql2 = 'SELECT * FROM table2;'
df1 = pd.read_sql(sql1, conn)
df2 = pd.read_sql(sql2, conn)
# SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
df1.groupby('id')['order_id'].nunique()

# SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
# merge default using inner join
pd.merge(df1, df2, on='id',) 
   

# SELECT * FROM table1 UNION SELECT * FROM table2;
# remove duplicate
pd.concat([df1, df2], axis='index').drop_duplicates()
   

# DELETE FROM table1 WHERE id=10;
# two kinds of approach
# df1 = df1[df1['id'] != 10]
df1.drop(df1[df1['id'] == 10].index)
   

# ALTER TABLE table1 DROP COLUMN column_name;
df1.drop(['column_name'], axis='column')
