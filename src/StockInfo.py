# previous_close = "前日終値"
# open_price = "始値"
# high_price = "高値"
# low_price = "安値"
# volume = "出来高"
# turnover = "売買代金"
# price_limit = "値幅制限"
# market_cap = "時価総額"
# outstanding_shares = "発行済株式数"
# dividend_yield = "配当利回り"
# dividend_per_share = "1株配当"
# per_ratio = "PER"
# pbr_ratio = "PBR"
# eps = "EPS"
# bps = "BPS"
# minimum_purchase_amount = "最低購入代金"
# unit_shares = "単元株数"
# year_to_date_high = "年初来高値"
# year_to_date_low = "年初来安値"

# margin_buying = "信用買残"
# margin_buying_change_weekly = "前週比（信用買残）"
# margin_buying_ratio = "信用倍率"
# margin_selling = "信用売残"
# margin_selling_change_weekly = "前週比（信用売残）"

class StockInfo:
	# コンストラクタ
    def __init__(self):
        # 前日終値
        self.previous_close = ""
        # 始値
        self.open_price = ""
        # 高値
        self.high_price = ""
        # 安値
        self.low_price = ""
        # 出来高
        self.volume = ""
        # 売買代金
        self.turnover = ""
        # 値幅制限
        self.price_limit = ""
        # 時価総額
        self.market_cap = ""
        # 発行済株式数
        self.outstanding_shares = ""
        # 配当利回り
        self.dividend_yield = ""
        # 1株配当
        self.dividend_per_share = ""
        # PER
        self.per_ratio = ""
        # PBR
        self.pbr_ratio = ""
        # EPS
        self.eps = ""
        # BPS
        self.bps = ""
        # 最低購入代金
        self.minimum_purchase_amount = ""
        # 単元株数
        self.unit_shares = ""
        # 年初来高値
        self.year_to_date_high = ""
        # 年初来安値
        self.year_to_date_low = ""
        # 信用買残
        self.margin_buying = ""
        # 前週比（信用買残）
        self.margin_buying_change_weekly = ""
        # 信用売残
        self.margin_selling = ""
        # 前週比（信用売残）
        self.margin_selling_change_weekly = ""
    
    def makeStockInfoObj(stockData):
        print()

