import json
import requests as rq

class SSOSDK:

    def __init__(self, token):
        self.host = "https://simulator.apiuser.ru/%method%/?author=niki_tt"
        self.token = token

    def get(self, method, data):
        url = self.host.replace("%method%", method)
        payload = data
        headers = {'Content-Type': 'application/json'}
        response = rq.post(url, data=json.dumps(payload), headers=headers)
        return response

    def usersGet(self, user_ids):
        userids = []
        for x in user_ids: userids.append(str(x))
        users = ",".join(userids)
        data = { "token": self.token, "user_ids": users }
        res = self.get("users.get", data)
        return res.json()

    def transfersCreate(self, to, count):
        data = { "token": self.token, "peer_id":to, "count": count }
        res = self.get("transfers.create", data)
        return res.json()

    def transfersGet(self, count):
        data = { "token": self.token, "limit": count }
        res = self.get("transfers.getHistory", data)
        return res.json()

    def webhooksCreate(self, url):
        data = { "token": self.token, "url": url }
        res = self.get("webhooks.create", data)
        return res.json()
