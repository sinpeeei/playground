import requests, json

payload = {"title": "foo", "body": "bar", "userId": 1}

resp = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=payload
)

print(json.dumps(resp.json(), indent=2))
