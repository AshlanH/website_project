from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import psycopg2.extras
import sql_query

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            dbname='cetenary_project',
                            user='postgres',
                            password='472112',
                            port=5432
    )
    return conn

print(sql_query.get_items(5, 1))

# def get_sql(limit, offset):
#     conn = get_db_connection()
#     cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#     cur.execute(f"SELECT v.vinyl_id, v.name, v.artist, array_agg(t.tag_name)\
#                     FROM vinyl v\
#                     LEFT JOIN vinyl_tag vt ON v.vinyl_id = vt.vinyl_id\
#                     LEFT JOIN tag t ON vt.tag_id = t.tag_id\
#                     GROUP BY v.vinyl_id\
#                     LIMIT {limit} OFFSET {offset};")
#     # ans = cur.fetchall()
#     output = []
#     for row in cur.fetchall():
#         output.append(dict(row))

#     return output


# @app.route('/')
# def home():
#     return render_template('test_page.html', push_album = sample_dict)
#     # return render_template('test_page.html')

# if __name__ == "__main__":
#       app.run(debug=True)