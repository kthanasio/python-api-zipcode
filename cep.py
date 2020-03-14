import requests as req
cep = input('Entre com um CEP: ')
url = f'http://viacep.com.br/ws/{cep}/json'
resp = req.get(url).json();
logradouro = resp['logradouro']
bairro = resp['bairro']
cidade = resp['localidade']
uf = resp['uf']
print(f"{logradouro}, {bairro}, {cidade}, {uf}")