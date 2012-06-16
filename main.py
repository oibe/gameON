from flask import Flask, request, Response
from pymongo import Connection
import json

app = Flask(__name__)

connection = Connection()
db = connection.test_database
post = {"author":"Mike","text":"Test"}

posts = db.posts
posts.insert(post)
print 'done'

@app.route("/api", methods=['POST', 'GET'])
def api_response():
    if request.method == 'POST':
        return request.json

if __name__ == '__main__':
    app.run('0.0.0.0', 8000)
