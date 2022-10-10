from urllib import request
# добавление библиотек
import requests

# в кавычки вставить ссылку
response = requests.post("https://petstore.swagger.io/v2/pet", json={
  "id": 505,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "MyPet",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})


# вывести
print(response.text)

response = requests.put("https://petstore.swagger.io/v2/pet", json={
  "id": 505,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "MyPet2",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
)

print(response.text)

response = requests.get("https://petstore.swagger.io/v2/pet/505", json={
  "id": 505,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "MyPet",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
)

print(response.text)