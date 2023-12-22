from StockInfo import StockInfo
from ScrapeStockData import ScrapeStockData

class StockController:
    def __init__(self):
        self.D_PBR = 2
        self.D_PER = 10
    
    # 銘柄取得
    def getStockInfoList(self):
        # 銘柄情報をスクレイピング
        ssd = ScrapeStockData()
        stockLinks = ssd.getStockLinksFromRankingOfBoard()
        stockDataList = ssd.getStockDataList(stockLinks)
        # スクレイピングしたデータを整形
        si = StockInfo()
        stockInfoList = si.makeStockInfoList(stockDataList)
        # 整形したデータを選定
        selectedStockInfoList = []
        selectedStockInfoList = self.selectStockList(stockInfoList)
        return selectedStockInfoList

    # stockInfoListから銘柄を選定
    def selectStockList(self, stockInfoList):
        result = []
        # ループ内の条件により銘柄を選定
        for obj in stockInfoList:
            # 選定に使用するデータがIntに変換できるかチェック
            if not self.isCalcable(obj["pbr_ratio"]) or not self.isCalcable(obj["per_ratio"]):
                continue
            # PBRが定数の値より大きい場合はスキップ
            pbr_ratio = float(obj["pbr_ratio"])
            if not self.LT(pbr_ratio, self.D_PBR):
                continue
            # PERが定数の値より大きい場合はスキップ
            per_ratio = float(obj["per_ratio"])
            if not self.LT(per_ratio, self.D_PER):
                continue
            result.append(obj)
        
        return result

    # AがBより小さいか判定
    def LT(self, A, B):
        blResult = False
        try:
            blResult = A <= B
        except Exception as e:
            blResult = False
        
        return blResult
    
    # 受け取った値がint型に変換可能かチェック
    def isCalcable(self, data):
        try:
            float(data)
            return True
        except ValueError:
            return False
