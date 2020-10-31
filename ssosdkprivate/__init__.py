import requests as rq
from urllib.parse import parse_qs

class SSOSDKPRIVATE:

    host = "http://simulator.it-hube.site/api/"

    def __init__(self, url):
        self.url = url
        qsparsed = parse_qs(self.url)
        self.vkid_ = qsparsed["vk_user_id"][0]
        self.profile = rq.get(self.host+"auth/?user="+str(self.vkid_)+"&params="+self.url).json()
        self.token = self.profile["data"]["token"]

    def buyAds(self, type) -> bytearray:
        method_name = "buyAds"
        if type == 0:
            ads_ = self.profile["data"]["ads_0"]
        elif type == 1:
            ads_ = self.profile["data"]["ads_1"]
        res = rq.get(self.host+method_name+"/?user="+str(self.vkid_)+"&count="+str(ads_)+"&type="+str(type)+"&params="+self.url).json()
        return [ res["status"], res["message"] ]

    def changePrice(self, to) -> bytearray:
        method_name = ""
        if to == 0:
            method_name = "toRaise"
        elif to == 1:
            method_name = "toDowngrade"
        res = rq.get(self.host+method_name+"/?user="+str(self.vkid_)+"&params="+self.url).json()
        return res

    def getMarket(self, type) -> bytearray:
        method_name: str = "getUpgrades"
        if type == 0:
            method_name += "One"  # opt
        elif type == 1:
            method_name += "Two"  # radio
        res = rq.get(self.host+method_name+"/?user="+str(self.vkid_)+"&params="+self.url).json()
        return res

    def buyItem(self, type, shop_id) -> bytearray:
        method_name: str = "buyUpgrades"
        items = [  # shop_id
            "2G (E)",  # 0
            "3G",  # 1
            "LTE (4G)",  # 2
            "LTE Advanced (4G PLUS)",  # 3
            "5G"  # 4
        ]
        if type == 0 or type == 1:  # 0 - opt # 1 - radio
            if shop_id >= 0 and shop_id <= 4:
                buy_item: str = items[shop_id].replace(" ", "%20")
                result: bytearray = rq.get(self.host + method_name + "/?user=" + str(self.vkid_) + "&type=" + str(type) + "&up_name=" + buy_item + "&params=" + self.url).json()
                return result