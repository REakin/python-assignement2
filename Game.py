import json
from druid import Druid
from warrior import Warrior
from hunter import Hunter


class Game():

    def __init__(self):
        self.players = self.read_file()

    def add(self,player):
        """adds a character to the list of players"""
        self.players.append(player)
        self.write_to_file(self.players)

    def get(self,id):
        """gets a individual character by id"""
        for player in self.players:
            if player.get_id() == id:
                return player

    def get_all(self):
        """returns all the characters in the list of players"""
        return self.players

    def get_all_by_type(self,type):
        """returns a list of characters identified by their class"""
        match = []
        for player in self.players:
            if player.get_class() == type:
                match.append(player)
        return match

    def update(self,new_player):
        """updates a user by replacing them in the array of users if the ID's match between characters"""
        replace = False
        for player in self.players:
            if player.get_id() == new_player.get_id():
                self.players[self.players.index(player)] = new_player
                replace = True
                self.write_to_file(self.players)
        if replace is False:
            raise LookupError('Player ID not found')

    def delete(self,id):
        """deletes a character by id"""
        for player in self.players:
            if player.get_id() == id:
                self.players.remove(player)
                self.write_to_file(self.players)

    @staticmethod
    def write_to_file(data):
            with open('datafile.json','w') as file:
                writing = []
                for char in data:
                    writing.append(char.to_dict())
                json.dump(writing, file,indent=4)



    @staticmethod
    def read_file():
        try:
            with open('datafile.json','r') as file:
                data=json.load(file)
                players=[]
                for player in data:
                    char = eval(player["Class"])(player['Name'],player['Intelligence'],player['Strength'],player['Dexterity'])
                    char.set_id(player['id'])
                    players.append(char)
                return players
        except:
            with open('datafile.json','w') as file:
                file.write('[]')
                return json.load(file)