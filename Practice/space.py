import requests

response=requests.get('http://api.open-notify.org/astros.json')
json = response.json()
print(json)

print('the people currently in place are: ')
for person in json['people']:
    print(person['name'])
