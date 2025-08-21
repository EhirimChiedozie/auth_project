import json
import requests

resp = requests.get('http://localhost:8000/todo/view_todo')
dates = [i['deadline_day'] for i in resp.json()]
print(dates)