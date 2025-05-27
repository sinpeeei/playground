import os, json, datetime, csv
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()                       # .env からキー読み込み
client = OpenAI()                   # env の OPENAI_API_KEY を自動検出

def summarise(json_path: str):
    with open(json_path) as f:
        data = f.read()

    prompt = f"""
あなたは日本語で書く株式アナリストです。
次の JSON を読み取り、重要ポイントを 80 字以内 × 5 行で要約し、
最後に投資判断を ★5 段階で示してください（例：★★★☆☆）。
JSON:
```json
{data}
```"""

    rsp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"system","content":"You are ChatGPT."},
                  {"role":"user","content":prompt}],
        temperature=0.3,
        max_tokens=400)
    return rsp.choices[0].message.content.strip()

def log(csv_path: str, date: str, ticker: str, summary: str):
    file_exists = os.path.exists(csv_path)
    with open(csv_path, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["date", "ticker", "summary_v1"])
        writer.writerow([date, ticker, summary])

if __name__ == "__main__":
    today  = datetime.date.today().isoformat()
    ticker = "AAPL"                                     # ★自由に変更可
    json_file = f"data_{ticker}_{today}.json"

    if not os.path.exists(json_file):
        raise FileNotFoundError(f"{json_file} がありません。先に fetch_fin_data.py を実行してください。")

    summary = summarise(json_file)
    log("prompt_log.csv", today, ticker, summary)
    print("要約生成＆CSV 追記完了。")
