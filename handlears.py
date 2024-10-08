from telegram import Update
from telegram.ext import CallbackContext
from test_model import image_classification
async def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    await update.message.reply_text(
        text=f"""Assalomu aleykum {user.full_name}. X-Ray tasvir yuboring, tasvirni aniqlashda yordam beraman!""",
    )
    
async def covid_clasification(update: Update, context: CallbackContext):
    image = update.message.photo[0].file_id
    reslts = image_classification(image)
    await update.message.reply_text(reslts)

async def send_message(update: Update, context: CallbackContext):
    user = update.message.from_user
    await update.message.reply_text(
        text=f"""Kechirasiz {user.full_name}. Faqat tasvir yuboring!""",
    )