import psycopg2
import psycopg2.extras

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            dbname='cetenary_project',
                            user='postgres',
                            password='472112',
                            port=5432
    )
    return conn

def get_items(limit, offset):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(f"SELECT v.vinyl_id, v.name, v.artist, array_agg(t.tag_name) AS genre\
                    FROM vinyl v\
                    LEFT JOIN vinyl_tag vt ON v.vinyl_id = vt.vinyl_id\
                    LEFT JOIN tag t ON vt.tag_id = t.tag_id\
                    GROUP BY v.vinyl_id\
                    LIMIT {limit} OFFSET {offset};")
    # ans = cur.fetchall()
    output = []
    for row in cur.fetchall():
        output.append(dict(row))

    return output

def get_genres():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT tag_name from tag")
    output = cur.fetchall()
    return (output)

def get_album():

    return

print(get_genres())