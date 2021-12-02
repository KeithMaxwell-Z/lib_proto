from connector import connector
from generator import generator

if __name__ == '__main__':
    # con: psycopg2._psycopg.connection
    # cur: psycopg2._psycopg.cursor
    con = connector()
    gen = generator()
    cur = con.cursor()
    for i in range(0, 100):
        res = gen.fetch_one()
        query = f"INSERT INTO members_information(member_first_name, member_last_name, dob, address, rank) " \
                f"VALUES ('{res[0]}', '{res[1]}', '{res[2]}', '{res[3]}', {res[4]})"
        cur.execute(query=query)
    con.commit()
