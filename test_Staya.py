from urllib import response
import requests
import pytest
# название
def test_statuscode():
    url = "https://petstore.swagger.io/v2/pet/505"
    response = requests.get(url)
    assert response.status_code == 200

def test_check_response():
    url = "https://petstore.swagger.io/v2/pet/505"
    response = requests.get(url)
    response = response.json()
    assert response['name'] == 'MyPet2'