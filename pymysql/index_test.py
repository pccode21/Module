import pymysql

def main():
    conn = pymysql.connect(
                            host='localhost',
                            port=3306,
                            database='db_test',
                            user='root',
                            password='admin',
                            charset='utf8'
                            )
    cursor = conn.cursor()
    for i in range(100000):
        cursor.execute("insert into index_test values('hao-%d')" % i)
    conn.commit()


if __name__ == '__main__':
    main()

"""
在mysql终端开启运行时间监测：set profiling=1;
查找第1万条数据ha-99999: select * from index_test where name='haha-99999';
查看执行的时间：show profiles;
为表index_test的name列创建索引：create index name_index on index_test(name(10));
"""
