from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = 'food.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    conn = get_db_connection()
    
    # Create the SQL statement with full-text search
    sql = """
    SELECT
        Category,
        Description,
        Data_Kilocalories,
        Data_Protein,
        Data_Carbohydrate,
        Data_Household_Weights_2nd_Household_Weight,
        Data_Household_Weights_2nd_Household_Weight_Description
    FROM food_data
    WHERE Category LIKE ? OR Description LIKE ?
    """
    
    # Execute the query with parameters to prevent SQL injection
    cursor = conn.execute(sql, (f'%{query}%', f'%{query}%'))
    rows = cursor.fetchall()
    conn.close()
    
    # Convert rows to a list of dictionaries
    results = [dict(row) for row in rows]
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
