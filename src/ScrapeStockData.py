import time
from bs4 import BeautifulSoup
from selenium import webdriver
import random

class ScrapeStockData:
	# コンストラクタ
	def __init__(self):
		# 掲示板投稿ランキング
		self.D_strRankingOfBoard = "https://finance.yahoo.co.jp/stocks/ranking/up?market=all&term=daily&page="
		# 偏った銘柄取得の防止策として暫定でランダム値を使用する
		page_num = random.randint(1, 10)
		self.D_strRankingOfBoard += str(page_num)

		# ドライバの取得
		self.driver = webdriver.Chrome()
	
	# デストラクタ
	def __exit__(self):
		# ドライバインスタンスの開放
		self.driver.quit()
	
	# 掲示板ランキングより銘柄リンクを取得
	def getStockLinksFromRankingOfBoard(self):
		return self.getStockLinks(self.D_strRankingOfBoard)

	# 銘柄のリンクを取得
	def getStockLinks(self, url):
		# リンクへアクセス
		self.driver.get(url)
		# 5秒待機でHTMLがJavaScriptにより形成されるまで待機
		time.sleep(5)
		# HTMLを取得
		page_source = self.driver.execute_script("return document.documentElement.outerHTML;")
		# パース
		soup = BeautifulSoup(page_source, 'html.parser')

		# 銘柄のリンクのみを取得
		stockLinks = []
		for a_tag in soup.find_all('a'):
			url = a_tag['href']
			if "quote" in url:
				stockLinks.append(url)			
		return stockLinks

	def getStockData(self, stockLink):
		# リンクへアクセス
		self.driver.get(stockLink)
		time.sleep(5)
		# HTMLを取得
		page_source = self.driver.execute_script("return document.documentElement.outerHTML;")
		# パース
		soup = BeautifulSoup(page_source, 'html.parser')


		# 銘柄名を取得
		stockName_CSS_SELECTOR = "_2BzIEkFN"
		stockElement = soup.select_one('.' + stockName_CSS_SELECTOR)
		stockName = stockElement.get_text(strip=True)

		# 銘柄の基本情報取得
			# いずれスクレイピング対策でクラス名が変わったとしても対応できるように
			# 外部ファイルで管理したい
		# 下記情報が配列で取得できる
			# ( 前日終値, 始値, 高値, 安値, 出来高, 売買代金, 値幅制限, 時価総額, 発行済株式数, 配当利回り, 
			# 1株配当, PER, PBR, EPS, BPS, 最低購入代金, 単元株数, 年初来高値, 年初来安値 )
		stockData_CSS_SELECTOR = 'span._11kV6f2G'
		stockData = [] # <- 最終的には構造体に詰めてStockControllerに返す
		for element in soup.select(stockData_CSS_SELECTOR):
			text = element.get_text(strip=True)
			stockData.append(text)

		# 銘柄の信用取引情報
			# いずれスクレイピング対策でクラス名が変わったとしても対応できるように
			# 外部ファイルで管理したい
		# 下記情報が配列で取得できる
			# 信用買残, 前週比, 信用倍率, 信用売残, 前週比
		liList = soup.select('ul._3BSKtx-a > li')
		creditData = [] # <- 最終的には構造体に詰めてStockControllerに返す
		for li in liList:
			dd = li.select_one('dl > dd')
			span = dd.select_one('span')
			span2 = span.select('span')
			text = span2[1].get_text()
			creditData.append(text)
		
		result = [stockName, stockLink] + stockData + creditData

		return result

	# 銘柄情報を取得しStockDataのリストを返す
	def getStockDataList(self, stockLinks):
		stockDataList = []
		for stockLink in stockLinks:
			# 銘柄リンクでない場合は処理しない(銘柄リンクには"quote"の文字列が含まれている)
			if not "quote" in stockLink:
				continue
			else:
				try:
					stockData = self.getStockData(stockLink)
					stockDataList.append(stockData)
				except Exception:
					# 例外が発生した場合は次の処理に移行
					continue

		return stockDataList