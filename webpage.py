from flask import Flask, render_template, request, redirect, url_for
import sql_query

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('base.html')

@app.route('/store', methods=['POST', 'GET'])
def store():
    if request.method == 'POST':
        return redirect(url_for('buffer', buffer_input = request.form.get('submission_identifier')))
    
    elif request.method == 'GET':
        # cur.execute("SELECT v.vinyl_id, v.name, v.artist, array_agg(t.tag_name)\
        #             FROM vinyl v\
        #             LEFT JOIN vinyl_tag vt ON v.vinyl_id = vt.vinyl_id\
        #             LEFT JOIN tag t ON vt.tag_id = t.tag_id\
        #             GROUP BY v.vinyl_id ORDER BY vinyl_id\
        #             LIMIT 5 OFFSET 2;")
        return render_template('store.html', menu = sql_query.get_items(10, 0))

@app.route('/admin', methods=['POST', 'GET'])
def admin():
    if request.method == 'POST':
        return
    elif request.method == 'GET':
        return render_template('admin.html', genre = sql_query.get_genres())

@app.route('/buffer/<buffer_input>')
def buffer(buffer_input):
    return f"<h1>Passed value: {buffer_input} </h1>"

if __name__ == "__main__":
      app.run(debug=True)