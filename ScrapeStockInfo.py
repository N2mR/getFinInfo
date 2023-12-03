import time
from bs4 import BeautifulSoup
from selenium import webdriver

# DriverManager

class ScrapeStockInfo:
	def __init__(self):
		#掲示板投稿ランキング
		self.D_strRankingOfBoard = "https://finance.yahoo.co.jp/stocks/ranking/bbs?market=all&term=daily"
	
	def getStockInfo():
		print("getStockInfo")
	
	# 掲示板ランキングより銘柄リンクを取得
	def getStockLinksFromRankingOfBoard(self):
		self.getStockLinks(self.D_strRankingOfBoard)

	# 銘柄のリンクを取得
	def getStockLinks(self, url):

		# ドライバの取得
		driver = webdriver.Chrome()
		# リンクへアクセス
		driver.get(url)
		# 5秒待機でHTMLがJavaScriptにより形成されるまで待機
		time.sleep(5)
		# HTMLを取得
		page_source = driver.execute_script("return document.documentElement.outerHTML;")
		# パース
		soup = BeautifulSoup(page_source, 'html.parser')

		# 銘柄のリンクのみを取得
		stockLinks = []
		for a_tag in soup.find_all('a'):
			url = a_tag['href']
			if "quote" in url:
				stockLinks.append(url)			
		
		driver.quit()
		return stockLinks


ssi = ScrapeStockInfo()
ssi.getStockLinksFromRankingOfBoard()