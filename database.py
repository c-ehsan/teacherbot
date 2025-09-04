import sqlite3 
DB_path="data/teacherbot.db"
def init_db():
    conn=sqlite3.connect(DB_path)
    cursor=conn.cursor()
    # جدول کاربران 
    cursor.execute("""create table if not exists users(
                   id integer primary key autoincrement,
                   telegram_id integer unique,
                   first_name text,
                   score integer default 0)""")
    # جدول سوالات ازمون 
    cursor.execute("""create table if not exists questions(
                   id integer primary key autoincrement,
                   question text,
                   answer text)""")
    conn.commit()
    conn.close()
