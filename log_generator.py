from psycopg2.extensions import connection, cursor
from connector import connector
import random
from datetime import datetime, timedelta

conn: connection
cur: cursor

conn = connector()
cur = conn.cursor()

command = "SELECT * FROM books_information"
cur.execute(command)
books = cur.fetchall()
random.shuffle(books)

command = "SELECT * FROM members_information"
cur.execute(command)
members = cur.fetchall()
random.shuffle(members)

for _ in range(40):
    b = books.pop()
    m = members.pop()

    n = datetime.now()
    day = random.randint(7, 180)
    hour = random.randint(1, 3)
    minu = random.randint(1, 50)
    bt = n - timedelta(days=day, hours=hour, minutes=minu)
    bt_str = bt.strftime("%Y-%m-%d %H:%M:%S")

    kt = random.randint(10, 30)

    query = f"INSERT INTO log(book_id, member_id, operation_time, keep_time) VALUES " \
            f"({b[0]}, {m[0]}, '{bt_str}', '{kt} days')"
    cur.execute(query)

    if random.randint(0, 100) > 70:
        rt_d = random.randint(5, 40)
        rt = bt + timedelta(days=rt_d)
        rt_str = rt.strftime("%Y-%m-%d %H:%M:%S")

        query = f"INSERT INTO log(book_id, member_id, operation_time, keep_time) VALUES " \
                f"({b[0]}, {m[0]}, '{rt_str}', 'returned')"
        cur.execute(query)
    else:
        query = f"UPDATE books_information SET borrowed=true WHERE isbn={b[0]}"
        cur.execute(query)

    conn.commit()

