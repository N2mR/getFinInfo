import requests
import json

class MessageController:
    def notifyStockMessage(self, stockInfoList):
        respMsg = self.makeMessage(stockInfoList)
        return respMsg
    
    def makeMessage(self,stockInfoList):
        respMsg = ""
        for stockInfo in stockInfoList:
            try:
                # 名前
                stock_name = stockInfo["stock_name"]
                # 前日終値
                previous_close = stockInfo["previous_close"]
                # 一株配当
                dividend_yield = stockInfo["dividend_yield"]
                # PER
                per_ratio = stockInfo["per_ratio"]
                # PBR
                pbr_ratio= stockInfo["pbr_ratio"]
                # 信用倍率
                leverage_ratio = stockInfo["leverage_ratio"]
                # 信用買い残
                margin_buying = stockInfo["margin_buying"]
                # 信用売り残
                margin_selling = stockInfo["margin_selling"]
                # 銘柄リンク
                stock_link = stockInfo["stock_link"]

            except Exception as e:
                continue
        
            # メッセージ作成
            respMsg += "銘柄:       " + stock_name + "\n"
            respMsg += "前日終値:       " + previous_close + "\n"
            respMsg += "一株配当:       " + dividend_yield + "\n"
            respMsg += "PER:            " + per_ratio + "\n"
            respMsg += "PBR:            " + pbr_ratio + "\n"
            respMsg += "信用倍率:       " + leverage_ratio + "\n"
            respMsg += "信用買残:       " + margin_buying + "\n"
            respMsg += "信用売残:       " + margin_selling + "\n"
            respMsg += "URL:        " + stock_link + "\n"
            respMsg += "\n"
        return respMsg
    
    def sendMessage(self, msg):
        # 送信先のAPIキーを取得
        data = None
        with open('../config/config.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        API_keys = data['API_key']

        #要求先のURL
        api_url = 'https://notify-api.line.me/api/notify'

        # LineNotifyでは1000文字ずつでしか送信できないため分割する
        msgCount = len(msg) / 1000 + 1
        for i in range(int(msgCount)):
            fromIdx = i * 999
            toIdx = (i + 1) * 999
            dic_contents = {'message' : "\n" + msg[fromIdx:toIdx]}

            # 送信先数分テキストを送信する
            for API_key in API_keys:
                dic_TOKEN = {'Authorization' : 'Bearer' + ' ' + API_key}
                requests.post(api_url, headers=dic_TOKEN, data=dic_contents)