### week04 Homework

#### 提示

**每一题有两个代码块，第一个未SQL语句，第二个为pandas语句**

#### 预设python代码(1)

```python
import pandas as pd
import pymysql


conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='',
    db='geekbang',
)

sql = 'SELECT * FROM data;'
df = pd.read_sql(sql, conn)
```

##### 1. 

```sql
SELECT * FROM data;
```

```python
df = pd.read_sql(sql, conn)
df
```

##### 2. 

```sql
SELECT * FROM data LIMIT 10;
```

```python
df.head(10)
```

##### 3.  

```sql
SELECT id FROM data;  --//id 是 data 表的特定一列
```

```python
df['id']
```

##### 4. 

```sql
SELECT COUNT(id) FROM data;
```

```
df['id'].count()
```

##### 5.

```sql
SELECT * FROM data WHERE id<1000 AND age>30;
```

```python
df[(df['id'] < 1000) & (df['age'] > 30)]
```

#### 预设python代码(2)

```python
sql1 = 'SELECT * FROM table1;'
sql2 = 'SELECT * FROM table2;'
df1 = pd.read_sql(sql1, conn)
df2 = pd.read_sql(sql2, conn)
```

##### 6. 

```sql
SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
```

```python
df1.groupby('id')['order_id'].nunique()
```

##### 7. 

```sql
SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
```

```python
# merge default using inner join
pd.merge(df1, df2, on='id',)
```

##### 8. 

```sql
SELECT * FROM table1 UNION SELECT * FROM table2;
```

```python
pd.concat([df1, df2], axis='index').drop_duplicates()
```

##### 9.

```sql
DELETE FROM table1 WHERE id=10;
```

```python
# two kinds of approach
# df1 = df1[df1['id'] != 10]
df1.drop(df1[df1['id'] == 10].index)
```

##### 10. 

```sql
ALTER TABLE table1 DROP COLUMN column_name;
```

```python
df1.drop(['column_name'], axis='column')
```

