import json, csv, pathlib

# ----- ダミー JSON を用意（存在しなければ自動生成） -----
json_path = pathlib.Path('post_output.json')
if not json_path.exists():
    json_path.write_text(json.dumps({
        "title": "foo",
        "body": "bar",
        "userId": 1,
        "id": 101
    }, indent=2))

# ----- JSON → CSV 変換 -----
data = json.loads(json_path.read_text())
with open('post_output.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=data.keys())
    writer.writeheader()
    writer.writerow(data)

print('CSV書き出し完了:', 'post_output.csv')
