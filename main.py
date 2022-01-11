import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
from collections import Counter
		
@app.route('/get/<string:name>', methods=['GET'])
def getsearch(name):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        select_stmt = "SELECT PaperReferenceId FROM authors INNER JOIN paperauthoraffiliations ON authors.AuthorId = paperauthoraffiliations.AuthorId INNER JOIN paperreferences ON paperauthoraffiliations.paperId = paperreferences.paperId WHERE NormalizedName LIKE '%%%s%%';" % name
        cursor.execute(select_stmt)
        empRows = cursor.fetchall()
        response = jsonify(empRows)
        if len(empRows) == 0:
            response.status_code = 404
            return response

        referencedpapers = [item["PaperReferenceId"] for item in empRows]
        c = Counter(referencedpapers)
        c.most_common()
        print ("",c.most_common())
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
    conn.close()
		
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
		
if __name__ == "__main__":
    app.run()