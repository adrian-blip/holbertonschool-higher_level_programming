#!/usr/bin/python3

"""ConsultMysqldb"""

if __name__ == '__main__':
    """main"""

    import MySQLdb
    import sys

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states
                WHERE name LIKE 'N%' ORDER BY states.id ASC;""")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
