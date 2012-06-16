from flask import Flask, request, Response
from pymongo import Connection
import json

app = Flask(__name__)

connection = Connection()
db = connection.gameon

@app.route("/api", methods=['POST', 'GET'])
def api_response():
    if request.method == 'POST':
        return request.form['param_one'] + ' ' + request.form['param_two']
    else:
        return 'test'

@app.route("/game/details")
def game_details():
    pass

@app.route('/user/create', methods=['GET','POST'])
def create_user():
    if request.method == 'POST':
        user = {
            'fbid': request.form['id'],
            'name': request.form['name'],
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'fblink': request.form['link'],
            'gender': request.form['gender']
        }
        db.users.insert(user)
        return 'Saved to MongoDB'
    else:
        return 'GET REQUEST, USE POST INSTEAD'


@app.route("/game/create", methods=['POST'])
def create_game():
    if request.method == 'POST':
        game = {
            'sport': request.form['sport'],
            'latitude': request.form['lat'],
            'longitude': request.form['lon'],
            'timestamp': request.form['timestamp'],
            'number_of_players': request.form['numplayers'],
            'creator': {
                'name': request.form['name'],
                'fbid': request.form['fbid']
            }
        }
        db.games.insert(game)


@app.route("/games/list")
def list_games():
    # sorted by closest long/lat coordinates, then by date/time
    return db.gameon.games.find("loc": )

@app.route("/game/join")
def join_game():
    pass

@app.route("/<user>/games")
def display_user_games():
    pass



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
