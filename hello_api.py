#
python<br>import requests, json<br>resp = requests.get('https://jsonplaceholder.typicode.com/todos/1')<br>print(json.dumps(resp.json(), indent=2))<br>


