import pandas as pd
import numpy as np

df = pd.DataFrame({
    'key1': ['a', 'a', 'b', 'b', 'a', 'c', 'a', 'd', 'd', 'a'],
    'key2': ['one', 'two', 'one', 'two', 'three', 'one', 'three', 'three', 'one', 'two'],
    'data1': np.random.randn(10),
    'data2': np.random.randn(10),
})


# SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
grouped = df.groupby(['key1'])['key2'].nunique()

print(grouped)
# print(grouped.count())

