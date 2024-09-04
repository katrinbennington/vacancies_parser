import requests


query = {
    'text' : 'крановщик',
    'per_page' : 100,

}
response = requests.get('http://api.hh.ru/vacancies', params=query)

result = response.json()
pass
