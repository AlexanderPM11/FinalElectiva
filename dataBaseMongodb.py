from dataclasses import dataclass
from http import client
from pydoc import cli
from pymongo import MongoClient


class mongo():
    client = MongoClient(
        "mongodb+srv://electiva:electiva@cluster0.lyulc0c.mongodb.net/?retryWrites=true&w=majority")
    db = client.get_database("test")
    records = db.semafaro
    vadd = 23

    def countCollection(self):
        return (len(list(self.records.find())))

    def getCollection(self, id):
        loadData = list(self.records.find())
        listed = []
        listed.append(loadData[id]["Steps"])
        listed.append(loadData[id]["Metros"])
        listed.append(loadData[id]["Color"])
        listed.append(loadData[id]["IP"])
        return (listed)

    def insertCollection(self, color, Ip):
        new_s = {
            "Steps": 10,
            "Metros": "1",
            "Color": color,
            "IP": Ip
        }
        self.records.insert_one(new_s)
