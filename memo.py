import sqlite3
from contextlib import closing

dbname = 'database.db'


with closing(sqlite3.connect(dbname)) as conn:
    c = conn.cursor()

        # executeメソッドでSQL文を実行する
    create_table = '''create table memo (id int, user varchar(64),memonaiyou varchar(64),makeTime int)'''
    c.execute(create_table)


def createdata(self, user, memonaiyou, makeTime):
        # SQL文に値をセットする場合は，Pythonのformatメソッドなどは使わずに，
        # セットしたい場所に?を記述し，executeメソッドの第2引数に?に当てはめる値を
        # タプルで渡す．
    sql = 'insert into memo (id, self.user, self.memonaiyou, self.makeTime) values (?,?,?,?,?)'
    memo = (user, memonaiyou, makeTime)
    c.execute(sql, memo)

    select_sql = 'select * from memo'
    for row in c.execute(select_sql):
        print(row)

        # 一度に複数のSQL文を実行したいときは，タプルのリストを作成した上で
        # executemanyメソッドを実行する
        # insert_sql = 'insert into memos (id, name, age, gender) values (?,?,?,?)'
        # memos = [
        #     (2, 'Shota', 54, 'male'),
        #     (3, 'Nana', 40, 'female'),
        #     (4, 'Tooru', 78, 'male'),
        #     (5, 'Saki', 31, 'female')
        # ]
        # c.executemany(insert_sql, memos)
        # conn.commit()
#def updatedata(self,user,memonaiyou, makeTime):

def inquirydata(self,user,memonaiyou, makeTime):
    c.execute( "select * from dbname")
    for row in c:
        print(str(row[0])+','+row[1])
    c.close()

#def deliteedata(self,user,memonaiyou, makeTime):
