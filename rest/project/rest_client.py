import requests


api_server_addr = 'server'
api_server_port = '8000'

api_url = f'http://{api_server_addr}:{api_server_port}'
response = requests.get(api_url)
print(response.status_code)

#GET
base = 3
expoente  = 5
service_url = f'{api_url}/pow/{base}/{expoente}'
response = requests.get(service_url)
print(f'Response: {response.status_code}')
print(response.json())

#POST
query = {'base': 5, 'expoente': 3}

service_url = f'{api_url}/pow'
response = requests.post(service_url, json=query)
print(f'Response: {response.status_code}')
print(response.json())

