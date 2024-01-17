import requests

url = 'https://test.it-kyzyl.ru/api/category/'

res = requests.get(url)
#print(res.json())
assert res.status_code == 200

res = requests.options(url)
#print(res.json())
assert res.status_code == 200

data = {
    'name': 'Новая категория курсов'
}
res = requests.post(url, data=data)
#print(res.status_code, res.json())
id = res.json()['id']
assert res.status_code == 201

#id=5

res = requests.delete(f'{url}/{id}')
assert res.status_code == 204