from flask import Flask, request
from Game import Game
from druid import Druid
from warrior import Warrior
from hunter import Hunter
import json
import uuid

app = Flask(__name__)
game = Game()

@app.route('/game/players', methods=['POST'])
def add_player():
    content = request.json
    try:
        player = eval(content["class"])(content['name'],content['int'],content['str'],content['dex'])
        if len(game.get_all())==0:
            id = 1
        else:
            id = game.get_all()[-1].get_id()+1
        player.set_id(id)
        game.add(player)

        response = app.response_class(
            status=200,
            response="Character added to game\nCharacter ID is "+ str(len(game.get_all()))
        )
    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=400
        )
    return response

@app.route('/game/players/<int:player_id>', methods=['GET'])
def get_player(player_id):
    try:
        player = game.get(player_id)
        response = app.response_class(
            status=200,
            response=json.dumps(player.to_dict()),
            mimetype='application/json'
        )
        return response

    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=404
        )
        return response

@app.route('/game/players/<int:player_id>', methods=['DELETE'])
def del_player(player_id):
    try:
        game.delete(player_id)
        response = app.response_class(
            status=200,
        )
        return response
    except ValueError as e:
        response=app.response_class(
            status=400,
            response=str(e)
        )
        return response

@app.route('/game/players/<string:class_type>', methods=['GET'])
def get_class(class_type):
    players = []
    try:
        for player in game.get_all():
            if player.get_class() == class_type:
                players.append(player)

        if len(players) == 0:
            raise ValueError("No users exist in class "+str(class_type))

        response = app.response_class(
            status=200,
            response=str(players),
            mimetype='application/json'
        )
        return response

    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=400
        )
        return response

if __name__ == "main":
    app.run(debug=0)
