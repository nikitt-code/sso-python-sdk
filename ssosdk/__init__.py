import json
import requests as rq

class SSOSDK:

    def __init__(self, token):
        self.host = "https://simulator.apiuser.ru/%method%/?author=niki_tt"
        self.token = token

    def get(self, method, data) :
        url = self.host.replace("%method%", method)
        payload = data
        headers = {'Content-Type': 'application/json'}
        response = rq.post(url, data=json.dumps(payload), headers=headers)
        return response

    def usersGet(self, user_ids) -> bytearray:
        userids = []
        for x in user_ids: userids.append(str(x))
        users = ",".join(userids)
        data = { "token": self.token, "user_ids": users }
        res = self.get("users.get", data)
        return res.json()

    def transfersCreate(self, to, count) -> bytearray:
        data = { "token": self.token, "peer_id":to, "count": count }
        res = self.get("transfers.create", data)
        return res.json()

    def transfersGetHistory(self, count) -> bytearray:
        data = { "token": self.token, "limit": count }
        res = self.get("transfers.getHistory", data)
        return res.json()

    def transfersGet(self, ids) -> bytearray:
        tids = []
        for x in ids: tids.append(str(x))
        transferids = ",".join(tids)
        data = {"token": self.token, "transfer_ids": transferids}
        res = self.get("transfers.get", data)
        return res.json()

    def webhooksGet(self) -> bytearray:
        data = { "token": self.token }
        res = self.get("webhooks.get", data)
        return res.json()

    def webhooksSet(self, url) -> bytearray:
        data = { "token": self.token, "url": url }
        res = self.get("webhooks.create", data)
        return res.json()

    def webhooksDelete(self) -> bytearray:
        data = { "token": self.token }
        res = self.get("webhooks.delete", data)
        return res.json()

    def promoCreate(self, count, activations) -> bytearray:
        data = { "token": self.token, "count": count, "activations": activations}
        res = self.get("promocodes.create", data)
        return res.json()

    def promoGet(self) -> bytearray:
        data = { "token": self.token }
        res = self.get("promocodes.get", data)
        return res.json()

    def promoActivate(self, code) -> bytearray:
        data = { "token": self.token, "code": code }
        res = self.get("promocodes.activate", data)
        return res.json()

