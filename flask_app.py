from flask import Flask, request
from test_model import image_classification
from PIL import Image
from telegram import Bot, Update
from config import get_token
from test_model import image_classification


TOKEN = get_token()
bot = Bot(TOKEN)
app = Flask(__name__)
url = 'https://codeschoolacademy.pythonanywhere.com/'

@app.route('/', methods=['POST'])  
def main():
    data = request.get_json()
    user = data['message']['chat']
    if data['message'].get('text')=='/start':
        bot.send_message(
            chat_id = user['id'],
            text=f"""Assalomu aleykum {user['first_name']}. X-Ray tasvir yuboring, tasvirni aniqlashda yordam beraman!""",
            )
    elif data['message'].get('photo') != None:
        image = data['message']['photo'][0]['file_id']
        results = image_classification(image)
        bot.send_photo(photo=image, caption=f'{results}')
    
    else:
        bot.send_message(
            chat_id = user['id'],
            text=f'Please {user["first_name"]} send me the photo. My function below only works on images',
            )
        
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
