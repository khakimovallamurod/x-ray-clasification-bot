from telegram import Update
from telegram.ext import CallbackContext
from test_model import image_classification
import keyboards



async def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    await update.message.reply_text(
        text=f"""Assalomu aleykum {user.full_name}. X-Ray tasvir yuboring, tasvirni aniqlashda yordam beraman!""",
    )
    

async def covid_classification(update: Update, context: CallbackContext):
    # Get file id
    file_id = update.message.photo[-1].file_id
    # File dowland
    file = await context.bot.get_file(file_id)
    file_data = await file.download_as_bytearray()
    # clasification image api
    classification_url = 'http://149.28.56.114/onlychest'
    
    response = image_classification(url=classification_url, file_data=file_data)
    if round(response[1]['confidence']) == 1:
        context.user_data['photo'] = file_id
        await update.message.reply_text(
            text='Chest image ✅. Select the type of image classification',
            reply_markup=keyboards.inline_keyboard
            )
    else:
        await update.message.reply_text(
            text="❌ Siz yuborgan rasm ko'krak qafasi emas. Qaytadan tasvir yuborib tekshirib ko'ring."
        )
    
async def type_clasification(update: Update, context: CallbackContext):
    file_id = context.user_data['photo']
    type_cls = update.callback_query.data.split(":")[1]
    file = await context.bot.get_file(file_id)
    file_data = await file.download_as_bytearray()

    if type_cls == 'fourclass':
        classification_url = 'http://149.28.56.114/image'
        response = image_classification(url=classification_url, file_data=file_data)
        await update.callback_query.message.reply_text(
            text=f"{response[0]['label']} ------------ {response[0]['confidence']*100}% ✅\n{response[1]['label']} ------------ {response[1]['confidence']*100}%\n{response[2]['label']} ------------ {response[2]['confidence']*100}%\n{response[3]['label']} ------------ {response[3]['confidence']*100}%."
        )
    elif type_cls == 'iscovid':
        classification_url = 'http://149.28.56.114/iscovid'
        response = image_classification(url=classification_url, file_data=file_data)
        await update.callback_query.message.reply_text(
            text=f"{response[0]['label']} ------------ {response[0]['confidence']*100}% ✅\n{response[1]['label']} ------------ {response[1]['confidence']*100}%."
        )
    else:
        await update.callback_query.message.reply_text(
           text = "X-Ray tasvir yuboring, tasvirni aniqlashda yordam beraman." 
        )




async def send_message(update: Update, context: CallbackContext):
    user = update.message.from_user
    await update.message.reply_text(
        text=f"""Kechirasiz {user.full_name}. Faqat tasvir yuboring!""",
    )