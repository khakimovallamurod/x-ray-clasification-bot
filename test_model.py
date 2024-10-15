import json
import requests

def image_classification(url, file_data):
    
    response = requests.post(url, files={'file': ('image.jpg', file_data)})
    image_data = response.json()
    return image_data


