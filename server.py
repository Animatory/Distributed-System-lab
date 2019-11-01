import pymongo
from flask import Flask, request, render_template

app = Flask(__name__)
# db_client = pymongo.MongoClient('mongodb://18.188.95.229:27017')
db_client = pymongo.MongoClient('mongodb://18.191.232.104:27017')

db = db_client['chat']


def get_messages():
    collection = db['messages']
    messages = collection.find({}, {'_id': 0})
    return messages


@app.route('/')
def main_page():
    return render_template('index.html', messages=get_messages())


@app.route('/', methods=['POST'])
def get_form():
    message = request.form['Message']
    author = request.form['Author']

    collection = db['messages']
    collection.insert_one({'author': author, 'message': message})

    return render_template('index.html', messages=get_messages())


if __name__ == '__main__':
    app.run()
