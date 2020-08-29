import pymysql


sql = "INSERT INTO maoyan_movie (name, category, release_time) " \
      "VALUES ({}, {}, {})"
print(sql)

try:
    cnn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        db='geekbang',
        password=''
    )
    print("到哪了")
except Exception as e:
    print("进这里了吗")
    print(e)
    raise e

cursor = cnn.cursor()
cursor.execute("SELECT * FROM maoyan_movie")
print(cursor.fetchall())
cnn.close()