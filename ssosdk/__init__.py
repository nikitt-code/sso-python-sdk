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

    """
    USERS     |
              |
              V
    """

    # users.get
    def usersGet(self, user_ids):
        userids = []
        for x in user_ids: userids.append(str(x))
        users = ",".join(userids)
        data = { "token": self.token, "user_ids": users }
        res = self.get("users.get", data)
        return res.json()

    """
    TRANSFERS |
              |
              V
    """

    # transfers.create
    def transfersCreate(self, to, count):
        data = { "token": self.token, "peer_id":to, "count": count }
        res = self.get("transfers.create", data)
        return res.json()

    # transfers.getHistory
    def transfersGetHistory(self, count):
        data = { "token": self.token, "limit": count }
        res = self.get("transfers.getHistory", data)
        return res.json()

    # transfers.get
    def transfersGet(self, ids):
        tids = []
        for x in ids: tids.append(str(x))
        transferids = ",".join(tids)
        data = {"token": self.token, "transfer_ids": transferids}
        res = self.get("transfers.get", data)
        return res.json()

    """
    WEBHOOKS  |
              |
              V
    """

    def webhooksGet(self):
        data = { "token": self.token }
        res = self.get("webhooks.get", data)
        return res.json()

    def webhooksSet(self, url):
        data = { "token": self.token, "url": url }
        res = self.get("webhooks.create", data)
        return res.json()

    def webhooksDelete(self):
        data = { "token": self.token }
        res = self.get("webhooks.delete", data)
        return res.json()