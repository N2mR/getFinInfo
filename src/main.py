from StockController import StockController
from MessageController import MessageController
from ScrapeStockData import ScrapeStockData
from StockInfo import StockInfo


def main():
    
    # 銘柄情報を取得
    sc = StockController()
    selectedStockInfoList = sc.getStockInfoList()

    # ラインで送信する
    mc = MessageController()
    msg = mc.notifyStockMessage(selectedStockInfoList)
    mc.sendMessage(msg)
    print(msg)

if __name__ == "__main__":
    main()