from flask import Flask
from pymongo import Connection
import json

app = Flask(__name__)
app.config.from_object(__name__)

#Creates a connection
connection = Connection()
db = connection.test_database
post = {"author":"Mike","text":"Test"}

posts = db.posts
posts.insert(post)
print 'done'


payload {'key1':'value1','key2':'value2'}
r = requests.get(url,params=payload)

