import yfinance as yf, json, os, datetime
from newsapi import NewsApiClient

TICKER = "AAPL"                          # ★銘柄は自由に変更
today   = datetime.date.today().isoformat()

ticker  = yf.Ticker(TICKER)
info    = ticker.info
hist    = ticker.history(period="1mo").reset_index().tail(5).to_dict(orient="records")

newsapi = NewsApiClient(api_key=os.getenv("NEWSAPI_KEY", "NO_KEY"))
articles = newsapi.get_everything(q=TICKER, language="en",
                                  sort_by="publishedAt", page_size=3)["articles"]

payload = {
    "ticker": TICKER,
    "date": today,
    "price": info.get("regularMarketPrice"),
    "marketCap": info.get("marketCap"),
    "peRatio": info.get("trailingPE"),
    "history": hist,
    "news": articles
}

# 変換用の payload を書き出す部分
fn = f"data_{TICKER}_{today}.json"
with open(fn, "w") as f:
    json.dump(payload, f, indent=2, default=str)   # ← default=str を追加
print("saved →", fn)
