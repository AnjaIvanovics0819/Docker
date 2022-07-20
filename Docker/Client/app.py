import json
import http.client

connection = http.client.HTTPConnection("localhost:5000")
objectPayload = json.dumps(
  {'ime': 'Anja',
  'prezime': 'Ivanovic',
  'username': 'Aivanovic',
  'smer': 'IT',
  'predmeti':
    [{'ime': 'AIOS', 'espb': 4},
     {'ime': 'Osnovi programiranja', 'espb': 3},
     {'ime': 'Dizajn', 'espb': 3}
    ]}
)
headers = {
  'Content-Type': 'application/json'
}

connection.request("POST", "/users", objectPayload, headers)
response = connection.getresponse()
dataDisplay = response.read()
print(dataDisplay.decode("utf-8"))