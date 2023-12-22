from collections import OrderedDict
class StockInfo:
    # 銘柄情報を辞書型で返す
    def makeStockInfo(self, stockDataList):
        # 銘柄情報
        stockInfo = {
            "stock_name": "",
            "stock_link": "",
            "previous_close": "",
            "open_price": "",
            "high_price": "",
            "low_price": "",
            "volume": "",
            "turnover": "",
            "price_limit": "",
            "market_cap": "",
            "outstanding_shares": "",
            "dividend_yield": "",
            "dividend_per_share": "",
            "per_ratio": "",
            "pbr_ratio": "",
            "eps": "",
            "bps": "",
            "minimum_purchase_amount": "",
            "unit_shares": "",
            "year_to_date_high": "",
            "year_to_date_low": "",
            "margin_buying": "",
            "margin_buying_change_weekly": "",
            "leverage_ratio": "",
            "margin_selling": "",
            "margin_selling_change_weekly": ""
        }
        
        # 要素の数が一致していれば、stockInfoにデータを詰める
        if(len(stockDataList) == len(stockInfo)):
            stockInfo = OrderedDict(stockInfo)
            num = 0
            # イテレート中に値を変更すると例外が発生するためコピーを使用
            for k, v in stockInfo.copy().items():
                stockInfo[k] = stockDataList[num]
                # インクリメント
                num = num + 1
                # 配列のレンジを超えた場合にはbreak
                if num >= len(stockInfo):
                    break
            
            stockInfo = dict(stockInfo)
        else:
            # 作成に失敗した場合は空の辞書型を返す
            stockInfo = {}
        
        return stockInfo

    # 銘柄情報(辞書型)を配列に詰めて返す
    def makeStockInfoList(self, stockDataList):
        stockInfoList = []
        for stockData in stockDataList:
            stockInfo = self.makeStockInfo(stockData)
            # 正常に銘柄情報が取得できた場合はstockInfoListに詰める
            if not stockInfo == {}:
                stockInfoList.append(stockInfo)

        return stockInfoList

