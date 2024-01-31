import requests

url_category = 'http://localhost:8000/api/category/'
url_course = 'http://localhost:8000/api/course/'
url_auth_jwt = 'http://localhost:8000/api/token/'

# JWT авторизация
data = {
    'username': 'teacher1',
    'password': '1'
}
res = requests.post(url_auth_jwt, data=data)
assert res.status_code==200, res.status_code
token = res.json()["access"]

# список категорий
headers = {
   'Authorization': f'Bearer {token}'
}
res = requests.get(url_category, headers=headers)
assert res.status_code==200, res.status_code
cat_id = res.json()['results'][0]['id'] # id первой категории в списке

res = requests.get(f'{url_category}{cat_id}/', headers=headers)
assert res.status_code==200, res.status_code

# список категорий
res = requests.get(url_course, headers=headers)
assert res.status_code==200, res.status_code