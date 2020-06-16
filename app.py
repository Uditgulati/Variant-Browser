from flask import Flask, render_template, jsonify
import sql_query

app = Flask(__name__, static_url_path='/static')

@app.route('/source')
def get_data():
    limit = 10
    query_data = sql_query.fetch_data(limit)

    data = {
        "data": query_data
    }
    return jsonify(data)

@app.route('/') 
def index(): 
    return render_template('table.html')

if __name__ == '__main__':
    app.run(debug=False) 